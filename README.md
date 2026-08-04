# OCD Checklist

A checklist for those dreadful repetitive tasks. Did you lock the door? Yes — you checked it today at 12:47. Digital proof it happened. 

**[Live Site](https://ocd-checklist.onrender.com/)** 

**[Demo Video](https://1drv.ms/v/c/58c600f7cd74ce27/IQBVjNgmGBJGT5QD8gZY26PbAcFHWXuLLSKQMjxl6xcYPgc?e=X90FXP)**

## About

OCD Checklist is a small web app for logging routine safety checks (locking the door, turning off the stove, etc.) so you have a timestamped record you can look back on instead of relying on memory. It's built to give a quick, reassuring answer to "did I actually do that?"

 
<table align="center">
  <tr>
    <td align="center"><img src="docs/desktop.png" alt="Desktop view" height="400"></td>
    <td align="center"><img src="docs/mobile.png" alt="Mobile view" height="400"></td>
  </tr>
</table>


## Features

- User accounts (register / log in / log out)
- Personal task lists — create checklist items you check regularly
- Each check-off is timestamped, giving you a log of exactly when you last did something
- Simple, responsive UI

## Tech Stack

- **Backend:** [Django](https://www.djangoproject.com/) 6.0
- **Database:** PostgreSQL (via `psycopg2-binary` and `dj-database-url`)
- **Server:** Gunicorn
- **Static files:** WhiteNoise
- **Deployment:** [Render](https://render.com/)
- **Config:** `python-dotenv` for local environment variables

## Project Structure

```
OCD-Checklist/
├── accounts/       # user auth (register, login, profile)
├── config/         # Django project settings/config
├── user_tasks/     # core checklist app (tasks, check-ins)
├── static/css/     # stylesheets
├── templates/      # HTML templates
├── build.sh        # Render build script
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL (or adjust `DATABASE_URL` to use SQLite locally)

### Installation

```bash
git clone https://github.com/YoanaBast/OCD-Checklist.git
cd OCD-Checklist

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/ocd_checklist
```

### Run Migrations & Start the Server

```bash
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Deployment

The app is configured for [Render](https://render.com/) via `build.sh`, which installs dependencies, collects static files, and runs migrations at deploy time. Gunicorn serves the app in production and WhiteNoise handles static assets.

## Roadmap

See the [`to-do`](https://github.com/YoanaBast/OCD-Checklist/blob/master/to-do) file for planned improvements.

## Contributing

Issues and pull requests are welcome. If you spot a bug or have a feature idea, feel free to open an issue.

