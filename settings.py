# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("CONSUMER_KEY")
CS = os.environ.get("CONSUMER_SECRET")
AK = os.environ.get("ACCESS_KEY")
AS = os.environ.get("ACCESS_SECRET")

