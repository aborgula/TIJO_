from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Klucz API 
genai.configure(api_key="AIzaSyCtsV6aMG5mhUvacPJt1DXLPsMWAh9i2DQ")

# Wybierz model - najnowszy Gemini 2.0
model = genai.GenerativeModel("gemini-2.0-flash-exp")

app = Flask(__name__)

# Prompt bazowy
base_prompt = (
    "Jesteś ekspertem od testowania i jakości oprogramowania. "
    "Twoim zadaniem jest analizować kod źródłowy pod kątem zasad SOLID, OOP, DRY, KISS, Law of Demeter oraz wykrywać błędy i 'code smells'. "
    "Oceniaj profesjonalnie, zwięźle i rzeczowo. "
    "Jeśli to możliwe, zaproponuj konkretne poprawki lub lepsze praktyki."
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        code = data.get("code", "")
        prompt = data.get("prompt", "")
        analysis_type = data.get("analysis", "Ogólna analiza")

        # 🔧 Składamy pełny prompt
        full_prompt = (
            base_prompt + "\n\n"
            f"Typ analizy: {analysis_type}.\n"
            f"{prompt.strip() if prompt else ''}\n\n"
            f"Kod:\n{code}"
        )

        # 📡 Wysyłamy zapytanie do modelu
        response = model.generate_content(full_prompt)
        
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
