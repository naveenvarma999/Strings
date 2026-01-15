import csv
import io
from datetime import datetime

from flask import Flask, render_template_string, redirect, url_for, request, flash, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-me"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobtracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


# -------------------- MODELS --------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), default="Applied")
    link = db.Column(db.String(300))
    notes = db.Column(db.Text)

    date_applied = db.Column(db.Date, default=datetime.utcnow().date)
    follow_up_date = db.Column(db.Date, nullable=True)          # ✅ NEW
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # ✅ NEW

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -------------------- TEMPLATES (INLINE) --------------------
BASE_HTML = """
<!doctype html>
<html>
<head>
  <title>JobTracker Pro</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container py-4">

  <div class="d-flex justify-content-between align-items-center mb-3">
    <div>
      <h2 class="m-0">JobTracker <span class="text-muted" style="font-size:16px;">Pro</span></h2>
      {% if current_user.is_authenticated %}
        <div class="text-muted" style="font-size: 14px;">Signed in as {{ current_user.email }}</div>
      {% endif %}
    </div>

    {% if current_user.is_authenticated %}
      <div class="d-flex gap-2">
        <a class="btn btn-outline-primary" href="{{ url_for('dashboard') }}">Dashboard</a>
        <a class="btn btn-outline-primary" href="{{ url_for('jobs') }}">Jobs</a>
        <a class="btn btn-outline-danger" href="{{ url_for('logout') }}">Logout</a>
      </div>
    {% endif %}
  </div>

  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <div class="alert alert-info">{{ messages[0] }}</div>
    {% endif %}
  {% endwith %}

  {{ content|safe }}
</body>
</html>
"""

LOGIN_HTML = """
<h3>Login</h3>
<form method="POST" class="mt-3" style="max-width: 450px;">
  <input class="form-control mb-2" name="email" placeholder="Email" required>
  <input class="form-control mb-2" name="password" type="password" placeholder="Password" required>
  <button class="btn btn-primary">Login</button>
  <a href="{{ url_for('register') }}" class="btn btn-link">Register</a>
</form>
"""

REGISTER_HTML = """
<h3>Register</h3>
<form method="POST" class="mt-3" style="max-width: 450px;">
  <input class="form-control mb-2" name="email" placeholder="Email" required>
  <input class="form-control mb-2" name="password" type="password" placeholder="Password" required>
  <button class="btn btn-success">Create account</button>
  <a href="{{ url_for('login') }}" class="btn btn-link">Login</a>
</form>
"""

DASHBOARD_HTML = """
<h3>Dashboard</h3>

<div class="mb-3 d-flex flex-wrap gap-2">
  <a class="btn btn-success" href="{{ url_for('job_new') }}">+ Add Job</a>
  <a class="btn btn-outline-secondary" href="{{ url_for('jobs') }}">View All</a>
  <a class="btn btn-outline-dark" href="{{ url_for('export_csv') }}">Export CSV</a>
</div>

{% if jobs|length == 0 %}
  <div class="alert alert-secondary mt-3">No jobs added yet.</div>
{% else %}
  <div class="row g-3">
    <div class="col-md-6">
      <div class="card p-3">
        <h5 class="mb-2">Status counts</h5>
        <ul class="m-0">
          {% for k,v in stats.items() %}
            <li><b>{{ k }}</b> : {{ v }}</li>
          {% endfor %}
        </ul>
      </div>
    </div>

    <div class="col-md-6">
      <div class="card p-3">
        <h5 class="mb-2">Status chart</h5>
        <canvas id="statusChart"></canvas>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script>
    const labels = {{ stats.keys()|list|tojson }};
    const values = {{ stats.values()|list|tojson }};

    new Chart(document.getElementById("statusChart"), {
      type: "bar",
      data: {
        labels: labels,
        datasets: [{
          label: "Jobs",
          data: values
        }]
      },
      options: {
        responsive: true,
        scales: { y: { beginAtZero: true } }
      }
    });
  </script>
{% endif %}
"""

