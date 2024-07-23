from app.main import create_app
from app.line_bot.handler import setup_line_bot
import logging

app = create_app()
logging.basicConfig(level=logging.INFO)

line_bot_api, handler = setup_line_bot(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)