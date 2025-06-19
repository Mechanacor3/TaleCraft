"""Default data used when DEMO_MODE is enabled."""

from pathlib import Path

# Path to a placeholder image served when image generation is bypassed.
DEFAULT_IMAGE_PATH = str(
    Path(__file__).resolve().parent.parent / "static" / "default.png"
)

# Text returned by the speech-to-text processor in demo mode.
DEFAULT_TRANSCRIPTION = "This is a sample transcription."

# Story outline returned by the story agent when demo mode is enabled.
DEFAULT_STORY_OUTLINE = "This is a sample story outline."

# Additional defaults can be added here as needed.
