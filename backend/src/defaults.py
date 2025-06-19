"""Default data used when DEMO_MODE is enabled."""

from pathlib import Path

# Path to a placeholder image served when image generation is bypassed.
DEFAULT_IMAGE_PATH = str(
    Path(__file__).resolve().parent.parent / "static" / "default.png"
)

# Text returned by the speech-to-text processor in demo mode.
DEFAULT_TRANSCRIPTION = "This is a sample transcription."

# Default script lines returned by the script alignment agent in demo mode.
DEFAULT_SCRIPT_LINES = [
    "This is a demo script line one.",
    "Here is demo line two matching an image.",
    "Finally demo line three completes the sample.",
]

# Additional defaults can be added here as needed.
