# coding: utf-8
import json
import urllib
import sys, os
import traceback
import time
sys.path[0] = '../'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_globalhome'
from tickets.models import Category, SubEvent, Event, Venue, Get_SubEvent, Tags # Sectors, 
session = 'globalhome353216' # Дается к API

all_categories = Category.objects.all()

def get_tags():
    all = Tags(id = 5) 
    all.alias = "all"
    all.title = u"Все события"
    all.category_id = 1
    all.save()

    for cat in all_categories:
        category = cat.id
        #category = 454827
        tags = urllib.urlopen('http://api.cultserv.ru/jtransport/partner/get_tags?category_id=%s&session=%s'%(category, session)).read()
        data_tags = json.loads(tags)
        time.sleep(1)
        #print data_tags['message']
        for dict in data_tags['message']:
            dict = dict
            try:
                tag = Tags.objects.get(id = dict['id'])
            except Tags.DoesNotExist:
                tag = Tags(id = dict['id'])
            tag.title = dict['title']
            tag.category_id = category
            try:
                tag.title_eng = dict['title_eng']
            except:
                print u"Нет title_eng"
            tag.alias = dict['alias']
            tag.count = dict['count']
            tag.show = dict['show']
            tag.save()
            #print dict['id']
            #print dict['title']
    
