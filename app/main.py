from flask import Flask
from app.config import Config
from app.line_bot.handler import setup_line_bot
from app.refrigerator.manager import RefrigeratorManager
from app.recipe.suggester import RecipeSuggester

def create_app():
    app = Flask(__name__)
    
    # 必要な環境変数を取得
    app.config['LINE_CHANNEL_ACCESS_TOKEN'] = Config.get_required_env('LINE_CHANNEL_ACCESS_TOKEN')
    app.config['LINE_CHANNEL_SECRET'] = Config.get_required_env('LINE_CHANNEL_SECRET')
    app.config['OPENAI_API_KEY'] = Config.get_required_env('OPENAI_API_KEY')

    refrigerator_manager = RefrigeratorManager()
    recipe_suggester = RecipeSuggester(app.config['OPENAI_API_KEY'])

    setup_line_bot(app, refrigerator_manager, recipe_suggester)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)