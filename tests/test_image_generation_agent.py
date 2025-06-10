import os
from unittest.mock import MagicMock, patch

from backend.src.agents.image_generation_agent import ImageGenerationAgent


def test_generate_image_returns_url():
    agent = ImageGenerationAgent("key")
    with patch("openai.Image.create") as mock_create:
        mock_create.return_value = {"data": [{"url": "http://img"}]}
        url = agent.generate_image("a cat")
        assert url == "http://img"
        mock_create.assert_called_once_with(prompt="a cat", n=1)


def test_modify_image_returns_url(tmp_path):
    agent = ImageGenerationAgent("key")
    img = tmp_path / "test.png"
    img.write_bytes(b"data")
    with patch("openai.Image.create_edit") as mock_edit:
        mock_edit.return_value = {"data": [{"url": "http://edit"}]}
        url = agent.modify_image(str(img), "prompt")
        assert url == "http://edit"
        assert mock_edit.called


def test_regenerate_image_returns_url(tmp_path):
    agent = ImageGenerationAgent("key")
    img = tmp_path / "test.png"
    img.write_bytes(b"data")
    with patch("openai.Image.create_variation") as mock_var:
        mock_var.return_value = {"data": [{"url": "http://var"}]}
        url = agent.regenerate_image(str(img))
        assert url == "http://var"
        assert mock_var.called


def test_get_image_local_file(tmp_path):
    agent = ImageGenerationAgent()
    img = tmp_path / "test.png"
    img.write_text("data")
    assert agent.get_image(str(img)) == str(img)


def test_get_image_downloads_url(tmp_path):
    agent = ImageGenerationAgent()
    resp = MagicMock()
    resp.content = b"abc"
    resp.raise_for_status = MagicMock()
    with patch("requests.get", return_value=resp) as mock_get:
        path = agent.get_image("http://example.com/img.png")
        assert os.path.isfile(path)
        with open(path, "rb") as f:
            assert f.read() == b"abc"
        mock_get.assert_called_once_with("http://example.com/img.png", timeout=10)
