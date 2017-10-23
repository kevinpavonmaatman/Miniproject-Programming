from tkinter import *
from functions import *

def load_mainmenu(event):

    #Loading global frames
    global top_frame
    global buttons_frame
    global footer_frame

    #Removal of previous frames.
    buttons_frame.destroy()
    top_frame.destroy()
    footer_frame.destroy()

    #Definition of Frames
    top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
    buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
    footer_frame = Frame(root, width=200, height=50, bg=bg_color)

    #Position of New Frames
    top_frame.grid(row=0)
    buttons_frame.grid(row=1)
    footer_frame.grid(row=2)

    #Information in top_frame:
    title = Label(top_frame, text='NS Main Menu Interface')
    title.configure(bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
    img = PhotoImage(file="ns.png")
    foto = Label(top_frame,image=img, bg=bg_color)
    foto.image = (img)
    welcometext = Label(top_frame, text='Welkom bij de NS Reisadvies applicatie \n Maak een keuze door te klikken op één van de onderstaande knoppen')
    welcometext.configure(bg=bg_color, fg=fg_color, width = 100, height=2, font=("Helvetica", 10, "bold"))

    #Position of objects in top_frame
    title.grid(row=0)
    foto.grid(row=1)
    welcometext.grid(row=2)

    #Information in buttons_frame:
    reisinfo_button = Button(master = buttons_frame, text = 'Reisinformatie', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
    reisinfo_button.grid(row=0,column=0,padx=50)
    reisadvies_button = Button(master = buttons_frame, text = 'Reisadvies', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
    reisadvies_button.grid(row=0,column=1, padx=20)

    #Information in footer_frame
    copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
    copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=5, font=("Helvetica", 8, "bold"))
    exit_button = Button(master = footer_frame, text = 'Afsluiten')
    exit_button.configure(bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))
    copyright_text.grid(row=0)
    exit_button.grid(row=1)

    #Button Bindings
    reisinfo_button.bind("<Button-1>", load_reisinfomenu)
    reisadvies_button.bind("<Button-1>", load_reisadviesmenu)
    exit_button.bind("<Button-1>", exit)

def load_reisinfomenu(event):

    #Loading global frames
    global top_frame
    global buttons_frame
    global footer_frame
    #Removal of previous frames.
    buttons_frame.destroy()
    top_frame.destroy()
    footer_frame.destroy()

    #Definition of Frames
    top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
    buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
    footer_frame = Frame(root, width=200, height=50, bg=bg_color)

    #Position of New Frames
    top_frame.grid(row=0)
    buttons_frame.grid(row=1)
    footer_frame.grid(row=2)

    #Information in top_frame:
    title = Label(top_frame, text='NS Reisinformatie Interface')
    title.configure(bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
    title.grid(row=0)
    img = PhotoImage(file="ns.png")
    foto = Label(top_frame,image=img, bg=bg_color)
    foto.image = (img)
    foto.grid(row=1)

    #Information in buttons_frame:
    backtomenu_button = Button(master = buttons_frame, text = 'Terug naar het menu', bg=fg_color, fg=bg_color, font=("Helvetica", 10, "bold"))
    backtomenu_button.grid(row=0,column=0,padx=50)

    # #Information in footer_frame
    copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
    copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=5, font=("Helvetica", 8, "bold"))
    copyright_text.grid(row=0)
    exit_button = Button(master = footer_frame, text = 'Afsluiten', bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))
    exit_button.grid(row=1)

    #Button bindings
    backtomenu_button.bind("<Button-1>", load_mainmenu)
    exit_button.bind("<Button-1>", exit)

def load_reisadviesmenu(event):

    #Loading global frames
    global top_frame
    global buttons_frame
    global footer_frame
    #Removal of previous frames.
    buttons_frame.destroy()
    top_frame.destroy()
    footer_frame.destroy()

    #Definition of Frames
    top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
    buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
    footer_frame = Frame(root, width=200, height=50, bg=bg_color)

    #Position of Frames
    top_frame.grid(row=0)
    buttons_frame.grid(row=1)
    footer_frame.grid(row=2)

    #Information in top_frame:
    title = Label(top_frame, text='NS Reisadvies Interface')
    title.configure(bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
    title.grid(row=0)
    img = PhotoImage(file="ns.png")
    foto = Label(top_frame,image=img, bg=bg_color)
    foto.image = (img)
    foto.grid(row=1)

    #Information in buttons_frame:
    backtomenu_button = Button(master = buttons_frame, text = 'Terug naar het menu', bg=fg_color, fg=bg_color, font=("Helvetica", 10, "bold"))
    backtomenu_button.grid(row=0,column=0,padx=50)

    #Information in footer_frame
    copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
    copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=5, font=("Helvetica", 8, "bold"))
    copyright_text.grid(row=0)
    exit_button = Button(master = footer_frame, text = 'Afsluiten', bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))
    exit_button.grid(row=1)


    #Button Bindings
    exit_button.bind("<Button-1>", exit)
    backtomenu_button.bind("<Button-1>", load_mainmenu)

#Initialization of Tkinter root and color configuration.
root = Tk()
root.title('Project Progamming')
root.geometry('{}x{}'.format(800, 400))
root.resizable(width=False, height=False)
bg_color = "#FFCC20"
fg_color = "#000066"
root.configure(bg=bg_color)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#Definition of Frames
top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
footer_frame = Frame(root, width=200, height=50, bg=bg_color)

#Position of Frames
top_frame.grid(row=0)
buttons_frame.grid(row=1)
footer_frame.grid(row=2)

#Information in top_frame:
title = Label(top_frame, text='NS Main Menu Interface')
title.configure(bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
img = PhotoImage(file="ns.png")
foto = Label(top_frame,image=img, bg=bg_color)
foto.image = (img)
welcometext = Label(top_frame, text='Welkom bij de NS Reisadvies applicatie \n Maak een keuze door te klikken op één van de onderstaande knoppen')
welcometext.configure(bg=bg_color, fg=fg_color, width = 100, height=2, font=("Helvetica", 10, "bold"))

#Position of objects in top_frame
title.grid(row=0)
foto.grid(row=1)
welcometext.grid(row=2)

#Information in buttons_frame:
reisinfo_button = Button(master = buttons_frame, text = 'Reisinformatie', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
reisinfo_button.grid(row=0,column=0,padx=50)
reisadvies_button = Button(master = buttons_frame, text = 'Reisadvies', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
reisadvies_button.grid(row=0,column=1, padx=20)

# #Information in footer_frame
copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=5, font=("Helvetica", 8, "bold"))
copyright_text.grid(row=0)
exit_button = Button(master = footer_frame, text = 'Afsluiten', bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))
exit_button.grid(row=1)

#Button Bindings
reisinfo_button.bind("<Button-1>", load_reisinfomenu)
reisadvies_button.bind("<Button-1>", load_reisadviesmenu)
exit_button.bind("<Button-1>", exit)

#Execute
root.mainloop()
