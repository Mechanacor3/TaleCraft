# YouTube Story Creator Backend

This repository contains the backend for the YouTube Story Creator application, an interactive platform powered by OpenAI technologies that helps users generate engaging stories for short YouTube videos.

## Project Structure

```
youtube-story-creator-backend
├── src
│   ├── agents                # Contains agent classes for story generation, image creation, script alignment, TTS, and video assembly.
│   ├── audio_processing      # Contains classes and utilities for speech-to-text and text-to-speech processing.
│   ├── routes                # Contains API route handlers for different functionalities.
│   ├── utils                 # Contains utility functions for various tasks.
│   ├── app.py                # Entry point of the backend application.
│   └── config.py             # Configuration settings for the application.
├── requirements.txt          # Lists dependencies required for the backend application.
├── Dockerfile                # Instructions for building a Docker image for the backend application.
└── README.md                 # Documentation for the project.
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd youtube-story-creator-backend
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**
   Update the `src/config.py` file with your API keys and any other necessary configuration settings.

4. **Run the application:**
   Start the backend server using:
   ```bash
   python src/app.py
   ```

## Usage Guidelines

- The backend provides various API endpoints for interacting with the story creation process, including story generation, image creation, script alignment, audio processing, and video assembly.
- Refer to the individual route files in `src/routes` for detailed information on available endpoints and their usage.

## Future Enhancements

- Integration of real-time voice command features.
- Advanced editing tools for improved user experience.
- Additional audio processing capabilities, including sound effects and music libraries.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.