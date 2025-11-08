# app/utils.py
import os

def save_uploaded_file(file_storage, upload_folder):
    filename = file_storage.filename
    # intentionally insecure: filename not sanitized (path traversal risk)
    save_path = os.path.join(upload_folder, filename)
    file_storage.save(save_path)
    return save_path
