# Devops_flask

A minimal Flask example app that demonstrates:

- Rendering a Jinja2 template (`templates/index.html`) and passing a value (current day of week).
- A tiny JSON API that serves `data.json` at `/api`.
- A simple endpoint `/name` that returns the `name` and `age` parameters from the request.

This repository is intended as a small learning/demo project for Flask and basic API/template usage.

## What the app contains

- `app.py` — main Flask application. Key routes:
	- `/` : renders `templates/index.html` and passes `day_of_week` to the template.
	- `/name` : reads `name` and `age` from request values and returns them as a JSON-like dict.
	- `/api` : reads and returns the contents of `data.json` as JSON.
- `data.json` — sample JSON data used by the `/api` endpoint.
- `templates/index.html` — simple form and a line that shows the current day of the week.

## Requirements

- Python 3.8+ (should work with 3.7 as well but 3.8+ is recommended)
- Flask (installable via pip)

There is no `requirements.txt` in the repo; the only required package for this project is Flask.

## Quick start (Windows PowerShell)

Open PowerShell in the project folder and run:

```powershell
# create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# install Flask
pip install Flask

# run the app
python app.py
```

Then open your browser at http://127.0.0.1:5000/

## Endpoints and examples

- Home page
	- `GET /` — renders the HTML form in `templates/index.html` and shows the current day (template variable `day_of_week`).

- API (data.json)
	- `GET /api` — returns the contents of `data.json` as JSON.
		- Example (PowerShell):
			```powershell
			Invoke-RestMethod -Uri "http://127.0.0.1:5000/api"
			```

- Name endpoint
	- `GET /name?name=Alice&age=30` — returns a JSON-like response with `name` and `age`.
		- Example (PowerShell):
			```powershell
			Invoke-RestMethod -Uri "http://127.0.0.1:5000/name?name=John&age=30"
			```

Note: the `/name` route in `app.py` returns a Python dict (Flask will convert that to a JSON response). It accepts values from query-string or body-encoded form values via `request.values`.

## Data format

`data.json` contains a JSON array of simple objects with `name` and `age` fields. Example:

```json
[
	{"name": "Alice", "age": 30},
	{"name": "Bob", "age": 25}
]
```

## Templates

`templates/index.html` is a small HTML page with a form. It also prints the `day_of_week` variable passed from the server.

Important note: the form in `templates/index.html` posts to `/submit` with method `post`, but `app.py` does not implement a `/submit` route. Options to fix or test the form:

- Change the form to use `action="/name"` and `method="get"` to test the `/name` endpoint directly from the page.
- Or implement a `@app.route('/submit', methods=['POST'])` handler in `app.py` that processes the submitted form.

## Development notes

- The app is started with `debug=True` in `app.py`. That is convenient for development but should be disabled in production.
- If you plan to package the project or add more dependencies, add a `requirements.txt` (for example `pip freeze > requirements.txt`).

## Next steps / suggestions

- Add a `requirements.txt` and optionally a `Procfile` or Dockerfile for deployment.
- Implement the missing `/submit` route or update the form to match an existing route.
- Add tests (e.g., pytest + Flask test client) for the API endpoints.

## License

No license specified. Add a `LICENSE` file if you want to make this project open-source under a specific license.

## Contact / Author

This repository is a small demo. If you want help extending it (adding tests, Dockerfile, or CI), open an issue or update the project.
