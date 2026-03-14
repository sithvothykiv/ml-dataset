# ML Deploy Flask Demo

A small demonstration project that trains a machine learning model and serves predictions via a Flask web service.

Repository structure

- `train.py` — training script that reads `data.csv` and writes a serialized model file `model_C=1.0.bin` (a tuple with a DictVectorizer and a classifier).
- `serve_predict.py` — Flask application exposing a `/predict` POST endpoint that returns churn probability and a binary churn decision as JSON.
- `model_C=1.0.bin` — pretrained model used by the Flask app (serialized with pickle).
- `test_flask.py` — example or test client for the Flask service.
- `data.csv` — example dataset used for training (if you want to re-train).

What is Flask?
Flask is a lightweight Python web framework for building web applications and HTTP APIs. It provides an easy-to-use routing system, request/response handling, and utilities for working with JSON and HTTP methods. In this project Flask is used to create a small API that accepts a JSON payload describing a customer and returns a JSON response containing the churn probability and a boolean churn prediction.

Prerequisites

- General: Python 3.8+ installed; basic command-line experience.

macOS (zsh)

1. Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate

2. Upgrade pip and install dependencies from `requirements.txt`:

   pip install --upgrade pip
   pip install -r requirements.txt

Windows (PowerShell or Command Prompt)

1. Open PowerShell or CMD in the project folder.

2. Create a virtual environment:

   python -m venv venv

3. Activate the virtual environment:

- PowerShell:

  .\venv\Scripts\Activate.ps1

- Command Prompt (cmd.exe):

  .\venv\Scripts\activate

4. Upgrade pip and install dependencies from `requirements.txt`:

   python -m pip install --upgrade pip
   pip install -r requirements.txt

Note: On some Windows systems you may need to adjust the PowerShell execution policy to allow running scripts. Run PowerShell as Administrator and execute:

   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Troubleshooting: "Activate.ps1 cannot be loaded because running scripts is disabled on this system"

If, when activating the virtual environment in PowerShell, you see an error like:

   ".\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system."

Fixes and alternatives:

- Recommended (allow scripts for current user):

  Open PowerShell (not necessarily as Administrator) and run:

  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

  This permits locally-created scripts to run for your user without changing system-wide policy.

- Temporary bypass (no persistent change):

  Run the activation command with a bypass for the current process:

    powershell -ExecutionPolicy Bypass -NoProfile -Command "& '.\\venv\\Scripts\\Activate.ps1'"

- Use the Command Prompt activation instead of PowerShell:

    .\\venv\\Scripts\\activate

- In VS Code: use the Command Palette (Ctrl/Cmd+Shift+P) -> "Python: Select Interpreter" -> choose the interpreter inside `venv`. VS Code will manage activation for integrated terminals and debugging.

Linux (bash)

1. Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate

2. If you get an error about the venv module missing, install system packages (Debian/Ubuntu):

   sudo apt update
   sudo apt install python3-venv python3-dev build-essential -y

3. Upgrade pip and install dependencies from `requirements.txt`:

   pip install --upgrade pip
   pip install -r requirements.txt

   Optionally, create a `requirements.txt` with those packages and install via `pip install -r requirements.txt`.
4. (Optional) Train a new model:

   If you want to create a fresh `model_C=1.0.bin` from `data.csv`, run:

   python train.py

   After running, a new `model_C=1.0.bin` will be produced. If you prefer, use the included `model_C=1.0.bin`.
5. Start the Flask service:

   python serve_predict.py

   The app will start in debug mode and listen on `localhost:9696` by default (see the bottom of `serve_predict.py`).
6. Send a prediction request:

   The `/predict` endpoint expects a JSON object with the same feature names used during training. Check `train.py` or `data.csv` for the expected keys. Example using `curl` (replace keys with real feature names):

   curl -X POST -H "Content-Type: application/json" -d '{"feature_1": "value1", "feature_2": 42, "feature_3": "value3"}' http://localhost:9696/predict

   Example response:

   {
   "churn_probability": 0.123,
   "churn": false
   }
7. Run tests or example client:

   If `test_flask.py` contains example calls, you can run it while the service is running:

   python test_flask.py

Notes

- The Flask app returns JSON with primitive types (floats and booleans). The `serve_predict.py` script converts NumPy types to native Python `float` and `bool` to avoid JSON serialization issues.
- For production deployments, consider using a production WSGI server (e.g. gunicorn) and disabling Flask debug mode.
