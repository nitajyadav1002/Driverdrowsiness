from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Run the blinkDetect.py script and capture the output
        result = subprocess.run(['python', 'blinkDetect.py'], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.output
    
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
