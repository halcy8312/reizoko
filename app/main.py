from app import create_app, db
from app.line_bot.handler import setup_line_bot
from app.refrigerator.manager import RefrigeratorManager
from app.recipe.suggester import RecipeSuggester
from app.line_bot.rich_menu import create_rich_menu
from linebot import LineBotApi, WebhookHandler
import logging

app = create_app()
logging.basicConfig(level=logging.INFO)

line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(app.config['LINE_CHANNEL_SECRET'])

refrigerator_manager = RefrigeratorManager(db)
recipe_suggester = RecipeSuggester(app.config['OPENAI_API_KEY'])

setup_line_bot(app, line_bot_api, handler, refrigerator_manager, recipe_suggester)
create_rich_menu(line_bot_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)