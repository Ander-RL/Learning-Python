import urllib.request, urllib.parse, urllib.error
import json

response = urllib.parse.urlparse('https://linuxhint.com/use_urllib_python/')
print('RESPONSE:', response)
print('URL     :', response.geturl())

# Algunas webs detectan urllib como un webcrawler y lo bloquean
try:
    handler = urllib.request.urlopen("https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping")
    for line in handler:
        print(line.decode().strip())
except Exception as e:
    print(e)

# BeautifulSoup se usa para leer webs de forma más cómoda. Web crawlers.