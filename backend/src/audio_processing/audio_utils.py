import os
import tempfile
from typing import List, Optional

import ffmpeg


def merge_audio_clips(clips: List[str], output_path: Optional[str] = None) -> str:
    """Merge multiple audio files into one."""
    if output_path is None:
        fd, output_path = tempfile.mkstemp(suffix=os.path.splitext(clips[0])[1])
        os.close(fd)
    inputs = [ffmpeg.input(c) for c in clips]
    joined = ffmpeg.concat(*inputs, v=0, a=1)
    ffmpeg.output(joined, output_path).overwrite_output().run(quiet=True)
    return output_path


def adjust_volume(
    input_path: str, db_change: float, output_path: Optional[str] = None
) -> str:
    """Adjust the volume of an audio file by a specified number of decibels."""
    if output_path is None:
        fd, output_path = tempfile.mkstemp(suffix=os.path.splitext(input_path)[1])
        os.close(fd)
    stream = ffmpeg.input(input_path).filter("volume", f"{db_change}dB")
    ffmpeg.output(stream, output_path).overwrite_output().run(quiet=True)
    return output_path


def export_audio(input_path: str, file_path: str, format: str = "mp3") -> None:
    """Export the audio file to a different format."""
    ffmpeg.input(input_path).output(file_path, format=format).overwrite_output().run(
        quiet=True
    )
