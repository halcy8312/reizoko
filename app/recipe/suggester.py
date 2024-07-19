import openai

class RecipeSuggester:
    def __init__(self, api_key):
        openai.api_key = api_key

    def suggest_recipe(self, ingredients):
        if not ingredients:
            return "冷蔵庫が空なので、レシピを提案できません。"
        
        ingredients_str = ", ".join(ingredients)
        prompt = f"冷蔵庫に{ingredients_str}があります。これらの材料を使った簡単なレシピを1つ提案してください。レシピ名と簡単な作り方を含めてください。"
        
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは料理の専門家です。与えられた材料を使って、簡単で美味しいレシピを提案してください。"},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content