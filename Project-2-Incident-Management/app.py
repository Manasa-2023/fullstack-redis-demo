from flask import Flask, render_template, request, redirect
import sqlite3
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Email (use Gmail account + app password)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "manasanb2001@gmail.com"
app.config['MAIL_PASSWORD'] = "kxjo xmci size ydlx"
app.config['MAIL_DEFAULT_SENDER'] = "manasanb2001@gmail.com"

mail = Mail(app)

# DB setup
def init_db():
    conn = sqlite3.connect("incidents.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS incidents
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  description TEXT,
                  status TEXT)''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect("incidents.db")
    c = conn.cursor()
    c.execute("SELECT * FROM incidents")
    incidents = c.fetchall()
    conn.close()
    return render_template("index.html", incidents=incidents)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    desc = request.form["description"]

    conn = sqlite3.connect("incidents.db")
    c = conn.cursor()
    c.execute("INSERT INTO incidents (title, description, status) VALUES (?, ?, ?)",
              (title, desc, "Open"))
    conn.commit()
    conn.close()

    # Email notification
    msg = Message("New Incident Logged",
                  recipients=["manasanb2001@gmail.com"])
    msg.body = f"Incident reported:\nTitle: {title}\nDescription: {desc}\nStatus: Open"
    mail.send(msg)

    return redirect("/")

@app.route("/resolve/<int:id>")
def resolve(id):
    conn = sqlite3.connect("incidents.db")
    c = conn.cursor()
    c.execute("UPDATE incidents SET status = 'Resolved' WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    # Email notification
    msg = Message("Incident Resolved",
                  recipients=["manasanb2001@gmail.com"])
    msg.body = f"Incident ID {id} has been resolved ✅"
    mail.send(msg)

    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
