# Configuration settings for the ShortVideo Story Creator application

import os


class Config:
    # General configuration
    DEBUG = os.getenv("DEBUG", "False") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")

    # Demo mode bypasses calls to external services like OpenAI and returns
    # predefined data instead. Enable by setting `DEMO_MODE=true` in the
    # environment when running tests or local demos.
    DEMO_MODE = os.getenv("DEMO_MODE", "False").lower() == "true"

    # Serve a prebuilt frontend with the backend. Defaults to True so containers
    # include the static assets built in the Docker image.
    SERVE_FRONTEND = os.getenv("SERVE_FRONTEND", "True").lower() == "true"

    # OpenAI API configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

    # Audio processing settings
    AUDIO_SAMPLE_RATE = 44100  # Sample rate for audio processing
    AUDIO_CHANNELS = 2  # Number of audio channels (1 for mono, 2 for stereo)

    # Other configurations can be added here as needed
