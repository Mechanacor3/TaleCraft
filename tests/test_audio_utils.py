import wave

import pytest

from backend.src.audio_processing import audio_utils


def create_silent_wav(path: str, duration_ms: int) -> None:
    nframes = int(44100 * duration_ms / 1000)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(b"\x00\x00" * nframes)


from pathlib import Path


def test_merge_audio_clips_combines_lengths(tmp_path: Path) -> None:
    f1 = tmp_path / "a.wav"
    f2 = tmp_path / "b.wav"
    create_silent_wav(f1, 500)
    create_silent_wav(f2, 700)
    out = audio_utils.merge_audio_clips([str(f1), str(f2)])
    with wave.open(out) as wf:
        duration = wf.getnframes() / wf.getframerate()
    assert duration == pytest.approx(1.2, rel=0.01)


def test_adjust_volume_keeps_duration(tmp_path: Path) -> None:
    f = tmp_path / "a.wav"
    create_silent_wav(f, 1000)
    out = audio_utils.adjust_volume(str(f), 5)
    with wave.open(out) as wf_out, wave.open(str(f)) as wf_in:
        assert wf_out.getnframes() == wf_in.getnframes()


def test_export_audio_creates_file(tmp_path: Path) -> None:
    f = tmp_path / "a.wav"
    out = tmp_path / "out.mp3"
    create_silent_wav(f, 100)
    audio_utils.export_audio(str(f), str(out), format="mp3")
    assert out.exists()
