from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager

login_manager = LoginManager()

login_manager.login_view = "users.sign_in"

@login_manager.user_loader
def load_user(user_id):
    from users.models import User
    return User.query.get(str(user_id))

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)