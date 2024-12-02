from datetime import datetime
from pytz import country_timezones
import pytz

from paises import *

print("================ horário mundial ============")


time_zones = pytz.all_timezones

timezone_country = {}

for countrycode in country_timezones:
    timezones = country_timezones[countrycode]
    for timezone in timezones:
        timezone_country[timezone] = countrycode


zonas = []
for i in timezone_country.keys():
    zonas.append(i)

zona_selecionada = pytz.timezone(zonas[5])
country_time = datetime.now(zona_selecionada)
print(country_time)


simbol_do_pais = [timezone_country[zonas[5]]]

for i in paises.keys():
    simbol_do_pais.append(i.lower())

imagem = "png250px/{}.{}".format(simbol_do_pais[0],'png')
key = simbol_do_pais[0].upper()
nome_do_pais = paises[key]
print(imagem, nome_do_pais)

print(f"A data de {zona_selecionada} é {country_time.strftime('%d-%m-%y')} e o pais é {nome_do_pais} e la são {country_time.strftime('%H:%M:%S')} Horas")

