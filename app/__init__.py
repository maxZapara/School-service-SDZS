from flask import Flask


def create_app():
    from .extensions import db
    app = Flask(__name__, static_url_path='/static')

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    from core import main_blp
    app.register_blueprint(main_blp)

    from subjects import subjects_blp
    app.register_blueprint(subjects_blp)

    from users import user_blp
    app.register_blueprint(user_blp)
    
    with app.app_context():
        db.create_all()

    return app