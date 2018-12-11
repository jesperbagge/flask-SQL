from flask import Flask

from .settings import Config
from .extensions import db, migrate, login


def create_app(config_class=Config):
    """Main application factory"""

    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_blueprints(app)
    register_shell_context(app)

    return app


def register_extensions(app):
    """Register flask extensions"""

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'user.login'

    return None


def register_blueprints(app):
    """Register Flask blueprints"""

    return None


def register_shell_context(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects"""
        return {
            'db': db
        }

    app.shell_context_processor(shell_context)

