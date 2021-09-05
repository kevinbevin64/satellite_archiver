import requests, time
from datetime import datetime, timedelta


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


while True:
	img_dl()
	time.sleep(30)












