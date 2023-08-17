import pyaudio
import time
import audioop 
from math import log10
from tkinter import *
from tkinter import ttk

audio_reader = pyaudio.PyAudio()
WIDTH = 2
RATE = int(audio_reader.get_default_input_device_info()['defaultSampleRate'])
DEVICE = audio_reader.get_default_input_device_info()['index']
rms = 1
print(audio_reader.get_default_input_device_info())

root = Tk()
canvas = Canvas(root, width=800, height=800)
decibels = []

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue


stream = audio_reader.open(format=audio_reader.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

def create_window():
    root_frame = ttk.Frame(root, padding=400)
    root_frame.grid()

    canvas.grid(column=0, row=2, sticky=(N, W, E, S))

    ttk.Label(root_frame, text="~AUDIO VISUALISER~").grid(column=0, row=0)
    ttk.Button(root_frame, text="Listen", command=fetch_decibels).grid(column=0, row=1)
        
    # style = ttk.Style()

    # style.theme_create('av', settings={
    #     'TFrame': {'configure': {'background': '#5A5A5A'}}
    # })

    # style.theme_use('av')

    root.mainloop()

def fetch_decibels():
    stream.start_stream()

    while stream.is_active(): 
        db = 20 * log10(rms)
        decibels.append(db)
        print(decibels)
        canvas.create_line(170, 100, 150, 200, fill='red', width=3)
        time.sleep(0.3)

    stream.stop_stream()
    stream.close()

    audio_reader.terminate()

create_window()