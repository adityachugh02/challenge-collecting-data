import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd

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
		buffer = (re.findall('^[^\d]*(\d+)', buffer.text))
	if buffer != None:
		price.append(buffer[0])
		print("Price (take cheapest option): ", price[-1])
	else:
		price.append(None)
		print("Price (take cheapest option): ", price[-1])

	#locality
	try:
		buffer = soup.find_all("span", {"class":"classified__information--address-row"})[1]
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', buffer.text).split())
		locality.append(buffer)
		print("Locality: ", locality[-1])
	except:
		buffer = soup.find_all("span", {"class":"classified__information--address-row"})[0]
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', buffer.text).split())
		locality.append(buffer)
		print("Locality: ", locality[-1])

	#proprety type & proprety_subtype
	try:
		buffer = soup.find("h1", {"class":"classified__title"})
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', buffer.text).split())
		proprety_type.append(buffer.replace(" for sale", ""))
		print("Proprety type: ", proprety_type[-1])
	except:
		proprety_type.append(None)
		print("Proprety type: ", proprety_type[-1])

	#sale_type 

	#rooms
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	str_match = [s.text for s in buffer if "Bedrooms" in s.text]
	if str_match:
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', str_match[0]).split())
		rooms.append(buffer.replace("Bedrooms ", ""))
		print("Bedrooms: ", rooms[-1])
	else: 
		rooms.append(None)
		print("Bedrooms: ", rooms[-1])

	#area
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	str_match = [s.text for s in buffer if "Living area" in s.text]
	if str_match:
		buffer = " ".join(re.sub(r'[^0-9]+', '', str_match[0]).split())
		area.append(buffer.replace("Living area ", ""))
		print("Area: ", area[-1])
	else: 
		area.append(None)
		print("Area: ", area[-1])	

	#equipped_kitchen
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	str_match = [s.text for s in buffer if "Kitchen type" in s.text]
	if str_match:
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', str_match[0]).split())
		equipped_kitchen.append(buffer.replace("Kitchen type ", ""))
		print("Kitchen: ", equipped_kitchen[-1])
	else: 
		equipped_kitchen.append(None)
		print("Kitchen: ", equipped_kitchen[-1])

	#furnished
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	str_match = [s.text for s in buffer if "Furnished" in s.text]
	if str_match:
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', str_match[0]).split())
		if "Yes" in buffer.replace("Furnished ", ""):
			furnished.append(1)
		else:
			furnished.append(0)
		print("Furnished: ", furnished[-1])
	else: 
		furnished.append(None)
		print("Furnished", furnished[-1])

	#open_fire
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	content = [t.text for t in buffer if "Fireplaces" in t.text]
	if content:
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', content[0]).split())
		open_fire.append(buffer.replace("Fireplaces ", ""))
		print("Open fire: ", open_fire[-1])
	else:
		open_fire.append(None)
		print("Open fire: ", open_fire[-1])

	#terrace & terrace_area
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	content = [t.text for t in buffer if "Terrace surface" in t.text]
	if content:
		buffer = " ".join(re.sub(r'[^0-9]+', '', content[0]).split())
		terrace.append(1)
		terrace_area.append(buffer.replace("Terrace surface ", ""))
		print("Terrace: ", terrace[-1])
		print("Terrace surface: ", terrace_area[-1])
	else:
		terrace.append(None)
		terrace_area.append(None)
		print("Terrace: ", terrace[-1])
		print("Terrace surface: ", terrace_area[-1])

	#garden & garden_area
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	content = [t.text for t in buffer if "Garden surface" in t.text]
	if content:
		buffer = " ".join(re.sub(r'[^0-9]+', '', content[0]).split())
		garden.append(1)
		garden_area.append(buffer.replace("Garden surface ", ""))
		print("Garden: ", garden[-1])
		print("Garden area: ", garden_area[-1])
	else:
		garden.append(None)
		garden_area.append(None)
		print("Garden: ", garden[-1])
		print("Garden area: ", garden_area[-1])

	#surface of the plot
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	content = [t.text for t in buffer if "Surface of the plot" in t.text]
	if content:
		buffer = " ".join(re.sub(r'[^0-9]+', '', content[0]).split())
		surface_plot.append(buffer.replace("Surface of the plot ", ""))
		print("Surface of plot: ", surface_plot[-1])
	else:
		surface_plot.append(None)
		print("Surface of plot: ", surface_plot[-1])

	#surface (living area)
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	str_match = [s.text for s in buffer if "Living area" in s.text]
	if str_match:
		buffer = " ".join(re.sub(r'[^0-9]+', '', str_match[0]).split())
		surface.append(buffer.replace("Living area ", ""))
		print("Surface (living area): ", surface[-1])
	else: 
		surface.append(None)
		print("Surface (living area): ", surface[-1])


	#facades
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	content = [t.text for t in buffer if "Number of frontages" in t.text]
	if content:
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', content[0]).split())
		facades.append(buffer.replace("Number of frontages ", ""))
		print("Facades: ", facades[-1])
	else:
		facades.append(None)
		print("Facades: ", facades[-1])

	#swimming_pool
	buffer = soup.find_all("th", {"class": "classified-table__header"})
	content = [t.text for t in buffer if "Swimming pool" in t.text]
	if content:
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', content[0]).split())
		if buffer.replace("Swimming pool ", "") == "Yes":
			swimming_pool.append(1)
		else:
			swimming_pool.append(0)
		print("swimming pool: ", swimming_pool[-1])
	else:
		swimming_pool.append(None)
		print("swimming pool: ", swimming_pool[-1])

	#state
	buffer = soup.find_all("tr", {"class": "classified-table__row"})
	content = [t.text for t in buffer if "Building condition" in t.text]
	if content:
		buffer = " ".join(re.sub(r'[^A-Za-z0-9 -]+', '', content[0]).split())
		state.append(buffer.replace("Building condition", ""))
		print("State: ", state[-1])
	else:
		state.append(None)
		print("State: ", state[-1])

	df = pd.DataFrame()
	df["locality"] = locality
	df["proprety_type"] = proprety_type
	df["price"] = price
	df["bedrooms"] = rooms
	df["area"] = area
	df["equipped_kitchen"] = equipped_kitchen
	df["furnished"] = furnished
	df["open_fire"] = open_fire
	df["terrace"] = terrace
	df["terrace_area"] = terrace_area
	df["garden"] = garden
	df["garden_area"] = garden_area
	df["surface"] = surface
	df["surface_plot"] = surface_plot
	df["facades"] = facades
	df["swimming_pool"] = swimming_pool
	df["state"] = state

	df.to_csv("data.csv", mode='w', header=True)


counter = 0
for i in range(4, 333):

	url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=cheapest"
	print("\n", url, "\n")
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, "lxml")

	for div_containing_link in soup.find_all("li", {"class":"search-results__item"}):
		for link in div_containing_link.find_all("a", {"class":"card__title-link"}):
			counter += 1
			print(f"Page number: {i}, Link count: {counter}")
			print(link["href"])
			get_data_from_link(link["href"])

for i in range(0, 10):

	url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=most_expensive"
	print("\n", url, "\n")
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, "lxml")

	for div_containing_link in soup.find_all("li", {"class":"search-results__item"}):
		for link in div_containing_link.find_all("a", {"class":"card__title-link"}):
			counter += 1
			print(f"Page number: {i}, Link count: {counter}")
			print(link["href"])
			get_data_from_link(link["href"])


