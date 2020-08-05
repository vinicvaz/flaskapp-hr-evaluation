from flask import Flask
from flask_bootstrap import Bootstrap
import joblib as jb



def create_app():
    """Create Flask application."""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('config.py')
    app.config.update(
        SEND_FILE_MAX_AGE_DEFAULT=0,
    )
    global model
    model = jb.load("./app/ml_models/lgbm_reduced.pkl.z")

    Bootstrap(app)


    with app.app_context():
        # Import parts of our application
        from .home import home
        # Register Blueprints
        app.register_blueprint(home.home_bp)

        return app


server = create_app()
