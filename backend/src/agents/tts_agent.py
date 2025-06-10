from typing import Any, Dict, Iterable, List

from pydub import AudioSegment

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
        self, audio_clip: AudioSegment, properties: Dict[str, Any]
    ) -> AudioSegment:
        """Adjust volume and speed of an audio clip."""

        result = audio_clip
        if "volume" in properties:
            result = result + float(properties["volume"])
        if "speed" in properties:
            speed = float(properties["speed"])
            if speed != 1.0:
                result = result.speedup(playback_speed=speed)
        return result

    def get_available_voices(self) -> Iterable[str]:
        """Return a list of supported voice styles."""

        return list(self._available_voices)
