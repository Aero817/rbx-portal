from flask import Flask, redirect

app = Flask(__name__)

@app.route('/run-python', methods=['GET'])
def run_python():
    # Your Python logic here (e.g., logging, processing, etc.)
    print("Button was pressed! Do your stuff here.")

    # Redirect to another page (e.g. YouTube or your own page)
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
