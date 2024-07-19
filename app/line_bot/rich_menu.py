import json
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

    try:
        rich_menu_json = json.dumps(rich_menu.as_json_dict())
        print(f"Sending rich menu: {rich_menu_json}")
        rich_menu_id = line_bot_api.create_rich_menu(rich_menu)
        print(f"Created rich menu with id: {rich_menu_id}")
    except Exception as e:
        print(f"Error creating rich menu: {str(e)}")
        return None

    # リッチメニューの画像ファイルのパスを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, '..', '..', 'static', 'rich_menu_image.png')
    print(f"Image path: {image_path}")

    # 画像ファイルが存在するか確認
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return None

    # リッチメニューの画像をアップロード
    try:
        with open(image_path, "rb") as f:
            line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", f)
        print("Uploaded rich menu image successfully")
    except Exception as e:
        print(f"Error uploading rich menu image: {str(e)}")
        return None

    # デフォルトのリッチメニューとして設定
    try:
        line_bot_api.set_default_rich_menu(rich_menu_id)
        print("Set as default rich menu successfully")
    except Exception as e:
        print(f"Error setting default rich menu: {str(e)}")
        return None

    return rich_menu_id