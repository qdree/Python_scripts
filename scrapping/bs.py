import bs4 as bs
import urllib.request

# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce, 'lxml')

# for el in soup.find_all('div', class_ = 'body'):
# 	print (el.text)

source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'xml')

# print (soup)
for block in soup.find_all('url'):
	for url in block.find_all('loc'):
		for date in block.find_all('lastmod'):
			print ("that link {0} was modified {1}".format(url.text, date.text))
