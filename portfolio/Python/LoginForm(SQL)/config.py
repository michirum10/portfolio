# config.py

# SECRET_KEY
class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# テスト用
# SQLデータベースに
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'

# 本番用
# class ProductionConfig(Config):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'