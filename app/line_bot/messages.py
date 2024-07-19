from linebot.models import QuickReply, QuickReplyButton, MessageAction

def get_quick_reply():
    return QuickReply(items=[
        QuickReplyButton(action=MessageAction(label="食材追加", text="食材追加")),
        QuickReplyButton(action=MessageAction(label="食材削除", text="食材削除")),
        QuickReplyButton(action=MessageAction(label="冷蔵庫確認", text="冷蔵庫確認")),
        QuickReplyButton(action=MessageAction(label="レシピ提案", text="レシピ提案"))
    ])

def process_message(text, refrigerator_manager, recipe_suggester):
    if text.startswith('追加:'):
        item = text[3:].strip()
        refrigerator_manager.add_item(item)
        return f"{item}を冷蔵庫に追加しました。"
    elif text.startswith('削除:'):
        item = text[3:].strip()
        refrigerator_manager.remove_item(item)
        return f"{item}を冷蔵庫から削除しました。"
    elif text == '冷蔵庫確認':
        contents = refrigerator_manager.get_contents()
        if contents:
            return "冷蔵庫の中身:\n" + "\n".join(contents)
        else:
            return "冷蔵庫は空です。"
    elif text == 'レシピ提案':
        ingredients = refrigerator_manager.get_items()
        if ingredients:
            recipe = recipe_suggester.suggest_recipe(ingredients)
            return f"提案レシピ:\n{recipe}"
        else:
            return "冷蔵庫が空なので、レシピを提案できません。"
    elif text == '食材追加':
        return "追加する食材名を教えてください。\n例: 追加:りんご"
    elif text == '食材削除':
        return "削除する食材名を教えてください。\n例: 削除:りんご"
    else:
        return "コマンドが認識できません。\n'食材追加'、'食材削除'、'冷蔵庫確認'、'レシピ提案' のいずれかを選択するか、\n'追加:食材名' または '削除:食材名' の形式で入力してください。"