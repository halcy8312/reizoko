from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, FillerComponent

def create_ingredient_list_flex(ingredients):
    contents = [
        TextComponent(text=ingredient, weight="bold", size="sm")
        for ingredient in ingredients
    ]
    
    bubble = BubbleContainer(
        body=BoxComponent(
            layout="vertical",
            contents=[
                TextComponent(text="冷蔵庫の中身", weight="bold", size="xl"),
                BoxComponent(layout="vertical", contents=contents)
            ]
        )
    )
    
    return FlexSendMessage(alt_text="冷蔵庫の中身", contents=bubble)