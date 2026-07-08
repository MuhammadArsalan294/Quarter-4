# FastAPI Backend Starter

A simple, beginner-friendly FastAPI backend project.

## Project Structure
```text
├── app/
│   └── main.py    # Entry point for the application
├── pyproject.toml # Dependency management (uv compatible)
└── README.md      # Instructions
```

## Setup and Running the Project

Follow these steps to manually set up and run your project.

### Step 1: Create a Virtual Environment
A virtual environment keeps your project dependencies isolated.
```powershell
python -m venv .venv
```
**Explanation:** This command uses Python's built-in `venv` module to create a folder named `.venv` containing its own Python executable and pip.

### Step 2: Activate the Virtual Environment
Activating ensures any command you run (like `pip` or `python`) uses the virtual environment.
```powershell
.\.venv\Scripts\Activate.ps1
```
**Explanation:** This script updates your shell's path to use the environment's Python version.

### Step 3: Install Dependencies
We'll use `uv` for lightning-fast dependency installation.
```powershell
uv pip install -e .
```
**Explanation:** This command uses `uv` to read `pyproject.toml` and install the necessary packages (`fastapi` and `uvicorn`) into your active virtual environment.

### Step 4: Run the Project
Start the development server with Uvicorn.
```powershell
uvicorn app.main:app --reload
```
**Explanation:** 
- `app.main:app` tells Uvicorn to look for an object named `app` inside the `app/main.py` file.
- `--reload` tells the server to automatically restart whenever you make changes to your code.

### Step 5: Verify
Open your browser and navigate to:
- `http://127.0.0.1:8000/` – to see the "Hello World" response.
- `http://127.0.0.1:8000/docs` – to see the interactive API documentation.
