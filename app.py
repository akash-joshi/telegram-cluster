import lang
import news

mypath = "./00-full"

# lang.print_main(mypath)
langs = lang.main(mypath)
# print(langs)
news.main(langs, mypath)