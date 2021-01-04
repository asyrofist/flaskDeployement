import os # import library os

class Config: # membuat fungsi class config
    SECRET_KEY = os.environ.get('SECRET_KEY') # inisialisasi secret key
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') # inisialisasi sqlalchemy
    MAIL_SERVER = 'smtp.googlemail.com' # inisialisasi email
    MAIL_PORT = 587 # inisialisasi port
    MAIL_USE_TLS = True # inislaisasi tls degan boolean true
    MAIL_USERNAME = os.environ.get('EMAIL_USER') # inisialisasi username dengan email
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS') # inisiaiisasi passowrd
