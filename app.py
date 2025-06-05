from flask import Flask, redirect, render_template_string, request
import os

app = Flask(__name__)

index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Free Robux Generator</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:700">
    <style>
        body {
            background: linear-gradient(135deg, #77e9ff, #ffe877);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Roboto', sans-serif;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 8px 40px rgba(0,0,0,0.15);
            padding: 3em 4em;
            text-align: center;
        }
        h1 {
            color: #24b47e;
            margin-bottom: .5em;
        }
        button {
            background: #24b47e;
            color: white;
            font-size: 1.4em;
            padding: .7em 2.5em;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-weight: 700;
            transition: background .2s;
            margin-top: 1.5em;
        }
        button:hover {
            background: #167755;
        }
        .subtitle {
            color: #444;
            margin-bottom: 2em;
            font-size: 1.1em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Free Robux Generator</h1>
        <div class="subtitle">Click the button below and get unlimited Robux instantly!</div>
        <form action="/generate" method="post">
            <button type="submit">Generate Robux</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(index_html)

@app.route("/generate", methods=["POST"])
def generate():
    # Rickroll!
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
