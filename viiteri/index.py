"""viiteri/index.py"""
from viiteri.app import app

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")
