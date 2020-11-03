import pandas as pd
import json
from flask import Response, jsonify
from flask_restful import Resource, reqparse
from sklearn.ensemble import RandomForestClassifier 
from wordcloud import WordCloud
from collections import Counter
import os

def word_cloud(self) : 
# cheese_list = pd.read_csv('cheese_data.csv', encoding ='utf-8') 

    text = ""
    with open("./cheese_data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
                text += line

    font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'

    wc = WordCloud(font_path=font_path, background_color="white", width=1000, height=700)
    wc.generate(text)
    wc.to_file("result.png")
    plt.imshow(wc)
    plt.show

    return wc