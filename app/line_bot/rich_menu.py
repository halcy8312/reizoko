from linebot import LineBotApi
from linebot.models import RichMenu, RichMenuArea, RichMenuSize, MessageAction
from app.config import Config

line_bot_api = LineBotApi(Config.LINE_CHANNEL_ACCESS_TOKEN)

def create_rich_menu():
    rich_menu = RichMenu(
        size=RichMenuSize(width=2500, height=1686),
        selected=True,
        name="冷蔵庫ボットメニュー",
        chat_bar_text="メニューを開く",
        areas=[
            RichMenuArea(
                bounds=RichMenuBounds(x=0, y=0, width=1250, height=843),
                action=MessageAction(label="食材追加", text="食材追加")
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=1251, y=0, width=1250, height=843),
                action=MessageAction(label="食材削除", text="食材削除")
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=0, y=844, width=1250, height=843),
                action=MessageAction(label="冷蔵庫確認", text="冷蔵庫確認")
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=1251, y=844, width=1250, height=843),
                action=MessageAction(label="レシピ提案", text="レシピ提案")
            )
        ]
    )

    rich_menu_id = line_bot_api.create_rich_menu(rich_menu)
    with open("path_to_your_rich_menu_image.png", "rb") as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", f)
    line_bot_api.set_default_rich_menu(rich_menu_id)