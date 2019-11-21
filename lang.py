import time
start_time = time.time()

from os import listdir
from os.path import isfile, join
import pathlib
from bs4 import BeautifulSoup

mypath = "./00"
dirs = listdir(mypath)

def path_relative(f):
  return_dict = {}
  return_dict["fname"] = f
  return_dict["path"] = mypath + "/" + f
  return return_dict

def get_title(file):
  with open(file["path"]) as fp:
    soup = BeautifulSoup(fp, "html.parser")
    title = soup.find("meta",  property="og:title")
    return_dict = {}
    return_dict["title"] = title["content"] if title else "No meta title given"
    return_dict["fname"] = file["fname"]
    return_dict["path"] = file["path"]
    return return_dict

joined_dirs = map(path_relative, dirs)
# print(joined_dirs)

print(list(map(get_title, joined_dirs)))

print("--- %s seconds ---" % (time.time() - start_time))