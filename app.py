from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route("/")
def index():
    env = os.getenv("ENVIRONMENT", None)
    return {
        "env": env
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Needs port number as a commandline argument.")
        sys.exit(1)
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
