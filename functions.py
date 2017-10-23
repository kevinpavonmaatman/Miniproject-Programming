from tkinter import *

def information_to_dict(api_paramaters):
    """"Takes the part of the URL after http://webservices.ns.nl/ and returns the information from the API as a dictionairy."""

    import requests
    import xmltodict

    response = requests.get('http://webservices.ns.nl/{}'.format(api_paramaters), auth=('tim.vandijk@student.hu.nl', 'Y8TYvZa6rVciUFEZsljW8PyQlmnmBcgZXMXreN67AwaLJarWcLHhvA'))
    response_XML = xmltodict.parse(response.text)

    return response_XML


def notification_label_text(possibility, label, fg_color):
    if 'Melding' in possibility:
        if 'Ernstig' in possibility['Melding']:
            if possibility['Melding']['Ernstig'] == 'true':
                label['text'] = 'Melding: {}'.format(possibility['Melding']['Text'])
                label['fg'] = 'red'
            else:
                label['text'] = 'Melding: {}'.format(possibility['Melding']['Text'])
                label['fg'] = fg_color
        else:
            label['text'] = ''
            for notification in possibility['Melding']:
                if notification['Ernstig'] == 'true':
                    label['text'] += 'Melding: {}\n'.format(notification['Text'])
                    label['fg'] = 'red'
                else:
                    label['text'] += 'Melding: {}\n'.format(notification['Text'])
                    label['fg'] = fg_color
    else:
        label['text'] = ''

def remove_grid_slaves(parent):
    for slave in parent.grid_slaves():
        slave.grid_remove()

def part_maker(parent, bg_color, fg_color, travel_part, column_number, part):
    part_frame = Frame(parent, bg=bg_color)
    part_frame.grid(row=0, column=column_number, sticky=N)

    if part is None:
        part_header = Label(master=part_frame, text='Reisdeel', bg=bg_color, fg=fg_color, font=('Helvetica', 14))
    else:
        part_header = Label(master=part_frame, text='Reisdeel {}'.format(part), bg=bg_color, fg=fg_color, font=('Helvetica', 14))
    carrier = travel_part['Vervoerder']
    ridenumber = travel_part['RitNummer']
    travel_type = travel_part['VervoerType']

    part_label = Label(master=part_frame, text='{} {}    {}'.format(carrier, travel_type, ridenumber), bg=bg_color, fg=fg_color)

    part_header.pack(anchor=W)
    part_label.pack(anchor=W)

    for stop in travel_part['ReisStop']:
        stop_name = stop['Naam']
        if stop['Tijd'] is None:
            stop_departure = 'Tijd n.v.t.'
        else:
            stop_departure = stop['Tijd'][11:16]

        if 'Spoor' in stop:
            if stop['Spoor']['@wijziging'] == 'true':
                stop_platform = stop['Spoor']['#text']
                stop_label = Label(master=part_frame, text='{}, {}, Spoor {} (wijziging)'.format(stop_name, stop_departure, stop_platform), bg=bg_color, fg=fg_color, font=('Helvetica', 9, 'bold'))
            else:
                if '#text' in stop['Spoor']:
                    stop_platform = stop['Spoor']['#text']
                    stop_label = Label(master=part_frame, text='{}, {}, Spoor {}'.format(stop_name, stop_departure, stop_platform), bg=bg_color, fg=fg_color, font=('Helvetica', 9, 'bold'))
                else:
                    stop_label = Label(master=part_frame, text='{}, {}'.format(stop_name, stop_departure), bg=bg_color, fg=fg_color)
        else:
            stop_label = Label(master=part_frame, text='{}, {}'.format(stop_name, stop_departure), bg=bg_color, fg=fg_color)
        stop_label.pack(anchor=W)

def times(time, day, month, year):
    import datetime as dt
    current_time = dt.datetime.today()
    time.insert(0, current_time.strftime('%H:%M'))
    day.insert(0, current_time.strftime('%d'))
    month.insert(0, current_time.strftime('%m'))
    year.insert(0, current_time.strftime('%Y'))