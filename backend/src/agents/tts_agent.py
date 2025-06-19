from typing import Any, Dict, Iterable, List

import os
import tempfile
import ffmpeg

from ..audio_processing.tts import TTSProcessor


class TTSAgent:
    """Wrapper around :class:`TTSProcessor` providing higher level controls."""

    def __init__(self, tts_processor: TTSProcessor | None = None) -> None:
        self.tts_processor = tts_processor or TTSProcessor()
        self._available_voices: List[str] = ["default", "excited", "calm"]

    def select_voice_style(self, style: str) -> None:
        """Select the active voice style for audio generation."""

        if style not in self._available_voices:
            raise ValueError(f"Unsupported voice style: {style}")
        self.tts_processor.set_voice_style(style)

    def generate_audio(self, text: str, voice_style: str) -> Any:
        """Generate audio for the given text using a specific voice style."""

        self.select_voice_style(voice_style)
        return self.tts_processor.generate_audio(text)

    def generate_audio_clip(self, text: str) -> Any:  # Backwards compatibility
        audio_clip = self.tts_processor.generate_audio(text)
        return audio_clip

    def adjust_audio_properties(
        self,
        input_path: str,
        properties: Dict[str, Any],
        output_path: str | None = None,
    ) -> str:
        """Adjust volume and speed of an audio file using ffmpeg."""

        stream = ffmpeg.input(input_path)
        if "volume" in properties:
            stream = stream.filter("volume", f"{float(properties['volume'])}dB")
        if "speed" in properties:
            speed = float(properties["speed"])
            if speed != 1.0:
                stream = stream.filter("atempo", speed)
        if output_path is None:
            fd, output_path = tempfile.mkstemp(suffix=os.path.splitext(input_path)[1])
            os.close(fd)
        ffmpeg.output(stream, output_path).overwrite_output().run(quiet=True)
        return output_path

    def get_available_voices(self) -> Iterable[str]:
        """Return a list of supported voice styles."""

        return list(self._available_voices)
