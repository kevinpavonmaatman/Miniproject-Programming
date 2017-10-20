from tkinter import *
from functions import *

root = Tk()
root.title('Project Progamming')
root.geometry('{}x{}'.format(1280, 720))
root.resizable(width=False, height=False)

def travel_recommendation():
    """"Uses information_to_dict() to ask for a travel recommendation from the NS API, and inserts the departure times from those recommendations into a listbox."""

    travel_possibilities = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}'.format(from_station_entry.get(), via_station_entry.get(), to_station_entry.get()))

    for possibility in travel_possibilities['ReisMogelijkheden']['ReisMogelijkheid']:
        possibilities_listbox.insert(END, possibility['GeplandeVertrekTijd'][11:16])


possibilities_listbox = Listbox()
possibilities_listbox.pack()

from_station_entry = Entry(root)
via_station_entry = Entry(root)
to_station_entry = Entry(root)
button = Button(master = root, text = 'Geef vertrekmogelijkheden', command=travel_recommendation)

from_station_entry.pack()
via_station_entry.pack()
to_station_entry.pack()
button.pack()

root.mainloop()

# travel_recommendation = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}&previousAdvices=0'.format(from_station, via_station, to_station))
# station_list = information_to_dict('ns-api-stations-v2')
# station_departure_information = information_to_dict('ns-api-avt?station=${}'.format(input_station))

