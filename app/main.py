from flask import Flask
from app.config import Config
from app.line_bot.handler import setup_line_bot
from app.refrigerator.manager import RefrigeratorManager
from app.recipe.suggester import RecipeSuggester
from app.line_bot.rich_menu import create_rich_menu
from linebot import LineBotApi

def create_app():
    app = Flask(__name__)
    
    # 必要な環境変数を取得
    app.config['LINE_CHANNEL_ACCESS_TOKEN'] = Config.get_required_env('LINE_CHANNEL_ACCESS_TOKEN')
    app.config['LINE_CHANNEL_SECRET'] = Config.get_required_env('LINE_CHANNEL_SECRET')
    app.config['OPENAI_API_KEY'] = Config.get_required_env('OPENAI_API_KEY')

    # LineBotApiのインスタンスを作成
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])

    refrigerator_manager = RefrigeratorManager()
    recipe_suggester = RecipeSuggester(app.config['OPENAI_API_KEY'])

    setup_line_bot(app, line_bot_api, refrigerator_manager, recipe_suggester)
    
    # リッチメニューの作成と設定
    create_rich_menu(line_bot_api)

    return app