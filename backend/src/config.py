# Configuration settings for the YouTube Story Creator application

import os


class Config:
    # General configuration
    DEBUG = os.getenv("DEBUG", "False") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")

    # OpenAI API configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

    # Audio processing settings
    AUDIO_SAMPLE_RATE = 44100  # Sample rate for audio processing
    AUDIO_CHANNELS = 2  # Number of audio channels (1 for mono, 2 for stereo)

    # Other configurations can be added here as needed
