# TaleCraft
An interactive, agentic web app powered by OpenAI to create AI-driven storyboards and short videos, enabling easy, user-driven storytelling.

## Integration Testing

To experiment with the complete stack locally, you can run the backend in
`DEMO_MODE`. This bypasses all OpenAI endpoints and serves a small frontend build
mounted at the FastAPI root path.

Steps:

1. Build the frontend:

   ```bash
   cd frontend && npm install && npm run build
   ```

2. Start the backend with demo mode enabled:

   ```bash
   cd backend && uvicorn src.app:app
   ```

Visit `http://localhost:8000` in your browser to see the demo interface. API
routes will return default data suitable for manual testing.
