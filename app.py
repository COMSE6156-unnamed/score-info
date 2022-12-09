from flask import Flask, render_template
from flask_migrate import Migrate
import config
from utils.exts import db
from blueprints import score_bp, user_bp
from flask_cors import CORS

# app config
app = Flask(__name__)
app.config.from_object(config)
CORS(app)

# DB config
db.init_app(app)  # Init DB
migrate = Migrate(app, db)  # DB Version Control

# Blueprints
app.register_blueprint(score_bp)
app.register_blueprint(user_bp)


@app.route("/")
def index():
    return "Score System"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5011)
