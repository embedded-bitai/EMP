from com_cheese_api.ext.db import url, db, openSession, engine
from com_cheese_api.util.file import FileReader
from flask import request
from sqlalchemy import func
from sqlalchemy import and_, or_
from flask import Response, jsonify
from flask_restful import Resource, reqparse
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
import json
import os
import sys
from typing import List
from pathlib import Path

#import csv, time
# from selenium import webdriver
# from wordcloud import WordCloud
# from collections import Counter

# class CheeseKdd(object):

#     def __init__(self):
        
#     def cheese_Crawling(html):
#         item_list = []
#         item_dict = {}
#         items = driver.find_elements_by_class_name('item')
#         itemNum = 1
#         for item in items:
#             itemNum += 1
#             title = item.find_element_by_class_name('name').text
#             price = item.find_element_by_class_name('price').text
#             info = item.find_element_by_class_name('desc').text
#             src = item.find_element_by_css_selector('a.img>img').get_attribute('src')
#             item_list.append([title, price, info, src])
#             item_dict[str(itemNum)] = {'title':title, 'price':price, 'info':info, 'img':src}
#         return item_list, item_dict

#     def toCSV(cheese_list):
#         file = open('cheese_kurly.csv', 'w', encoding='utf-8', newline='')
#         csvfile = csv.writer(file)
#         for row in cheese_list :
#             csvfile.writerow(row)
#         file.close()
#         cheese_list = []
#         cheese_dict = {}
#         url = "https://www.kurly.com/shop/goods/goods_search.php?searched=Y&log=1&skey=all&hid_pr_text=&hid_link_url=&edit=Y&sword=%C4%A1%C1%EE&x=0&y=0"
#         driver = webdriver.Chrome("./ChromeDriver/")
#         driver.implicitly_wait(5)
#         driver.get(url)
#         pages = driver.find_elements_by_class_name('layout-pagination-number')
#         body = driver.find_element_by_css_selector('body')
#         for page in pages:
#             page.click()
#             #print('-------------------------')
#             #print('page', pagenum)
#             #print('-------------------------')
#             #pagenum += 1
#             time.sleep(3)
#             items = driver.find_elements_by_class_name('item')
#             cheese_item = cheese_Crawling(items)
#             cheese_list += cheese_item[0]
#             cheese_dict = dict(cheese_dict, **cheese_item[1])
#         # 리스트 출력
#         for item in cheese_list :
#             print(item)
#         # 사전형 출력
#         for item in cheese_dict :
#             print(item, cheese_dict[item]['img'], cheese_dict[item]['title'], cheese_dict[item]['price'], cheese_dict[item]['info'])
#         # CSV파일 생성
#         toCSV(cheese_list)
#         driver.quit()