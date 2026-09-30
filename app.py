from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "interntrack-demo-key"
DB = Path("interntrack.db")

def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = db()
    conn.execute("""CREATE TABLE IF NOT EXISTS internships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        location TEXT NOT NULL,
        mode TEXT NOT NULL,
        skills TEXT NOT NULL,
        stipend TEXT NOT NULL,
        deadline TEXT NOT NULL
    )""")
    count = conn.execute("SELECT COUNT(*) FROM internships").fetchone()[0]
    if count == 0:
        demo = [
            ("Python Developer Intern","TechNova Solutions","Pune","Hybrid","Python, Flask, SQL","₹12,000/month","2026-10-20"),
            ("Web Development Intern","WebSphere Labs","Remote","Remote","HTML, CSS, JavaScript","₹10,000/month","2026-10-28"),
            ("Data Analytics Intern","DataBridge","Mumbai","On-site","Python, SQL, Power BI","₹15,000/month","2026-11-05"),
            ("Cloud & DevOps Intern","CloudOrbit","Remote","Remote","Linux, Docker, Git","₹14,000/month","2026-11-12")
        ]
        conn.executemany("""INSERT INTO internships
        (title,company,location,mode,skills,stipend,deadline) VALUES (?,?,?,?,?,?,?)""", demo)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = db()
    internships = conn.execute("SELECT * FROM internships ORDER BY id DESC").fetchall()
    total = conn.execute("SELECT COUNT(*) FROM internships").fetchone()[0]
    conn.close()
    return render_template("index.html", internships=internships, total=total)

@app.route("/add", methods=["POST"])
def add():
    data = [request.form.get(k,"").strip() for k in
            ["title","company","location","mode","skills","stipend","deadline"]]
    if not all(data):
        flash("Please fill all fields.")
        return redirect(url_for("home"))
    conn = db()
    conn.execute("""INSERT INTO internships
        (title,company,location,mode,skills,stipend,deadline)
        VALUES (?,?,?,?,?,?,?)""", data)
    conn.commit()
    conn.close()
    flash("Internship added successfully!")
    return redirect(url_for("home"))

@app.route("/apply/<int:internship_id>", methods=["POST"])
def apply(internship_id):
    conn = db()
    row = conn.execute("SELECT title FROM internships WHERE id=?", (internship_id,)).fetchone()
    conn.close()
    if row:
        flash(f"Application recorded for {row['title']} (demo mode).")
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
