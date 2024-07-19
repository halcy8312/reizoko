def process_message(text, refrigerator_manager, recipe_suggester):
    if text.startswith('追加:'):
        item = text[3:].strip()
        refrigerator_manager.add_item(item)
        return f"{item}を冷蔵庫に追加しました。"
    elif text.startswith('減らす:'):
        item = text[4:].strip()
        refrigerator_manager.remove_item(item)
        return f"{item}を冷蔵庫から減らしました。"
    elif text == '確認':
        return refrigerator_manager.get_contents()
    elif text == 'レシピ':
        return recipe_suggester.suggest_recipe(refrigerator_manager.get_items())
    else:
        return "無効なコマンドです。'追加:', '減らす:', '確認', 'レシピ'のいずれかを使用してください。"