# Miniproject-Programming
Dit is een Python programma gemaakt door Groep 3 - Klas: V1C. Deze programma heeft als doel het weergeven van
vertrektijden van een gekozen station en het kunnen opvragen van een reisadvies (beide dankzij de NS API).

## Installatie
Om het programma te gebruiken heb je de volgende onderdelen nodig:

Een Windows OS waarop PyCharm Edu versie >=3.0 ge?nstalleerd is.
Python 3.6.2
En de volgende modules
- XMLtoDict
- Requests

## Gebruik

1.	Als je het mapje opent van het miniproject krijg je vier bestanden te zien dit zijn: functions.py, mainmenu.py, ns.png en ns_small.png dit zijn de bestanden die nodig zijn om de applicatie goed uit te voeren.
2.	Uit deze bestanden kies je mainmenu.py en deze open je.
3.	Als je dit bestand opent krijg je een keuze menu te zien met de keuzes: Reisinformatie, Reisadvies en Afsluiten.
4.	Als je de keuze Reisinformatie kiest wordt je doorgeleid naar een volgende pagina waarop je een scherm te zien krijgt. Op dit scherm kun je een station naar keuze invoeren, en over het gekozen station krijg je alle reistijden te zien. Als je dan op ??n van de gekozen reistijden klikt krijg je nog andere informatie te zien zoals: wat voor soort trein het is en wat precies de tussenstations zijn.
5.	Mocht de applicatie een foutmelding geven zoals: ?Station onbekend en/of tijden onjuist? dan zou het kunnen zijn dat je niet de juiste interpreters hebt gedownload.
6.	Je download de juiste interpreters door het programma Pycharm op te starten, als het programma is opgestart ga je naar de optie File > Settings > Project > Project Interpreter > dan klik je op het groene + rechtsboven in de window > dan voer je in het zoekbalkje ??n voor 1 xmltodict en requests in deze interpreters installeer je dan, en als je dan opnieuw de applicatie opstart en bij de optie: Reisinformatie een station invoert zou de applicatie het moeten doen.
7.	Als je de optie: Reisadvies kiest wordt je doorgeleid naar een volgende pagina waarop je een scherm te zien krijgt. Op dit scherm kun je verschillende opties invoeren zoals: Beginstation, Via (een ander station) , Eindstation. Ook kun je een tijd instellen voor wanneer je wilt vertrekken, je kunt dit zelfs instellen voor maand en jaar. Ook heb je de keuze om te kiezen  voor vertrek of aankomst. Je kunt bijvoorbeeld aangeven dat je om 12 uur wilt vertrekken van Utrecht Centraal naar Den Haag Centraal, de applicatie zal dan alle reistijden geven binnen een range van 3 uur.
8.	Als je een begin station en een eindstation naar keuze hebt ingevoerd dan krijg je alle vertrek tijden te zien van wanneer je kunt vertrekken. Als je een optie aan hebt geklikt krijg je in de applicatie te zien vanaf welke stations je vertrekt en eventueel moet overstappen. Als je bijvoorbeeld een hele lange reis hebt ingevoerd waarin je meer als 4 keer moet overstappen zal de applicatie aangeven dat ?Helaas meer dan 4 reisdelen worden niet ondersteund door deze applicatie?.
9.	En de laatste optie van de applicatie is: Afsluiten dit spreekt voor zichzelf, deze optie sluit de hele applicatie en verwijderd alle zoekgeschiedenis.


