# TrustLens API

FastAPI backend for the PhishShield extension: rule + link detection, Gemini explanations
(English, Hindi, Kannada), optional Supabase storage.

## Run (Windows)
Double-click `start_backend.bat`, or:
```
venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```
First time only: `python -m venv venv`, then `venv\Scripts\python.exe -m pip install -r requirements.txt`, then copy `.env.example` to `.env` and add your keys.

Check it works: open http://127.0.0.1:8000/health. It shows the build, the languages, and
`gemini.last_error` (the reason AI explanations failed, if they did).
Check Gemini directly: `venv\Scripts\python.exe test_gemini.py`.

Gemini and Supabase are optional: without them the API still returns detection results and a
built-in explanation, in the user's language.

## Languages
Messages can be English, Hindi (देवनागरी), Kannada (ಕನ್ನಡ) or romanised Hindi.
- `language: "auto"` (default): answer in the language of the message.
- `language: "hi"` / `"kn"`: always answer in that language.
- `language: "en"`: English, unless the message itself is Hindi/Kannada.
The response includes `language` (the one actually used).

## Endpoints
- POST /analyze: `{ "message": "...", "urls": ["..."], "language": "auto", "private_mode": true }`
  (message may be empty when only checking a link; a single `"url": "..."` is also accepted)
- POST /feedback: report a false positive
- GET /health: status check
