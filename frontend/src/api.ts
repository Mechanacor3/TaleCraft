export const DEMO_ENDPOINT = "http://localhost:8000";

const demoMode = import.meta.env.VITE_DEMO_MODE === "true";

export const API_BASE = demoMode
  ? import.meta.env.VITE_DEMO_ENDPOINT || DEMO_ENDPOINT
  : "";

export function apiFetch(
  path: string,
  options?: RequestInit,
): Promise<Response> {
  const url = `${API_BASE}${path}`;
  return fetch(url, options);
}
