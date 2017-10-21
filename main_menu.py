from tkinter import *
from functions import *

#Initialization of Tkinter root and color configuration.
root = Tk()
root.title('Project Progamming')
root.geometry('{}x{}'.format(800, 400))
root.resizable(width=False, height=False)
bgcolor = "#FFCC20"
titlecolor = "#000066"
root.configure(bg=bgcolor)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#Definition of Frames
top_frame = Frame(root, width=200, height=50, pady=3, bg=bgcolor)
buttons_frame = Frame(root, width=200, height=50, bg=bgcolor)
footer_frame = Frame(root, width=200, height=50, bg=bgcolor)

#Position of Frames
top_frame.grid(row=0)
buttons_frame.grid(row=1)
footer_frame.grid(row=2)

#Information in top_frame:
title = Label(top_frame, text='NS Reisadvies Interface')
title.configure(bg=bgcolor, fg=titlecolor, width = 40, height=1, font=("Helvetica", 25, "bold"))
title.grid(row=0)
img = PhotoImage(file="ns.png")
foto = Label(top_frame,image=img, bg=bgcolor)
foto.image = (img)
foto.grid(row=1)
welcometext = Label(top_frame, text='Welkom bij de NS Reisadvies applicatie \n Maak een keuze door te klikken op één van de onderstaande knoppen')
welcometext.configure(bg=bgcolor, fg=titlecolor, width = 100, height=2, font=("Helvetica", 10, "bold"))
welcometext.grid(row=3)

#Information in buttons_frame:
reisinfo_button = Button(master = buttons_frame, text = 'Reisinformatie', bg=titlecolor, fg=bgcolor, font=("Helvetica", 20, "bold"))
reisinfo_button.grid(row=0,column=0,padx=50)
reisadvies_button = Button(master = buttons_frame, text = 'Reisadvies', bg=titlecolor, fg=bgcolor, font=("Helvetica", 20, "bold"))
reisadvies_button.grid(row=0,column=1, padx=20)

#Information in footer_frame
copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
copyright_text.configure(bg=bgcolor, fg=titlecolor, width = 50, height=5, font=("Helvetica", 8, "bold"))
copyright_text.grid(row=0)
exit_button = Button(master = footer_frame, text = 'Afsluiten', bg=titlecolor, fg=bgcolor, font=("Helvetica", 8, "bold"))
exit_button.grid(row=1)
exit_button.bind("<Button-1>",exit)

#Execute
root.mainloop()
