import pytest
from pydub import AudioSegment
from backend.src.audio_processing import audio_utils
from unittest.mock import MagicMock


def test_merge_audio_clips_combines_lengths():
    clip1 = AudioSegment.silent(duration=500)
    clip2 = AudioSegment.silent(duration=700)
    combined = audio_utils.merge_audio_clips([clip1, clip2])
    assert len(combined) == len(clip1) + len(clip2)


def test_adjust_volume_keeps_duration():
    clip = AudioSegment.silent(duration=1000)
    adjusted = audio_utils.adjust_volume(clip, 5)
    assert len(adjusted) == len(clip)


def test_export_audio_calls_export():
    mock_segment = MagicMock()
    audio_utils.export_audio(mock_segment, "out.mp3", format="mp3")
    mock_segment.export.assert_called_once_with("out.mp3", format="mp3")
