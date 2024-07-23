import logging
from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)
from app.line_bot.messages import process_message, get_quick_reply

def setup_line_bot(app, line_bot_api, handler, refrigerator_manager, recipe_suggester):
    @app.route("/callback", methods=['POST'])
    def callback():
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        logging.info(f"Request body: {body}")
        logging.info(f"Signature: {signature}")
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            logging.error("Invalid signature. Check your channel access token/channel secret.")
            abort(400)
        return 'OK'

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        reply_text = process_message(event.message.text, refrigerator_manager, recipe_suggester)
        quick_reply = get_quick_reply()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text, quick_reply=quick_reply)
        )