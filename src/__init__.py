from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate

from .config import config
from .utils import db
from .resources.Book import BookResource, BookId

# swagger congfigs
SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "Library API"
    }
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(config.DevConfig)

    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    api = Api(app)

    api.add_resource(BookResource, "/books")
    api.add_resource(BookId, "/books/id/<int:id>")

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    with app.app_context():
        db.create_all()

    from .views import session_views
    app.register_blueprint(session_views.session_bp)

    return app