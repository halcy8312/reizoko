from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.line_bot.handler import setup_line_bot
from app.refrigerator.manager import RefrigeratorManager
from app.recipe.suggester import RecipeSuggester
from app.line_bot.rich_menu import create_rich_menu
from linebot import LineBotApi

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])

    refrigerator_manager = RefrigeratorManager(db)
    recipe_suggester = RecipeSuggester(app.config['OPENAI_API_KEY'])

    setup_line_bot(app, line_bot_api, refrigerator_manager, recipe_suggester)
    create_rich_menu(line_bot_api)

    return app