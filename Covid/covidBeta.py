from datetime import datetime
from covid import Covid
covid = Covid()
for line in covid.list_countries():
    line = line['name']
    print(line)
while True:
    country = input('Enter Country: ')
    try:
        DataJson = covid.get_status_by_country_name(country)
        country = DataJson["country"]
        confirmed = DataJson["confirmed"]
        active = DataJson["active"]
        deaths = DataJson["deaths"]
        recovered = DataJson["recovered"]
        last_update = DataJson["last_update"]
        print(f'country: {country}')
        print(f'active: {active}')
        print(f'deaths: {deaths}')
        print(f'country: {confirmed}')
        print(f'recovered: {recovered}')
        print(f'last_update: {last_update}')
    except ValueError:
        print('country Not Found Try Agin . . .')
        continue
