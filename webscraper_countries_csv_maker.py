from bs4 import BeautifulSoup
import csv
import requests


url ='https://www.scrapethissite.com/pages/simple/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

overall = soup.find(id='countries')
container = overall.find_all('div', class_='country')


countries = []
names = []
populations = []
areas = [] 

for stats in container:
    name = stats.find('h3', class_='country-name')
    countries.append(name.text.strip())
    capital = stats.find('span', class_='country-capital')
    names.append(capital.text)
    population = stats.find('span', class_='country-population')
    populations.append(population.text)
    area = stats.find('span', class_='country-area')
    areas.append(area.text)


rows = zip(countries, names, populations, areas)

with open('country_statistics.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(["Country", "Capital", 'Population', 'Area (Km^2)'])
    for row in rows: 
        thewriter.writerow(row)



