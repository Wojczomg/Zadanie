import requests
from lxml import html
page = requests.get('https://www.auchandirect.pl/auchan-warszawa/pl/search?text=pepsi+cola&callback=true')
tree = html.fromstring(page.content)






lista = []
lista_img = [

]


for i in range(1,38):
    opis = tree.xpath('//*[@id="search-product-list"]/article[{}]/div/div/a/strong/text()'.format(i))
    cena1 = tree.xpath('//*[@id="search-product-list"]/article[{}]/div/div/aside[2]/p/span[1]/text()'.format(i))
    cena2 = tree.xpath('//*[@id="search-product-list"]/article[{}]/div/div/aside[2]/p/span[2]/text()'.format(i))
    image = tree.xpath('//*[@id="search-product-list"]/article[{}]/div/a/span/div/img'.format(i))
    pak = tree.xpath('//*[@id="search-product-list"]/article[{}]/div/div/p/strong/text()'.format(i))
    cena = round(int(cena1[0]) + (int(cena2[0]) / 100),2)
    b = [opis[0], cena, pak[0]]
    c = [opis[0], cena, pak[0], image]

    lista.append(b)
    lista_img.append(c)




print(lista)
print(len(lista))