from django.shortcuts import render

from django.http import HttpResponse

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test
collection = db.documents

def hello(request):
	text = collection.find_one({"id":"hello"})['text']
	return HttpResponse(text)
