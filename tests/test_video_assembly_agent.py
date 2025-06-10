import os
from pathlib import Path

from backend.src.agents.video_assembly_agent import VideoAssemblyAgent
from pydub import AudioSegment
from PIL import Image


def create_image(path: Path) -> None:
    img = Image.new("RGB", (64, 64), color="blue")
    img.save(path)


def create_audio(path: Path, duration: int = 500) -> None:
    AudioSegment.silent(duration=duration).export(path, format="wav")


def test_assemble_video_creates_file(tmp_path: Path) -> None:
    imgs = []
    auds = []
    for i in range(2):
        img = tmp_path / f"img{i}.png"
        aud = tmp_path / f"audio{i}.wav"
        create_image(img)
        create_audio(aud)
        imgs.append(str(img))
        auds.append(str(aud))
    output = tmp_path / "output.mp4"
    agent = VideoAssemblyAgent()
    agent.assemble_video(imgs, auds, str(output))
    assert output.exists()


def test_preview_and_upload_return_dict() -> None:
    agent = VideoAssemblyAgent()
    preview = agent.preview_video("demo.mp4")
    assert preview == {"message": "Preview generated", "video_path": "demo.mp4"}

    upload = agent.upload_to_youtube("demo.mp4", "t", "d")
    assert upload["video_path"] == "demo.mp4"
    assert "message" in upload
