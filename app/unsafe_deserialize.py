# app/unsafe_deserialize.py
import pickle

def unsafe_load_if_pickle(path):
    try:
        with open(path, 'rb') as f:
            data = f.read()
            # naive check for pickle data (intentional)
            if data.startswith(b'\x80'):
                obj = pickle.loads(data)  # insecure deserialization
                return f"Unpickled object of type {type(obj)}"
            else:
                return 'Not a pickle'
    except Exception as e:
        return f"Error loading: {e}"