JOBS_HTML = """
<h3>Jobs</h3>

<form class="row g-2 align-items-end mb-3" method="GET" action="{{ url_for('jobs') }}">
  <div class="col-md-5">
    <label class="form-label">Search (company or role)</label>
    <input class="form-control" name="q" value="{{ request.args.get('q','') }}" placeholder="e.g. Amazon / Data Scientist">
  </div>

  <div class="col-md-3">
    <label class="form-label">Status</label>
    <select class="form-control" name="status">
      <option value="">All</option>
      {% for s in ["Applied","Interview","Offer","Rejected"] %}
        <option value="{{ s }}" {% if request.args.get('status')==s %}selected{% endif %}>{{ s }}</option>
      {% endfor %}
    </select>
  </div>

  <div class="col-md-4 d-flex gap-2">
    <button class="btn btn-primary">Apply</button>
    <a class="btn btn-outline-secondary" href="{{ url_for('jobs') }}">Clear</a>
    <a class="btn btn-success" href="{{ url_for('job_new') }}">+ Add Job</a>
  </div>
</form>

<div class="table-responsive">
<table class="table table-bordered table-hover align-middle">
  <tr>
    <th>Company</th><th>Role</th><th>Status</th><th>Follow-up</th><th>Link</th><th>Actions</th>
  </tr>

  {% for j in jobs %}
  <tr>
    <td><b>{{ j.company }}</b></td>
    <td>{{ j.role }}</td>
    <td>
      {% if j.status == "Applied" %}
        <span class="badge bg-secondary">Applied</span>
      {% elif j.status == "Interview" %}
        <span class="badge bg-primary">Interview</span>
      {% elif j.status == "Offer" %}
        <span class="badge bg-success">Offer</span>
      {% else %}
        <span class="badge bg-danger">Rejected</span>
      {% endif %}
    </td>

    <td>
      {% if j.follow_up_date %}
        {{ j.follow_up_date }}
      {% else %}
        -
      {% endif %}
    </td>

    <td>
      {% if j.link %}
        <a href="{{ j.link }}" target="_blank">Open</a>
      {% else %}
        -
      {% endif %}
    </td>

    <td style="white-space: nowrap;">
      <a class="btn btn-sm btn-warning" href="{{ url_for('job_edit', job_id=j.id) }}">Edit</a>
      <form method="POST" action="{{ url_for('job_delete', job_id=j.id) }}" style="display:inline;">
        <button class="btn btn-sm btn-danger" onclick="return confirm('Delete this job?')">Delete</button>
      </form>
    </td>
  </tr>
  {% endfor %}
</table>
</div>

{% if jobs|length == 0 %}
  <div class="alert alert-secondary">No jobs found for this filter.</div>
{% endif %}
"""

JOB_FORM_HTML = """
<h3>{{ "Edit Job" if job else "Add Job" }}</h3>

<form method="POST" class="mt-3" style="max-width: 700px;">
  <div class="row g-2">
    <div class="col-md-6">
      <label class="form-label">Company</label>
      <input class="form-control" name="company" value="{{ job.company if job else '' }}" required>
    </div>
    <div class="col-md-6">
      <label class="form-label">Role</label>
      <input class="form-control" name="role" value="{{ job.role if job else '' }}" required>
    </div>
  </div>

  <div class="row g-2 mt-2">
    <div class="col-md-6">
      <label class="form-label">Status</label>
      <select class="form-control" name="status">
        {% for s in ["Applied","Interview","Offer","Rejected"] %}
          <option value="{{ s }}" {% if job and job.status == s %}selected{% endif %}>{{ s }}</option>
        {% endfor %}
      </select>
    </div>

    <div class="col-md-6">
      <label class="form-label">Follow-up date</label>
      <input class="form-control" type="date" name="follow_up_date"
             value="{{ job.follow_up_date if job and job.follow_up_date else '' }}">
    </div>
  </div>

  <div class="mt-2">
    <label class="form-label">Job Link</label>
    <input class="form-control" name="link" value="{{ job.link if job else '' }}">
  </div>

  <div class="mt-2">
    <label class="form-label">Notes</label>
    <textarea class="form-control" name="notes" rows="5">{{ job.notes if job else '' }}</textarea>
  </div>

  <div class="mt-3 d-flex gap-2">
    <button class="btn btn-primary">Save</button>
    <a class="btn btn-outline-secondary" href="{{ url_for('jobs') }}">Cancel</a>
  </div>
</form>
"""


