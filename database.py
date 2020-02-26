__author__ = "JrReubinJr"

import pymongo

class Database(object):
    path = "C:\Program Files\MongoDB\Server\MongoLogin.txt"
    file = open(path, 'r')
    uri = file.read()
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['blogDB']

    @staticmethod
    def inset(collection, data):
        Database.DATABASE[collection].inset(data)

    @staticmethod
    def find(collection, query): #returns pymongo cursor object
        Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query): #return first element return from cursor (json object)
        Database.DATABASE[collection].find_one(query)