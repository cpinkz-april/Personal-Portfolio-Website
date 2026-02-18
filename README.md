# Personal Portfolio Website
A full-stack portfolio site built with Flask (Python) on the backend and a custom ocean-themed HTML/CSS/JS frontend.
## Project Structure
portfolio/
├── app.py               ← Flask app, routes, SQLAlchemy model
├── requirements.txt     ← Python dependencies
├── templates/
│   ├── index.html       ← Main portfolio page
│   └── admin.html       ← Admin page to view contact messages
└── static/              ← (add images, extra CSS/JS here)
## Quick Start
### 1. Create & activate a virtual environment
python -m venv venv<br>
source venv/bin/activate      # Windows: venv\Scripts\activate
### 2. Install dependencies
pip install -r requirements.txt
### 3. Run the development server
python app.py<br><br>
Open http://127.0.0.1:5000 in your browser.
## Features
✅ Animated ocean-themed hero with floating particles<br>
✅ Scroll-reveal animations<br>
✅ Responsive layout (mobile-friendly)<br>
✅ Contact form → stores messages in SQLite<br>
✅ Admin dashboard to view messages<br>
✅ Custom cursor with hover effects<br>
✅ Zero external CSS frameworks (fully custom)
