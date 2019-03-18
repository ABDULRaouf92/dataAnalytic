# -----------------------Imports
from tkinter import *
from tkinter import ttk
import os
import threading
from random import randint
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from random import randint
import sys
import csv

# ---------------- end of imports

## matplotlib styles
## https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html

running = False  # Global flag

style.use("seaborn-whitegrid")

### set up the figure
fig = plt.Figure()
fig1 = plt.Figure()
fig2 = plt.figure()

### change the figure size
fig.set_size_inches(3, 1, forward=True)
fig1.set_size_inches(3, 1, forward=True)
fig2.set_size_inches(6.5, 4, forward=True)

### set the number of plots in the figure
ax = fig.add_subplot(111)
ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)

ran = randint(1,10)

## main GUI function
#  explain what this function do
global thread
global toAdd2
toAdd2 = []
def main_account_screen():

    def data_acquisition():

        username_info = username_entry.get()
        toAdd2.append(username_info)
        email_info = email_entry.get()
        toAdd2.append(email_info)
        # length_info   = length.get()
        length_info = length_entry.get()
        toAdd2.append(length_info)

        # size_info     = size.get()
        size_info = size_entry.get()
        toAdd2.append(size_info)


        # # clear the entry widgit
        # username_entry.delete(0, END)
        # email_entry.delete(0, END)
        # length_entry.delete(0,END)
        # size_entry.delete(0,END)

    # generate random data, write and read from a file
    def data_to_csv():
        out = open('d:\\test1.csv', 'w')
        out.write(str("Hr1")+ ","+str("hr2")+"\n")
        while True:
            if running:
                out.write(str(ran)+ ","+str(ran)+"\n")
        out.close()

    def save(filename):
        toAdd = ["Name", "Email", "length", "Gewicht"]
        with open(filename, "r") as infile:
            reader = list(csv.reader(infile))
            reader.insert(0, toAdd)
            reader.insert(1, toAdd2)

        with open(filename, "w") as outfile:
            writer = csv.writer(outfile)
            for line in reader:
                writer.writerow(line)
        # writer.close()

    def data_points():
        f = open("data.txt", "w")
        for i in range(100):
            f.write(str(randint(0, 10)) + '\n')
        f.close()

        f = open("data.txt", "r")
        data = f.readlines()
        f.close()

        l = []
        for i in range(len(data)):
            l.append(int(data[i].rstrip("\n")))
        return l

    # animate the data
    def animate(i):
        # clear the figure
        ax.clear()

        ax.plot(range(100), data_points())

    def animate1(i):
        # clear the figure
        ax1.clear()
        ax1.plot(range(100), data_points())  # marker='o', color='blue'

    def animate2(i):
        # clear the figure
        ax2.clear()
        ax2.plot(range(100), data_points(), color="red")

    # clean the GUI window
    def destroy():
        label1.grid_forget()
        label11.grid_forget()
        label2.grid_forget()
        label22.grid_forget()
    #    labelph.grid_forget()
        # label.grid_forget()
        startButton.grid_forget()
        stopButton.grid_forget()
        canvas.get_tk_widget().grid_forget()
        canvas1.get_tk_widget().grid_forget()
        canvas2.get_tk_widget().grid_forget()

    # stop Button
    def stop():
        global running
        running = False


        destroy()

        username_lable.pack()
        username_entry.pack()

        email_lable.pack()
        email_entry.pack()

        length_lable.pack()
        length_entry.pack()

        size_lable.pack()
        size_entry.pack()

        saveButton.pack()

        # sys.exit("Quit")

    #create the main "home" page widgets

    def destory2():

        username_lable.pack_forget()
        username_entry.pack_forget()

        email_lable.pack_forget()
        email_entry.pack_forget()

        length_lable.pack_forget()
        length_entry.pack_forget()

        size_lable.pack_forget()
        size_entry.pack_forget()

        saveButton.pack_forget()

    #start button
    def pack_entry_plotting():

        label1.grid(column=2, row=2, padx=10, pady=3, sticky=E + W + N + S)
        label11.grid(column=3, row=2, padx=10, pady=10, sticky=E + W + N + S)
        label2.grid(column=2, row=3, padx=10, pady=3, sticky=E + W + N + S)
        label22.grid(column=3, row=3, padx=10, pady=10, sticky=E + W + N + S)

        canvas.get_tk_widget().grid(column=4, row=2, padx=30, pady=15)
        canvas1.get_tk_widget().grid(column=4, row=3, padx=30, pady=15)
        canvas2.get_tk_widget().grid(column=0, row=0, rowspan = 2, columnspan = 2, padx=10, pady=3, sticky=E + W + N + S)
        # labelph.grid(row=0, column=3, rowspan=2, columnspan=2)
        # label.grid(row=2, column=0, rowspan=2, columnspan=2)
        startButton.grid(row=0, column=3)
        stopButton.grid(row=0, column=4)


    def start_():

        global running
        running = True

        thread = threading.Thread(target=data_to_csv,daemon = True)
        thread.start()




    def plotting():

        data_acquisition()
        thread2 = threading.Thread(target=save,args=["D:\\test1.csv"],daemon = True)
        thread2.start()
        destory2()
        pack_entry_plotting()
        replace_text()


    def main_page():
        pack_entry_plotting()
        replace_text()

    def replace_text():
        label1.config(width=10, text=" HRV1", fg='black', font="Helvetica 16 bold italic")
        label11.config(width=3, height=1, text=str(randint(0, 100)), fg='black', bg="white",
                       font=("Helvetica 16 bold italic", 40))

        label2.config(width=10, text=" HRV2", fg='black', font="Helvetica 16 bold italic")
        label22.config(width=3, height=1, text=str(randint(0, 100)), fg='black', bg="white", font=("Courier", 40))

        main_screen.after(1000, replace_text)

    global main_screen
    main_screen = Tk()

    main_screen.configure(background='white')
    # window size
    main_screen.geometry("1000x600")
    # set the title
    main_screen.title("VISSEIRO")

    # decleration
    global username
    global email
    global size
    global length

    global username_entry
    global email_entry
    global size_entry
    global length_entry


    username = StringVar()
    email    = StringVar()
    size     = StringVar()
    size.set('0')
    length   = StringVar()
    length.set('0')
    # set labels and entry wedgit
    username_lable = Label(main_screen, text="Username * ")
    username_entry = Entry(main_screen, textvariable=username)

    email_lable = Label(main_screen, text="Email * ")
    email_entry = Entry(main_screen, textvariable=email)

    length_lable = Label(main_screen, text="Größer ")
    # length_entry = Entry(main_screen, textvariable=length)

    length_entry = Scale(main_screen, from_=0, to=200, orient=HORIZONTAL, resolution=10)

    size_lable = Label(main_screen, text="Gewicht ")
    size_entry = Spinbox(main_screen, from_=50, to=120, increment = 10) # xscrollcommand

    label1 = Label(main_screen, bg = "white")
    label11 = Label(main_screen, bg = "white")

    label2 = Label(main_screen, bg = "white")
    label22 = Label(main_screen, bg = "white")


    #add image
    # image = Image.open("index.png")
    #
    # photo = ImageTk.PhotoImage(image.resize((200, 100), Image.ANTIALIAS), master=main_screen)
    # label = Label(main_screen, image=photo)
    # image.resize((200, 250), Image.ANTIALIAS)
    # labelph = Label(main_screen, image=photo)


    startButton = ttk.Button(main_screen, text="Start", style="TButton", command = start_)
    saveButton = ttk.Button(main_screen, text="Save",command=plotting, style="TButton")

    stopButton = ttk.Button(main_screen, text="Stop",style="TButton", command=stop)

    # set the plot window in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=main_screen)
    canvas1 = FigureCanvasTkAgg(fig1, master=main_screen)
    canvas2 = FigureCanvasTkAgg(fig2, master=main_screen)

    # live graph the data from animate function
    ani = animation.FuncAnimation(fig, animate, interval=1000)

    ani1 = animation.FuncAnimation(fig1, animate1, interval=1000)

    ani2 = animation.FuncAnimation(fig2, animate2, interval=1000)

    # pack the wedgit for main page


    pack_entry_plotting()
    replace_text()




    main_screen.mainloop()


if __name__ == '__main__':
    main_account_screen()
