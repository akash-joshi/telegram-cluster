import re
import time
start_time = time.time()

news_array = []

def detect_en_news(article):
  print(article)
  with open(article["path"]) as f:
    if 'news' in f or 'News' in f:
      print('here')
      news_array.append(article)

def detect_news(articles):
  if articles["lang_code"] == "en" :
    list(map(detect_en_news, articles["articles"]))
  return None

def main(articles, mypath):
  list(map(detect_news, articles))
  print(news_array)
  return None