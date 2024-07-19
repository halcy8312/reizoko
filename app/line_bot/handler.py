from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from app.line_bot.messages import process_message

def setup_line_bot(app, refrigerator_manager, recipe_suggester):
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
    handler = WebhookHandler(app.config['LINE_CHANNEL_SECRET'])

    @app.route("/callback", methods=['POST'])
    def callback():
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return 'OK'

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        reply_text = process_message(event.message.text, refrigerator_manager, recipe_suggester)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))