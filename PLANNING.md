## ShortVideo Story Creator App (OpenAI-powered)

### Project Goal
Create an interactive, browser-based, OpenAI-powered application that helps users generate engaging stories for short videos, with full interactivity at each stage.

---

## Tech Stack
- **Monorepo Setup:** Vite
- **Frontend:** React.js, Tailwind CSS, Framer Motion
- **AI Backend:** OpenAI Agents Python library, GPT-4.5, DALL·E 3
- **Audio Integration:** OpenAI Whisper (STT), Eleven Labs or browser-native TTS
- **Video Generation:** FFmpeg WASM

---

## Development Roadmap

### 1. Interactive Story Outline
- Users input a story idea (speech or text)
- GPT-4.5 generates and refines a detailed story outline interactively.
- Agentic conversation enabling deep collaboration and modifications.

### User Interaction:
- Story idea input (voice or text)
- Interactive outline refinement

---

### 2. Interactive Storyboarding
- AI generates a detailed beat-by-beat storyboard.
- User approval and modification at each story beat.

### User Interaction:
- Approve/edit story beats
- Edit or rearrange storyboard visually

---

### 3. Image Generation with DALL·E
- Generate images for each storyboard beat using OpenAI's DALL·E 3.
- Interactive user adjustments and regeneration capabilities.

### User Interaction:
- Modify image generation prompts
- Regenerate images interactively

---

### 3. Script and Narration Alignment
- AI creates a script matching images with narration/dialogue.
- Users can edit and adjust dialogue and narration script.

### User Interaction:
- Modify script directly
- Adjust narration-to-image timing

---

### 4. Text-to-Speech and Audio Production
- Select voices for narration and characters.
- Generate audio clips using TTS API.

### User Interaction:
- Choose voice style
- Edit narration and regenerate audio

---

### 4. Video Assembly and Animation
- Images, narration audio, and animations (pan, zoom, transitions).
- Preview and customization of animation styles.

### User Interaction:
- Customize image animations
- Preview video in-browser

---

### 5. Final Production and Export
- Assemble final video with FFmpeg WASM.
- Provide a direct ShortVideo upload option.

### User Interaction:
- Final preview and download
- Direct upload integration to ShortVideo (OAuth)

---

### Implementation Roadmap:
1. **Initial Setup:** OpenAI Agents & React Project Setup
2. **Interactive Workflow:** Build React components & Agent backend
3. **Integration:** STT/TTS and image generation (DALL·E)
4. **Production:** Video creation workflow via FFmpeg WASM
5. **Deployment:** Vercel or Netlify static deployment with secure serverless functions

---

### Future Enhancements:
- Real-time voice command integration
- Advanced editing tools
- Integrated sound effects and music libraries

---

**Next Steps:**
- Begin setting up development environment and basic React frontend
- Establish OpenAI Agents workflow for AI interaction

