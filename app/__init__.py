from flask import Flask


def create_app():
    from core import main_blp
    from subjects import subjects_blp
    from .extensions import db
    app = Flask(__name__, static_url_path='/static')

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    app.register_blueprint(main_blp)
    app.register_blueprint(subjects_blp)

    return app