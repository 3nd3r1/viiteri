"""viiteri/index.py"""
from viiteri.app import app
from viiteri.routes import index, add, list_references

if __name__ == "__main__":
    app.register_blueprint(index.blueprint)
    app.register_blueprint(add.blueprint)
    app.register_blueprint(list_references.blueprint)
    app.run(port=5001, host="0.0.0.0")
