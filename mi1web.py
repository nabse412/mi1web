from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # Ruta principal
def home():
    return render_template("index.html")  # Renderiza la página "index.html"

if __name__ == "__main__":
    app.run(debug=True)
