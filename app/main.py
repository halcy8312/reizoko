from app import create_app, db
from app.line_bot.handler import setup_line_bot
from app.line_bot.rich_menu import create_rich_menu
from linebot import LineBotApi
import logging
import os

app = create_app()
logging.basicConfig(level=logging.INFO)

setup_line_bot(app)
line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
create_rich_menu(line_bot_api)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)