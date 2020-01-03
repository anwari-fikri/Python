import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# Opening up connection, grabbing page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# print (page.read ())
soup = BeautifulSoup(page_html, 'html.parser')

# Grab each mango img
containers = soup.find_all("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name\n"

f.write(headers)

for container in containers:
	brand_container = container.findAll("a", {"class":"item-brand"})
	brand_name = brand_container[0].img["title"]

	product_container = container.findAll("a", {"class":"item-title"})
	product_name = product_container[0].text
	product_name = product_name.replace(",","|")

	f.write(f"{brand_name},{product_name},\n")

f.close()