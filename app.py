import geocoder
import requests
import csv


def currency(country):
    with open('mapping.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if country in row:
                return row[1]


def converter(def_currs, local_curr, user):
    result = []
    for curr in def_currs:
        url =f'https://free.currconv.com/api/v7/convert?q={curr}_{local_curr},{local_curr}_{curr}&compact=ultra&apiKey={user}'
        r = requests.get(url)
        result.append(r.text)
    return result


def get_location(user):
    g = geocoder.ip('me')
    payload = {'lat': g.lat, 'lng': g.lng, 'lang': None, 'radius': 0}
    url_geo = 'http://api.geonames.org/countryCode?username='+user
    r = requests.get(url_geo,params= payload)
    country_code = r.text.strip()
    return country_code

if __name__ == "__main__":

    default_currencies = ['USD','EUR','UAH']
    # YOUR USER NAME ON GEONAMES.ORG
    user_geo = ''
    # API KEY ON FREE.CURRCONV.COM
    user_converter = ''


    curr = currency(get_location(user_geo))
    print(converter(default_currencies,curr,user_converter))