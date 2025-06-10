from unittest.mock import MagicMock
from pydub import AudioSegment

from backend.src.agents.tts_agent import TTSAgent
from backend.src.audio_processing.tts import TTSProcessor


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


def test_adjust_audio_properties_modifies_clip():
    clip = AudioSegment.silent(duration=1000)
    agent = TTSAgent(MagicMock())

    louder = agent.adjust_audio_properties(clip, {"volume": 5})
    assert len(louder) == len(clip)

    faster = agent.adjust_audio_properties(clip, {"speed": 2.0})
    assert len(faster) < len(clip)


def test_generate_audio_clip_uses_processor():
    processor = MagicMock(spec=TTSProcessor)
    processor.generate_audio.return_value = "result"
    agent = TTSAgent(processor)

    clip = agent.generate_audio_clip("hi")

    processor.generate_audio.assert_called_once_with("hi")
    assert clip == "result"
