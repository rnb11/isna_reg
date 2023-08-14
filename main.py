from utils.URLHandler import URLHandler

urlHandler = URLHandler(True)
url = urlHandler.get_url()
print(url)
url = urlHandler.get_url_for_esb(True)
print(url)
url = urlHandler.get_url_for_authorization()
print(url)