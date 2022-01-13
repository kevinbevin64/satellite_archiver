import requests
from bs4 import BeautifulSoup as BS


"""
1 - Get all the times listed on website

2 - Convert times into a valid url pointing to its corresponding image

3 - Download image from url

URL struc --> https://www.nea.gov.sg/docs/default-source/satelliteimage/bluemarbleasean_{year}{date}_{n_time}.jpg
	e.g. --> https://www.nea.gov.sg/docs/default-source/satelliteimage/BlueMarbleASEAN_20220113_0820.jpg





"""

# Fetch the page and create BeautifulSoup object
page = requests.get("https://www.nea.gov.sg/weather/satellite-images")
print(page.content)

soup = BS(page.content, "html.parser")
print(soup)


list_container = soup.find("div", class_="weather-widget")
img_list = list_container.find("ul", class_="satellite-overlay-history-items")
img_list_items = img_list.find_all("li")

for item in img_list:
	print(True)



"""
def img_dl():
	
	now = datetime.now()
	current_time = now.strftime("%Y-%m-%d | %H:%M:%S")

	d = datetime.today() - timedelta(hours=2)
	year = d.strftime('%Y')
	date = d.strftime('%m%d')
	hours = d.strftime('%H')
	mins = d.strftime('%M')
	n_time = hours + mins


	f = 'SAT_' + year + '-' + date[:2] + '-' + date[2:] + '-' + n_time
	img = f'https://www.nea.gov.sg/docs/default-source/satelliteimage/bluemarbleasean_{year}{date}_{n_time}.jpg'

	
	if mins == '00' or mins == '20' or mins == '40':
		
		filename = f + '.png'
		
		response = requests.get(img)

		file = open(filename, 'wb')

		file.write(response.content)

		file.close
		
		print(f'Download completed at: {current_time}\n')
		

		time.sleep(900)

"""












