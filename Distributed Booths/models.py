from mongoengine import *

class Number(Document):
    number = IntField(required = False)
