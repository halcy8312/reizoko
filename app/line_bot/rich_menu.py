from linebot.models import RichMenu, RichMenuArea, RichMenuSize, MessageAction, RichMenuBounds
from app.config import Config
import os

def create_rich_menu(line_bot_api):
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

    # リッチメニューの画像ファイルのパスを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, '..', '..', 'static', 'rich_menu_image.png')

    # リッチメニューの画像をアップロード
    with open(image_path, "rb") as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", f)

    # デフォルトのリッチメニューとして設定
    line_bot_api.set_default_rich_menu(rich_menu_id)

    return rich_menu_id