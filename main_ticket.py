# coding: utf-8
import sys, os
sys.path.append('')
from get_tags_tickets import get_tags
from get_category import get_category
from get_events_tickets import get_events
from get_event_description import get_description



sys.path.append('../')
from tickets.models import Category

if __name__ == '__main__':
    #get_category() # При первом запуске, потом закомментить
    #get_tags()  # При первом запуске, потом закомментить
    get_events()
    get_description()