def render_page(content_html, **context):
    body = render_template_string(content_html, **context)
    return render_template_string(BASE_HTML, content=body)


# -------------------- ROUTES --------------------
@app.route("/")
def home():
    return redirect(url_for("dashboard"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password required.")
            return redirect(url_for("register"))

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please login.")
            return redirect(url_for("login"))

        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash("Account created. Please login.")
        return redirect(url_for("login"))

    return render_page(REGISTER_HTML)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash("Invalid credentials.")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("dashboard"))

    return render_page(LOGIN_HTML)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    jobs = Job.query.filter_by(user_id=current_user.id).all()
    stats = {}
    for j in jobs:
        stats[j.status] = stats.get(j.status, 0) + 1
    return render_page(DASHBOARD_HTML, jobs=jobs, stats=stats)


@app.route("/jobs")
@login_required
def jobs():
    status = request.args.get("status", "").strip()
    qtext = request.args.get("q", "").strip()

    q = Job.query.filter_by(user_id=current_user.id)

    if status:
        q = q.filter_by(status=status)

    if qtext:
        like = f"%{qtext}%"
        q = q.filter((Job.company.ilike(like)) | (Job.role.ilike(like)))

    jobs_list = q.order_by(Job.id.desc()).all()
    return render_page(JOBS_HTML, jobs=jobs_list)


@app.route("/jobs/new", methods=["GET", "POST"])
@login_required
def job_new():
    if request.method == "POST":
        fup = request.form.get("follow_up_date")
        follow_up_date = datetime.strptime(fup, "%Y-%m-%d").date() if fup else None

        job = Job(
            company=request.form["company"],
            role=request.form["role"],
            status=request.form.get("status", "Applied"),
            follow_up_date=follow_up_date,
            link=request.form.get("link"),
            notes=request.form.get("notes"),
            user_id=current_user.id,
        )
        db.session.add(job)
        db.session.commit()
        flash("Job added.")
        return redirect(url_for("jobs"))

    return render_page(JOB_FORM_HTML, job=None)


@app.route("/jobs/<int:job_id>/edit", methods=["GET", "POST"])
@login_required
def job_edit(job_id):
    job = Job.query.filter_by(id=job_id, user_id=current_user.id).first_or_404()

    if request.method == "POST":
        fup = request.form.get("follow_up_date")
        job.follow_up_date = datetime.strptime(fup, "%Y-%m-%d").date() if fup else None

        job.company = request.form["company"]
        job.role = request.form["role"]
        job.status = request.form.get("status", "Applied")
        job.link = request.form.get("link")
        job.notes = request.form.get("notes")
        db.session.commit()
        flash("Job updated.")
        return redirect(url_for("jobs"))

    return render_page(JOB_FORM_HTML, job=job)


@app.route("/jobs/<int:job_id>/delete", methods=["POST"])
@login_required
def job_delete(job_id):
    job = Job.query.filter_by(id=job_id, user_id=current_user.id).first_or_404()
    db.session.delete(job)
    db.session.commit()
    flash("Job deleted.")
    return redirect(url_for("jobs"))


@app.route("/export.csv")
@login_required
def export_csv():
    jobs = Job.query.filter_by(user_id=current_user.id).order_by(Job.id.desc()).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["company", "role", "status", "date_applied", "follow_up_date", "link", "notes"])

    for j in jobs:
        writer.writerow([
            j.company,
            j.role,
            j.status,
            str(j.date_applied) if j.date_applied else "",
            str(j.follow_up_date) if j.follow_up_date else "",
            j.link or "",
            (j.notes or "").replace("\n", " ")
        ])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=jobs.csv"}
    )


# -------------------- MAIN --------------------
if __name__ == "__main__":
    # NOTE: If you already created jobtracker.db before adding follow_up_date,
    # delete jobtracker.db once, then run again so the new columns are created.
    with app.app_context():
        db.create_all()
    app.run(debug=True)

