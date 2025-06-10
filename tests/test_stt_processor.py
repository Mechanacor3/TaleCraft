from backend.src.audio_processing.stt import STTProcessor
import openai
import pytest


def test_get_and_set_model():
    stt = STTProcessor(model="model1")
    assert stt.get_model() == "model1"
    stt.set_model("model2")
    assert stt.get_model() == "model2"


def test_transcribe_audio_returns_text(monkeypatch, tmp_path):
    audio_path = tmp_path / "clip.mp3"
    audio_path.write_bytes(b"data")

    def mock_transcribe(model, file, **kwargs):
        assert model == "whisper-1"
        file.read()  # ensure file object is usable
        return {"text": "hello world"}

    monkeypatch.setattr(openai.Audio, "transcribe", mock_transcribe)
    stt = STTProcessor(model="whisper-1")
    text = stt.transcribe_audio(str(audio_path))
    assert text == "hello world"


def test_transcribe_audio_missing_file():
    stt = STTProcessor(model="whisper-1")
    with pytest.raises(FileNotFoundError):
        stt.transcribe_audio("nonexistent.mp3")
