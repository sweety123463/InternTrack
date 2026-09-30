# InternTrack – Smart Internship & Skill Management Platform

InternTrack is a responsive web application designed to help students discover internship opportunities and manage their applications.

## Features
- Internship listing dashboard
- Search and filter internships
- Internship details: company, location, mode, skills, stipend and deadline
- Demo application workflow
- Add new internship opportunities
- SQLite database
- Responsive Bootstrap UI
- Ready for cloud deployment

## Tech Stack
- Python
- Flask
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Run Locally
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000

## Project Structure
```
InternTrack/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Future Scope
- Student accounts and authentication
- Real application tracking
- Resume upload
- Email notifications
- PostgreSQL cloud database
- Admin analytics
