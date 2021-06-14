# import numpy
# import sounddevice as sd
# import sys
# import queue
#
#
# def int_or_str(text):
#     """Helper function for argument parsing."""
#     try:
#         return int(text)
#     except ValueError:
#         return text
#
#
# q = queue.Queue()
#
#
# def callback(indata, frames, time, status):
#     """This is called (from a separate thread) for each audio block."""
#     if status:
#         print(status, file=sys.stderr)
#     q.put(indata.copy())
#
#
# i = 0
# # while i < 1000:
# with sd.InputStream(samplerate=1000, device=1,
#                     channels=1, callback=callback):
#     i+=1
#     if i==100:
#         sd.stop()
# print(q.get())
#
#
# # #!/usr/bin/env python3
# # """Create a recording with arbitrary duration.
# #
# # The soundfile module (https://PySoundFile.readthedocs.io/) has to be installed!
# #
# # """
# # import argparse
# # import tempfile
# # import queue
# # import sys
# #
# # import sounddevice as sd
# # import soundfile as sf
# # import numpy  # Make sure NumPy is loaded before it is used in the callback
# # assert numpy  # avoid "imported but unused" message (W0611)
# #
# #
# # def int_or_str(text):
# #     """Helper function for argument parsing."""
# #     try:
# #         return int(text)
# #     except ValueError:
# #         return text
# #
# #
# # parser = argparse.ArgumentParser(add_help=False)
# # parser.add_argument(
# #     '-l', '--list-devices', action='store_true',
# #     help='show list of audio devices and exit')
# # args, remaining = parser.parse_known_args()
# # if args.list_devices:
# #     print(sd.query_devices())
# #     parser.exit(0)
# # parser = argparse.ArgumentParser(
# #     description=__doc__,
# #     formatter_class=argparse.RawDescriptionHelpFormatter,
# #     parents=[parser])
# # parser.add_argument(
# #     'filename', nargs='?', metavar='FILENAME',
# #     help='audio file to store recording to')
# # parser.add_argument(
# #     '-d', '--device', type=int_or_str,
# #     help='input device (numeric ID or substring)')
# # parser.add_argument(
# #     '-r', '--samplerate', type=int, help='sampling rate')
# # parser.add_argument(
# #     '-c', '--channels', type=int, default=1, help='number of input channels')
# # parser.add_argument(
# #     '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
# # args = parser.parse_args(remaining)
# #
# # q = queue.Queue()
# #
# #
# # def callback(indata, frames, time, status):
# #     """This is called (from a separate thread) for each audio block."""
# #     if status:
# #         print(status, file=sys.stderr)
# #     q.put(indata.copy())
# #
# #
# # try:
# #     if args.samplerate is None:
# #         device_info = sd.query_devices(args.device, 'input')
# #         # soundfile expects an int, sounddevice provides a float:
# #         args.samplerate = int(device_info['default_samplerate'])
# #     if args.filename is None:
# #         args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
# #                                         suffix='.wav', dir='')
# #
# #     # Make sure the file is opened before recording anything:
# #     with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
# #                       channels=args.channels, subtype=args.subtype) as file:
# #         with sd.InputStream(samplerate=args.samplerate, device=args.device,
# #                             channels=args.channels, callback=callback):
# #             print('#' * 80)
# #             print('press Ctrl+C to stop the recording')
# #             print('#' * 80)
# #             while True:
# #                 file.write(q.get())
# # except KeyboardInterrupt:
# #     print('\nRecording finished: ' + repr(args.filename))
# #     parser.exit(0)
# # except Exception as e:
# #     parser.exit(type(e).__name__ + ': ' + str(e))


import tkinter as tk
import pyaudio as recorder

# --- functions ---

def start():
    global running

    if running is not None:
        print('already running')
    else:
        running = rec.open('nonblocking.wav', 'wb')
        running.start_recording()

def stop():
    global running

    if running is not None:
        running.stop_recording()
        running.close()
        running = None
    else:
        print('not running')

# --- main ---

rec = recorder.Recorder(channels=2)
running = None

root = tk.Tk()

button_rec = tk.Button(root, text='Start', command=start)
button_rec.pack()

button_stop = tk.Button(root, text='Stop', command=stop)
button_stop.pack()

root.mainloop()


import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream
stream.stop_stream()
stream.close()