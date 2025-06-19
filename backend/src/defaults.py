"""Default data used when ``DEMO_MODE`` is enabled."""

from pathlib import Path
import yaml

_DEFAULTS_FILE = Path(__file__).with_name("defaults.yaml")

with _DEFAULTS_FILE.open("r", encoding="utf-8") as f:
    _DATA = yaml.safe_load(f)

DEFAULT_IMAGE_PATH = str(Path(__file__).resolve().parent.parent / _DATA["image_path"])

DEFAULT_TRANSCRIPTION: str = _DATA["transcription"]

DEFAULT_TTS_AUDIO: str = _DATA["tts_audio"]

DEFAULT_SCRIPT_LINES: list[str] = _DATA["script_lines"]

DEFAULT_STORY_OUTLINE: str = _DATA["story_outline"]

# Additional defaults can be added in ``defaults.yaml`` as needed.
