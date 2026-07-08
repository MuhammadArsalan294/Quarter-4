# FastAPI Starter Project

A simple and beginner-friendly FastAPI starter project using `uv` for dependency management.

## Getting Started

Follow these steps to set up and run your project manually:

### 1. Create a Virtual Environment
First, create a virtual environment to isolate your project dependencies:
```bash
python -m venv .venv
```
*Explanation: This command creates a folder named `.venv` that will contain your project's local Python installation and packages.*

### 2. Activate the Virtual Environment
Activate the environment to start using it:
- **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```
*Explanation: This step tells your terminal to use the Python environment we just created.*

### 3. Install Dependencies
Use `uv` to install the dependencies defined in `pyproject.toml` into your active virtual environment:
```bash
uv pip sync pyproject.toml
```
*Alternatively, you can use `pip install .` if you don't have `uv` installed.*

### 4. Run the Project
Start the FastAPI development server with `uvicorn`:
```bash
uvicorn main:app --reload
```
*Explanation: `main:app` refers to the `app` object in `main.py`. `--reload` makes the server automatically restart whenever you change your code.*

### 5. Access the API
- **Open your browser at:** [http://127.0.0.1:8000](http://127.0.0.1:8000) (You should see `{"message": "Hello World"}`)
- **Interactive Documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
