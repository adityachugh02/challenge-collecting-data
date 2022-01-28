import requests
from bs4 import BeautifulSoup

locality = []
proprety_type = []
proprety_subtype = []
price = []
sale_type = []
rooms = []
area = []
equipped_kitchen = []
furnished = []
open_fire = []
terrace = []
terrace_area = []
garden = []
garden_area = []
surface = []
surface_plot = []
facades  = []
swimming_pool = []
state = []

def get_data_from_link(link):
	r = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
	soup = BeautifulSoup(r.content, "lxml")
	#price
	buffer = soup.find("span", {"class":"d-block price-label"})
	if buffer != None:
		price.append((buffer.text).replace("\u202f", ""))
		print(price[-1])
	else:
		price.append(None)
		print(price[-1])
	#locality
	buffer = soup.find("span", {"class":"city-line pl-1"})
	if buffer != None:
		locality.append(buffer.text)
		print(locality[-1])
	else:
		locality.append(None)
		print(locality[-1])
	#proprety type
	#proprety_subtype
	#sale_type 
	#rooms
	#area
	#equipped_kitchen
	#furnished
	#open_fire
	#terrace
	#terrace_area
	#garden
	#garden_area
	#surface
	#surface_plot
	#facades
	#swimming_pool
	#state






for i in range(3):

	url = f"https://immo.vlan.be/en/real-estate?transactiontypes=for-sale,in-public-sale&noindex=1&page={i}"
	r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	print(url, r.status_code, "\n")
	soup = BeautifulSoup(r.content, "lxml")

	for div_containing_link in soup.find_all("div", {"class":"long-and-truncated"}):
		for div in div_containing_link:
		    link = div.find('a')
		    print(link['href'])
		    get_data_from_link(link['href'])

print(price)
print(locality)

