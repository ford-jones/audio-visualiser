import pyaudio
import time
import audioop 
from math import log10
from tkinter import *
from tkinter import ttk

audio_reader = pyaudio.PyAudio()                                                                    #   Instantiate the audio parser
WIDTH = 2                                                                                           #   Set sample width in bytes
RATE = int(audio_reader.get_default_input_device_info()['defaultSampleRate'])                       #   Set sample rate
DEVICE = audio_reader.get_default_input_device_info()['index']                                      #   Fetch capture device (mic / built-in)
rms = 1                                                                                             #   Instantiate root-mean-square
print(audio_reader.get_default_input_device_info())                                                 #   Print capture device data to console

root = Tk()                                                                                         #   Instantiate Tkinter
decibels = []                                                                                       #   Define a container to store decibel data
x0 = 0                                                                                              #   Define x-axis draw start location
x1 = 10                                                                                             #   Define x-axis draw end location
canvas = Canvas(root, width=300, height=200)                                                        #   Instantiate square canvas, append to tkinter

def callback(in_data, frame_count, time_info, status):
    global rms                                                                                      #   Make root-mean-square mutations accessible out of scope
    rms = audioop.rms(in_data, WIDTH) / 32767                                                       #   Calculate root-mean-square
    return in_data, pyaudio.paContinue                                                              #   Return data, continue stream


stream = audio_reader.open(format=audio_reader.get_format_from_width(WIDTH),                        #   Create a stream to capture audio device data
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

def create_window():
    root.title('Audio Visualiser')                                                                  #   Instatiate window title
    root_frame = ttk.Frame(root, padding=250)                                                       #   Instatiate window-frame, append to tkinter
    root_frame.grid()                                                                               #   Instantiate window layout as a grid

    ttk.Label(root_frame, text="~AUDIO VISUALISER~").grid(column=2, row=0)                          #   Create a label / text, append to window-frame
    ttk.Button(root_frame, text="Listen", command=fetch_decibels).grid(column=2, row=1)             #   Create a button, reference onClick function, append to window-frame
    canvas.grid(column=0, row=2, sticky=(N, W, E, S))                                               #   Initialise canvas layout as grid
    sb = Scrollbar(root, orient='horizontal', command=canvas.xview)                                 #   Create a scrollbar, reference canvas onScroll function, append to window-frame
    sb.grid(row=1, column=0, sticky=(W, E))                                                         #   Initialise scrollbar layout as grid
    canvas.configure(xscrollcommand=sb.set)                                                         #   Configure canvas scroll behavior
    root.mainloop()                                                                                 #   Run main event / render loop

def draw():                                                                                         #   Define draw function
    global x0                                                                                       #   Make x-axis mutations available out of scope
    global x1                                                                                       #   Make x-axis mutations available out of scope
    if(len(decibels) > 1):
        prevDecStr = str(decibels[-2])                                                              #   Fetch seacond most recent dB reading from array
        prevPosInt = int(prevDecStr[1:].split('.')[0])                                              #   Convert negative floating point to positive integer
        currentDecStr = str(decibels[-1])                                                           #   Fetch first most recent dB reading from array
        currentPosInt = int(currentDecStr[1:].split('.')[0])                                        #   Convert negative floating point to positive integer
        canvas.create_line(x0, prevPosInt, x1, currentPosInt, fill='red', width=3)                  #   Draw a line on the canvas
        canvas.configure(scrollregion=canvas.bbox('all'))                                           #   Configure the canvases scroll area to be the entirety of its' own binding box
        canvas.xview_moveto(1)                                                                      #   Move to the end location of the x-axis scroll bar
        x0 += 10                                                                                    #   Mutate the x-axis line start point
        x1 += 10                                                                                    #   Mutate the x-axis line endpoint

def fetch_decibels():
    stream.start_stream()                                                                           #   Initialise the audio stream

    while stream.is_active():                                                                       #   Check the stream is still running, if so, loop
        db = 20 * log10(rms)                                                                        #   Calculate stream data as decibels
        decibels.append(db)                                                                         #   Append most recent calculation to decibels array
        draw()                                                                                      #   Call the draw function
        root.update()                                                                               #   Update tkinter (update draw result)
        time.sleep(0.1)                                                                             #   Sleep for 0.1sec, when awake loop condition will be checked

    stream.stop_stream()                                                                            #   Stop stream capture once stepped out of loop
    stream.close()                                                                                  #   Close the stream

    audio_reader.terminate()                                                                        #   End audio read process

create_window()                                                                                     #   Initialise the program