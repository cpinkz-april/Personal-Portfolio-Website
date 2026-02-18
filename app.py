from flask import Flask, render_template, request, jsonify
from datetime import datetime
import sqlite3, os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

DB_PATH = os.path.join(os.path.dirname(__file__), 'portfolio.db')

# ──────────────────────────────────────────────
# Database helpers (stdlib sqlite3)
# ──────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contact_message (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                name      TEXT    NOT NULL,
                email     TEXT    NOT NULL,
                subject   TEXT    NOT NULL,
                message   TEXT    NOT NULL,
                timestamp TEXT    NOT NULL
            )
        """)
        conn.commit()

init_db()

# ──────────────────────────────────────────────
# Portfolio Data (edit this to customise)
# ──────────────────────────────────────────────

PORTFOLIO_DATA = {
    "name": "Aethaya Meesawat",
    "title": "Master student & Freelancer",
    "bio": (
        "..."
    ),
    "skills": [
        {"category": "Remote Sensing & GIS", "tools": ["Google Earth Engine", "Sentinel-2"]},
        {"category": "Programming", "tools": ["Python", "JavaScript"]},
        {"category": "Marine Science", "tools": ["Seagrass Ecology", "Field Surveys"]},
    ],
    "projects": [
        {
            "title": "Automated News Dashboard",
            "description": (
                "..."
            ),
            "tags": ["Python", "Streamlit"],
            "link": "https://github.com/",
            "icon": "📰",
        },
        {
            "title": "NDVI Change Detection – GEE",
            "description": (
                "Google Earth Engine workflow for NDVI-based land-cover change "
                "detection and seagrass health monitoring at Koh Libong, Trang."
            ),
            "tags": ["GEE", "JavaScript", "NDVI", "Change Detection"],
            "link": "https://github.com/",
            "icon": "🛰️",
        },
    ],
    "education": [
        {
            "degree": "...",
            "school": "...",
            "year": "...",
            "detail": "...",
        }
    ],
    "socials": {
        "github": "...",
        "linkedin": "https://www.linkedin.com/in/aethaya-meesawat/",
        "email": "c.aethaya20@gmail.com",
    },
}

# ──────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)


@app.route('/api/contact', methods=['POST'])
def contact():
    """Receive contact form submissions and store them in SQLite."""
    payload = request.get_json()

    # Basic validation
    required = ['name', 'email', 'subject', 'message']
    for field in required:
        if not payload.get(field, '').strip():
            return jsonify({'success': False, 'error': f'Field "{field}" is required.'}), 400

    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    with get_db() as conn:
        conn.execute(
            "INSERT INTO contact_message (name, email, subject, message, timestamp) VALUES (?,?,?,?,?)",
            (payload['name'].strip(), payload['email'].strip(),
             payload['subject'].strip(), payload['message'].strip(), ts)
        )
        conn.commit()

    return jsonify({'success': True, 'message': 'Your message has been received. Thank you!'})


@app.route('/admin/messages')
def admin_messages():
    """Simple admin view to read all contact messages."""
    with get_db() as conn:
        msgs = conn.execute(
            "SELECT * FROM contact_message ORDER BY timestamp DESC"
        ).fetchall()
    return render_template('admin.html', messages=msgs)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
