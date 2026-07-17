
from flask import Flask,render_template,request,jsonify
import google.generativeai as genai
API_KEY=""   # Paste your Gemini API key here
app=Flask(__name__)
model=None
if API_KEY:
    genai.configure(api_key=API_KEY)
    model=genai.GenerativeModel("gemini-2.5-flash")
@app.route("/")
def home(): return render_template("index.html")
@app.post("/chat")
def chat():
    msg=request.json["message"]
    if model:
        reply=model.generate_content(msg).text
    else:
        reply="Gemini API key not configured."
    return jsonify(reply=reply)
if __name__=="__main__":
    app.run(debug=True)
