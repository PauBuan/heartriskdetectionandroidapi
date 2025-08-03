from flask import Flask
from flask_cors import CORS
from Controller.auth_controller import auth_bp
from Controller.prediction_controller import prediction_bp
from Controller.record_controller import record_bp
from Controller.android_api_controller import api_bp
from config.database import DatabaseConfig

app = Flask(__name__)
app.secret_key = DatabaseConfig.SECRET_KEY

# Enable CORS for Android app requests
CORS(app, resources={r"/api/android/*": {"origins": "*"}})

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(prediction_bp)
app.register_blueprint(record_bp)
app.register_blueprint(api_bp, url_prefix='/api/android')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)