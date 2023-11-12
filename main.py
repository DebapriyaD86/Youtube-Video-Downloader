from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from pytube import YouTube
from PIL import Image, ImageTk


def browse_folder():
    # +-----------------+------------------------------------------------------------------+
    # | Definition      | Asks user to select the path to download video                   |
    # +-----------------+------------------------------------------------------------------+
    # | Parameters      | None                                                             |
    # +-----------------+------------------------------------------------------------------+
    # | Returns         | None                                                             |
    # +-----------------+------------------------------------------------------------------+

    # using the askdirectory() method of the filedialog module to select the directory
    download_path = fd.askdirectory(initialdir="D:\Projects\General\YoutubeVideoDownloader\Downloads", title="Select the folder to save the video")
    # using the set() method to set the directory path in the entry field
    download_dir.set(download_path)


def download_video():
    # +-----------------+------------------------------------------------------------------+
    # | Definition      | Downloads the youtube video from its specified URL               |
    # +-----------------+------------------------------------------------------------------+
    # | Parameters      | None                                                             |
    # +-----------------+------------------------------------------------------------------+
    # | Returns         | None                                                             |
    # +-----------------+------------------------------------------------------------------+

    # Retrieve the youtube video URL and download folder path
    # from the respective entry fields
    youtube_url = video_url.get()
    download_folder = download_dir.get()

    # Check if the entry fields are not empty
    if (youtube_url != "" and download_folder != ""):
        # Create an object of the YouTube class for the request URL
        video = YouTube(youtube_url)

        # Select the stream with file extension = 'mp4', progressive = 'True',
        # and itag = '22' in order to download the video of 720p resolution
        video_stream = video.streams.filter(file_extension="mp4", progressive=True, res="720p",
                                            type="video").get_by_itag(22)

        # Download video to the specified folder to download
        video_stream.download(download_folder)

        # Display message indicating the successful download
        mb.showinfo("Download Complete", "Selected Video is downloaded\nand saved successfully in " + download_folder)
    else:
        # Display error message indicating empty fields
        mb.showerror("Empty Fields", "Fields are empty!")


def reset():
    # +-----------------+------------------------------------------------------------------+
    # | Definition      | Resets the video URL and destination fields to empty             |
    # +-----------------+------------------------------------------------------------------+
    # | Parameters      | None                                                             |
    # +-----------------+------------------------------------------------------------------+
    # | Returns         | None                                                             |
    # +-----------------+------------------------------------------------------------------+

    # Set entry fields to empty string
    video_url.set("")
    download_dir.set("")

    # Set cursor focus to first entry field
    url_field.focus_set()


def exit():
    # +-----------------+------------------------------------------------------------------+
    # | Definition      | Closed the application and the window                            |
    # +-----------------+------------------------------------------------------------------+
    # | Parameters      | None                                                             |
    # +-----------------+------------------------------------------------------------------+
    # | Returns         | None                                                             |
    # +-----------------+------------------------------------------------------------------+

    # Close the application/window
    gui_root.destroy()


if __name__ == "__main__":
    # Create an object of the Tk() class
    gui_root = Tk()

    # Set the title of the window
    gui_root.title("YouTube Downloader")

    # Set the size and position of the window
    gui_root.geometry("580x220+300+150")

    # Disable the resizable option for better UI
    gui_root.resizable(0, 0)

    # Configure the background color of the window
    gui_root.config(bg="#FEE4E3")

    # Configure the icon of the window
    gui_root.iconbitmap("images/download.ico")

    # Add 3 frames to the window using the Frame() widget
    header_frame = Frame(gui_root, bg="#FEE4E3")
    entry_frame = Frame(gui_root, bg="#FEE4E3")
    button_frame = Frame(gui_root, bg="#FEE4E3")
    header_frame.pack()
    entry_frame.pack()
    button_frame.pack()

    # ------------------------- the Header Frame -------------------------

    # Import the youtube logo bitmap image
    the_image = ImageTk.PhotoImage(Image.open("images/youtube_logo.png").resize((50, 35)))

    # Add the labels to the header frame
    image_label = Label(header_frame, image=the_image, bg="#FEE4E3", fg="#FE0700", anchor=SE)
    header_label = Label(header_frame, text="YouTube Video Downloader", font=("verdana", "14", "bold"), bg="#FEE4E3", anchor=SE)

    # Set the position of the labels in the grid format
    image_label.grid(row=0, column=0, padx=10, pady=10)
    header_label.grid(row=0, column=1, padx=10, pady=10)

    # ------------------------- The Entry Frame -------------------------

    # Add the labels to the entry frame
    url_label = Label(entry_frame, text="Video URL:", font=("verdana", "10"), bg="#FEE4E3", fg="#000000", anchor=SE)
    des_label = Label(entry_frame, text="Destination:", font=("verdana", "10"), bg="#FEE4E3", fg="#000000", anchor=SE)

    # Set the position of the labels in the grid format
    url_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)
    des_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    # Create objects to hold video URL and download path
    video_url = StringVar()
    download_dir = StringVar()

    # Add entry fields for video URL and downlaod path in the entry frame
    url_field = Entry(entry_frame, textvariable=video_url, width=35, font=("verdana", "10"),
                      bg="#FFFFFF", fg="#000000", relief=GROOVE)
    des_field = Entry(entry_frame, textvariable=download_dir, width=26, font=("verdana", "10"),
                      bg="#FFFFFF", fg="#000000", relief=GROOVE)

    # Set the position of the entry fields in the grid format
    url_field.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    des_field.grid(row=1, column=1, padx=5, pady=5)

    # Add a button to the entry frame to browse folder path
    # Set it to trigger 'browse_folder' function on click
    browse_button = Button(entry_frame, text="Browse", width=7, font=("verdana", "10"), bg="#FF9200",
                           fg="#FFFFFF", activebackground="#FFE0B7", activeforeground="#000000",
                           relief=GROOVE, command=browse_folder)

    # Set the position of the button in the grid format
    browse_button.grid(row=1, column=2, padx=5, pady=5)

    # ------------------------- The Button Frame -------------------------

    # Add a button to the button frame to download video
    # Set it to trigger 'download_video' function on click
    download_button = Button(button_frame, text="Download", width=12, font=("verdana", "10"),
                             bg="#15EF5F", fg="#FFFFFF", activebackground="#97F9B8", activeforeground="#000000",
                             relief=GROOVE, command=download_video)

    # Add a button to the button frame to reset the entry fields
    # Set it to trigger 'reset' function on click
    reset_button = Button(button_frame, text="Clear", width=12, font=("verdana", "10"), bg="#23B1E6",
                          fg="#FFFFFF", activebackground="#C3E6EF", activeforeground="#000000",
                          relief=GROOVE, command=reset)
    # Add a button to the button frame to close the application
    # Set it to trigger 'exit' function on click
    close_button = Button(button_frame, text="Exit", width=12, font=("verdana", "10"), bg="#F64247",
                          fg="#FFFFFF", activebackground="#F7A2A5", activeforeground="#000000",
                          relief=GROOVE, command=exit)

    # Set the position of the buttons in the grid format
    download_button.grid(row=0, column=0, padx=5, pady=10)
    reset_button.grid(row=0, column=1, padx=5, pady=10)
    close_button.grid(row=0, column=2, padx=5, pady=10)

    # Trigger mainloop() method
    gui_root.mainloop()