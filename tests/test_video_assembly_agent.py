from pathlib import Path

from backend.src.agents.video_assembly_agent import VideoAssemblyAgent
import wave
from PIL import Image


def create_image(path: Path) -> None:
    img = Image.new("RGB", (64, 64), color="blue")
    img.save(path)


def create_audio(path: Path, duration: int = 500) -> None:
    nframes = int(44100 * duration / 1000)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(b"\x00\x00" * nframes)


def test_assemble_video_creates_file(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DEMO_MODE", "true")
    imgs = []
    auds = []
    for i in range(2):
        img = tmp_path / f"img{i}.png"
        aud = tmp_path / f"audio{i}.wav"
        create_image(img)
        create_audio(aud)
        imgs.append(str(img))
        auds.append(str(aud))
    output = tmp_path / "output.txt"
    agent = VideoAssemblyAgent()
    agent.assemble_video(imgs, auds, str(output))
    assert output.exists()
    content = output.read_text().strip().splitlines()
    assert len(content) == 2
    assert "image=" in content[0]


def test_preview_and_upload_return_dict() -> None:
    agent = VideoAssemblyAgent()
    preview = agent.preview_video("demo.mp4")
    assert preview == {"message": "Preview generated", "video_path": "demo.mp4"}

    upload = agent.upload_to_shortvideo("demo.mp4", "t", "d")
    assert upload["video_path"] == "demo.mp4"
    assert "message" in upload
