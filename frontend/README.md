# YouTube Story Creator App

## Overview

The YouTube Story Creator App is an interactive, browser-based application powered by OpenAI that assists users in generating engaging stories for short YouTube videos. The app allows for full interactivity at each stage of the story creation process, from initial idea input to final video production.

## Features

- **Interactive Story Outline:** Users can input story ideas via text or speech, and the app generates a detailed outline interactively.
- **Storyboarding:** AI generates a beat-by-beat storyboard, allowing users to approve or modify each beat.
- **Image Generation:** Generate images for each storyboard beat using DALL·E 3, with options for user adjustments.
- **Script Alignment:** Create a script that aligns with images and narration, with user-editable dialogue.
- **Text-to-Speech:** Select voice styles for narration and generate audio clips.
- **Video Assembly:** Assemble images, narration, and animations for a final video preview.
- **Final Production:** Export the final video and provide direct upload options to YouTube.

## Tech Stack

- **Frontend:** React.js, Tailwind CSS, Framer Motion
- **AI Backend:** OpenAI Agents Python library, GPT-4.5, DALL·E 3
- **Audio Integration:** OpenAI Whisper (STT), Eleven Labs or browser-native TTS
- **Video Generation:** FFmpeg WASM

## Development Roadmap

1. **Initial Setup:** Set up OpenAI Agents and React project.
2. **Interactive Workflow:** Build React components and Agent backend.
3. **Integration:** Integrate STT/TTS and image generation (DALL·E).
4. **Production:** Develop video creation workflow using FFmpeg WASM.
5. **Deployment:** Deploy using Vercel or Netlify with secure serverless functions.

## Future Enhancements

- Real-time voice command integration
- Advanced editing tools
- Integrated sound effects and music libraries

## Getting Started

1. Clone the repository.
2. Install dependencies using `npm install`.
3. Start the development server with `npm start`.
4. Open your browser and navigate to `http://localhost:3000` to view the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
