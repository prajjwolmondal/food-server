import os

from dotenv import load_dotenv


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, '.env'))
    SECRET_KEY = os.getenv('APP_SECRET_KEY') or 'you-will-never-guess'
    MONGO_DB_PWD = os.getenv('MONGO_PWD')
    MONGO_DB_NAME = "untitled2"
    MONGO_URI = f"mongodb+srv://prajjwol:{MONGO_DB_PWD}@initcluster-2dabv.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority"