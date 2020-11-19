import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog, ttk
from resolutionSelector import resolutionSelector


def widgets():

    # ROW 1 ####

    link_label = Label(root,
                       text="YouTube link :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=video_Link)
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    resolution_label = Label(root,
                             text="Resolution :",
                             bg="#E8D579")
    resolution_label.grid(row=1,
                          column=3,
                          pady=5,
                          padx=5)

    root.comboResolution = ttk.Combobox(root,
                                        values=["1080",
                                                "720",
                                                "480",
                                                "360"],
                                        textvariable=resolutionBox)
    root.comboResolution.grid(row=1,
                              column=4,
                              pady=5,
                              padx=5)

    # ROW 2 ####

    destination_label = Label(root,
                              text="Destination :",
                              bg="#E8D579")
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=2,
                              column=1,
                              pady=5,
                              padx=5)

    browse_b = Button(root,
                      text="Browse",
                      command=browse,
                      width=10,
                      bg="#05E8E0")
    browse_b.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)

    combobox_label = Label(root,
                           text="Formato :",
                           bg="#E8D579")
    combobox_label.grid(row=2,
                        column=3,
                        pady=5,
                        padx=5)

    root.comboFormato = ttk.Combobox(root,
                                     values=["Mp4",
                                             "Mp3"],
                                     textvariable=formatoBox)
    root.comboFormato.grid(row=2,
                           column=4,
                           pady=5,
                           padx=5)

    # ROW 3 ###

    download_b = Button(root,
                        text="Download",
                        command=download,
                        width=20,
                        bg="#05E8E0")
    download_b.grid(row=3,
                    column=1,
                    pady=3,
                    padx=3)


def browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    download_Path.set(download_directory)


def download():

    youtube_link = video_Link.get()

    download_folder = download_Path.get()

    getvideo = YouTube(youtube_link)

    # getTitle = getvideo.title

    resolution = resolutionBox.get()

    videostream = getvideo.streams.get_by_resolution("1080p")

    print(videostream)

    #downloadresolution = resolutionSelector(resolution, videostream)

    #print(downloadresolution)

    #downloadresolution.download(download_folder)

    # fileFormato = formatoBox.get()

    messagebox.showinfo("SUCCESSFULLY", " DOWNLOADED AND SAVED IN\n" + download_folder)


root = tk.Tk()

root.geometry("700x120")
root.resizable(False, False)
root.title("Downloader")
root.config(background="#000000")

video_Link = StringVar()
download_Path = StringVar()
formatoBox = StringVar()
resolutionBox = StringVar()

widgets()

root.mainloop()
