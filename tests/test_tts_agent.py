from unittest.mock import MagicMock
import wave
import os

from backend.src.agents.tts_agent import TTSAgent
from backend.src.audio_processing.tts import TTSProcessor


def create_silent_wav(path: str, duration_ms: int) -> None:
    nframes = int(44100 * duration_ms / 1000)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(b"\x00\x00" * nframes)


def test_select_voice_style_updates_processor():
    processor = MagicMock(spec=TTSProcessor)
    agent = TTSAgent(processor)
    agent._available_voices = ["default", "calm"]
    agent.select_voice_style("calm")
    processor.set_voice_style.assert_called_once_with("calm")


def test_generate_audio_delegates_to_processor():
    processor = MagicMock(spec=TTSProcessor)
    processor.generate_audio.return_value = "clip"
    agent = TTSAgent(processor)
    agent._available_voices = ["default"]
    result = agent.generate_audio("hello", "default")
    processor.set_voice_style.assert_called_once_with("default")
    processor.generate_audio.assert_called_once_with("hello")
    assert result == "clip"


def test_adjust_audio_properties_modifies_clip(tmp_path):
    wav = tmp_path / "in.wav"
    create_silent_wav(wav, 1000)
    agent = TTSAgent(MagicMock())

    louder = agent.adjust_audio_properties(str(wav), {"volume": 5})
    assert os.path.exists(louder)

    faster = agent.adjust_audio_properties(str(wav), {"speed": 2.0})
    assert os.path.exists(faster)


def test_generate_audio_clip_uses_processor():
    processor = MagicMock(spec=TTSProcessor)
    processor.generate_audio.return_value = "result"
    agent = TTSAgent(processor)

    clip = agent.generate_audio_clip("hi")

    processor.generate_audio.assert_called_once_with("hi")
    assert clip == "result"
