# BraveSearch

A Django lab with a dark Brave Search interface.

- `/` is the search homepage. Submitting the form opens Brave Search results.
- `/terms/` summarizes Brave’s Terms of Use and links to the official text.

Both pages extend a shared template and use named Django URLs. The Brave logo, Inter font, and terms content live in `resources`.

## Run locally (Windows PowerShell)

Tested with Python 3.14.8.

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py check
.\venv\Scripts\python.exe manage.py runserver
```

Open [BraveSearch](http://127.0.0.1:8000/).
