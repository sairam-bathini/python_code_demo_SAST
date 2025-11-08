# app/app.py
from flask import Flask, request, render_template, send_from_directory
from .models import query_user_by_username, add_log
from .auth import check_credentials
from .utils import save_uploaded_file
from .unsafe_deserialize import unsafe_load_if_pickle
import os, subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), '..', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    # reflected XSS demo (value echoed into template)
    name = request.args.get('name', 'Guest')
    add_log(f"Visited index with name={name}")
    return render_template('index.html', name=name)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if check_credentials(username, password):
            return f"Welcome {username}!"
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        if not f:
            return 'No file', 400
        saved_path = save_uploaded_file(f, app.config['UPLOAD_FOLDER'])
        # insecure deserialization demo
        result = unsafe_load_if_pickle(saved_path)
        return render_template('upload_result.html', path=saved_path, result=result)
    return '''<form method="post" enctype="multipart/form-data">
<input type=file name=file>
<input type=submit>
</form>'''

@app.route('/run_cmd')
def run_cmd():
    # command injection demo: unsanitized shell=True
    cmd = request.args.get('cmd', 'echo hello')
    add_log(f"Running command: {cmd}")
    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    return f"Command output:\n<pre>{output}</pre>"

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    # intentionally insecure: possible path traversal if filename not sanitized
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=False)
