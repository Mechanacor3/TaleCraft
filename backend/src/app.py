from flask import Flask
from routes.story_routes import story_bp
from routes.image_routes import image_bp
from routes.script_routes import script_bp
from routes.tts_routes import tts_bp
from routes.video_routes import video_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints for different routes
    app.register_blueprint(story_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(script_bp)
    app.register_blueprint(tts_bp)
    app.register_blueprint(video_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)