"""Run this to check Gemini end-to-end:   venv\Scripts\python.exe test_gemini.py

It tries English, Hindi and Kannada and prints the exact error if anything
fails (wrong key, retired model, no quota, timeout...).
"""
import sys
import gemini_explainer as G

if not G.status()["configured"]:
    sys.exit("GEMINI_API_KEY is empty. Put your key in the .env file "
             "(copy .env.example to .env first).")

print("Models:", G.MODEL, "(backup:", G.BACKUP_MODEL + ")\n")

detection = {
    "risk_score": 85, "risk_level": "HIGH", "classification": "PHISHING",
    "components": {"rule_score": 45, "url_score": 75},
    "findings": ["Message asks for an OTP", "Link imitates the SBI brand"],
}
msg = "Your SBI account will be blocked. Share OTP and update KYC now."

for lang in ("en", "hi", "kn"):
    out = G.explain(msg, detection, lang)
    ok = out.get("ai_generated")
    print(f"[{lang}] AI worked: {ok}")
    print("   ", out["short_summary"])
    if not ok:
        print("    REASON:", G.last_error)
    print()
