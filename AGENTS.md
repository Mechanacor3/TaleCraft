# Agent Contribution Guidelines

This document outlines conventions and checks for any automated or human contributor working in this repository.

## Repository Structure
- `backend/` – Python FastAPI backend for AI agents
- `frontend/` – React + TypeScript user interface
- `PLANNING.md` – project roadmap

## Coding Standards

### Python
- Target Python 3.12. Format code with `black` (default settings).
- Follow PEP 8 style and keep functions small and typed.
- Prefer `async` functions for I/O bound tasks.

### TypeScript/React
- Use functional components and React hooks.
- Format code with Prettier (`npx prettier -w` before committing).
- Organize UI pieces under `frontend/src/components`.

## Commits and Pull Requests
- Write concise commit messages in the imperative mood (e.g. "Add API route").
- Separate unrelated changes into different commits.
- Pull requests should describe the changes and reference any related issues.

## Programmatic Checks
Run these commands from the repository root before opening a PR:

```bash
# Backend checks
python -m py_compile $(git ls-files '*.py')
black --check backend/src

# Frontend checks
cd frontend && npx tsc --noEmit && npx prettier -c src && cd ..
```

If any command fails and you cannot resolve it, mention the failure in the PR summary.

## Local Development
See `backend/README.md` and `frontend/README.md` for setup details. Keep documentation updated when adding new features.
