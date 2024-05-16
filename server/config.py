import datetime
import os

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=10)

JWT_TOKEN_LOCATION = ['cookies']

JWT_COOKIE_SAMESITE = 'Strict'

JWT_COOKIE_SECURE = os.getenv('JWT_COOKIE_SECURE')