from tkinter import *
from functions import *

root = Tk()
root.title('Project Progamming')
root.geometry('{}x{}'.format(1280, 720))
root.resizable(width=False, height=False)

def travel_recommendation():
    """"Uses information_to_dict() to ask for a travel recommendation from the NS API, and inserts the departure times from those recommendations into a listbox."""

    global travel_possibilities

    travel_possibilities_dict = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}'.format(from_station_entry.get(), via_station_entry.get(), to_station_entry.get()))
    travel_possibilities = [possibility for possibility in travel_possibilities_dict['ReisMogelijkheden']['ReisMogelijkheid']]

    possibilities_listbox.delete(0, END)

    for possibility in travel_possibilities:
        possibilities_listbox.insert(END, possibility['GeplandeVertrekTijd'][11:16])


def listbox_selection(event):
    selection_index = int(possibilities_listbox.curselection()[0])
    for possibility in travel_possibilities:
        if travel_possibilities.index(possibility) == selection_index:
            # Code to display information of the possibility
            print(possibility) # Explanatory print

possibilities_listbox = Listbox()
possibilities_listbox.pack()
possibilities_listbox.bind('<<ListboxSelect>>', listbox_selection)

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

