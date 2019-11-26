from whatthelang import WhatTheLang
from bs4 import BeautifulSoup
from os import listdir
import time
start_time = time.time()


wtl = WhatTheLang()

en_array = []
ru_array = []


def print_main(mypath):
    def get_title(file):
        path = mypath + "/" + file
        with open(path) as fp:
            soup = BeautifulSoup(fp, "lxml")
            title = soup.find("meta",  property="og:title")
            lang = wtl.predict_lang(title["content"])
            if lang == "ru":
                ru_array.append(file)
            if lang == "en":
                en_array.append(file)

    dirs = listdir(mypath)

    list(map(get_title, dirs))
    return_list = []

    en_return = {}
    en_return["lang_code"] = "en"
    en_return["articles"] = en_array
    return_list.append(en_return)

    ru_return = {}
    ru_return["lang_code"] = "ru"
    ru_return["articles"] = ru_array
    return_list.append(ru_return)

    print(return_list)
    print("--- %s seconds ---" % (time.time() - start_time))


def main(mypath):
    def get_title(file):
        path = mypath + "/" + file
        with open(path) as fp:
            soup = BeautifulSoup(fp, "lxml")
            title = soup.find("meta",  property="og:title")
            lang = wtl.predict_lang(title["content"])
            if lang == "ru":
                more_data = {}
                more_data["file"] = file
                more_data["path"] = path
                ru_array.append(more_data)
            if lang == "en":
                more_data = {}
                more_data["file"] = file
                more_data["path"] = path
                en_array.append(more_data)

    dirs = listdir(mypath)

    list(map(get_title, dirs))
    return_list = []

    en_return = {}
    en_return["lang_code"] = "en"
    en_return["articles"] = en_array
    return_list.append(en_return)

    ru_return = {}
    ru_return["lang_code"] = "ru"
    ru_return["articles"] = ru_array
    return_list.append(ru_return)
    print("--- %s seconds ---" % (time.time() - start_time))

    return return_list
