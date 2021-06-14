import tkinter as tk
from tkinter import font
import numpy
import sounddevice as sd
import sys
import queue
import threading


class CoughEvaluatorUI:
    def __init__(self):
        self.root = tk.Tk()
        self.width = 1200
        self.height = 720
        self.font = font.Font(self.root, size=50)
        self.__create_canvas()

    def __create_canvas(self):
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.__create_record_button()
        self.canvas.pack()

    def __callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.audio_data_queue.put(indata.copy())
        # self.audio_data = numpy.concatenate((self.audio_data, self.audio_data_queue.get()))

    def __record(self):
        self.audio_data_queue = queue.Queue()
        self.audio_data = numpy.array([[0]])
        print(self.audio_data.size)
        self.thread = threading.Thread(
            target=file_writing_thread,
            kwargs=dict(
                file=filename,
                mode='x',
                samplerate=int(self.stream.samplerate),
                channels=self.stream.channels,
                q=self.audio_q,
            ),
        )
        self.thread.start()
        with sd.InputStream(samplerate=1000, device=1,
                            channels=1, callback=self.__callback):
            while True:
                data = self.audio_data_queue.get()
                if data is None:
                    break
                # f.write(data)
                self.audio_data = numpy.concatenate((self.audio_data, data))

    def __record_button_press_handler(self):
        self.canvas.delete(self.record_button_on_canvas)
        self.__create_stop_button()
        self.__record()

    def __stop_button_press_handler(self):
        self.canvas.delete(self.record_button_on_canvas)
        sd.stop()
        self.__create_record_button()

    def __create_record_button(self):
        self.record_button = tk.Button(self.canvas, text="Record", bg="#c54985", font=self.font,
                                       command=lambda: self.__record_button_press_handler())
        self.record_button_on_canvas = self.canvas.create_window(600, 460, window=self.record_button, anchor="center")

    def __create_stop_button(self):
        self.record_button = tk.Button(self.canvas, text="Stop recording", bg="#c54985", font=self.font,
                                       command=lambda: self.__stop_button_press_handler())
        self.record_button_on_canvas = self.canvas.create_window(600, 460, window=self.record_button, anchor="center")

    def main(self):
        self.canvas.mainloop()


gg = CoughEvaluatorUI()
gg.main()
