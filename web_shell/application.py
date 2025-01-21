from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/exec', methods=['GET'])
def exec_command():
    # Get the shell command from the query parameters
    command = request.args.get('command')
    
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    # Ideally, validate and sanitize the command here!
    
    try:
        # Running the command securely with subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
