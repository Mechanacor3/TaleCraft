import pytest
from backend.src.agents.script_alignment_agent import ScriptAlignmentAgent
from backend.src.defaults import DEFAULT_SCRIPT_LINES, DEFAULT_IMAGE_PATH
from backend.src.config import Config


@pytest.fixture
def agent():
    return ScriptAlignmentAgent()


def test_align_script_with_images_handles_mismatched_lengths(agent):
    images = ["img1.png", "img2.png", "img3.png"]
    script = ["Hello", "World"]
    result = agent.align_script_with_images(images, script)
    assert len(result) == len(images)
    assert result[0]["image"] == "img1.png" and result[0]["dialogue"] == "Hello"
    assert result[1]["image"] == "img2.png" and result[1]["dialogue"] == "World"
    assert result[2]["image"] == "img3.png" and result[2]["dialogue"] == ""


def test_adjust_dialogue_updates_dialogue(agent):
    aligned = agent.align_script_with_images(["img1", "img2"], ["line1", "line2"])
    updated = agent.adjust_dialogue(aligned, 1, "new line")
    assert updated[1]["dialogue"] == "new line"
    assert updated[0]["dialogue"] == "line1"


def test_update_script(agent):
    new_script = ["a", "b"]
    updated = agent.update_script(new_script)
    assert agent.script == new_script
    assert updated == new_script


def test_generate_script_summary_includes_all_entries(agent):
    aligned = [
        {"image": "img1.png", "dialogue": "Hello"},
        {"image": "img2.png", "dialogue": "World"},
    ]
    summary = agent.generate_script_summary(aligned)
    assert "Image: img1.png, Dialogue: Hello" in summary
    assert "Image: img2.png, Dialogue: World" in summary


def test_align_script_with_images_demo_mode(monkeypatch, agent):
    monkeypatch.setattr(Config, "DEMO_MODE", True)
    result = agent.align_script_with_images(["img.png"], ["ignored"])
    assert len(result) == len(DEFAULT_SCRIPT_LINES)
    assert result[0]["dialogue"] == DEFAULT_SCRIPT_LINES[0]
    assert result[1]["image"].endswith("default.png")
