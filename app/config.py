import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
    LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    @classmethod
    def get_required_env(cls, name):
        value = os.environ.get(name)
        if not value:
            raise ValueError(f"必要な環境変数 {name} が設定されていません。")
        return value