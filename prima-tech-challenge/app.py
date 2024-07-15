from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from user_management.user_routes import user_blueprint

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Access API"}
)

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix="/")
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)
