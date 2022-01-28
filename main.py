import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(r"C:/Users/Aditya Chugh/Desktop/becode/chromedriver.exe")

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
	driver.get(link)
	soup = BeautifulSoup(driver.page_source, "lxml")
	#price
	for div_containing_price in soup.find_all("p", {"class":"classified__price"}):
		buffer = div_containing_price.find("span", {"class":"sr-only"})
	if buffer != None:
		price.append((buffer.text))
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

	url = f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={i}&orderBy=relevance"
	print("\n", url, "\n")
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, "lxml")

	for link in soup.find_all("a", {"class":"card__title-link"}):
		print(link["href"])
		get_data_from_link(link["href"])

