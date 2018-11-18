from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import pymongo
from pymongo import MongoClient
import pprint
import json

client = MongoClient('localhost', 27017)
db = client.test
collection = db.documents

def hello(request):
	text = collection.find_one({"id":"hello"})['text']
	return HttpResponse(text)