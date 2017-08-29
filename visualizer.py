import sys
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import time
import serial

np.set_printoptions(suppress=True, precision=4)
#open serial port to Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 2)

CHUNKSIZE = 2048
#FREQS = [60,170,310,600,1000,3000,6000,12000,14000,16000]
FREQS = [310]

#0.001 used to prevent divide by zero exception
current_fft = [0.001]*len(FREQS)
previous_fft = [0.001]*len(FREQS)
max_fft = [0.001]*len(FREQS)
scaled_fft = [0.001]*len(FREQS)

FFT_SMOOTH_FACTOR = 0.4;

af = wave.open("/home/jcyriac/Documents/visualizer/"+ sys.argv[1],'rb')

SAMPLE_WIDTH = af.getsampwidth()
RATE= af.getframerate()
print (RATE)
try:
        #initialise pyAudio
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(SAMPLE_WIDTH),
                        channels=af.getnchannels(),
                        rate=RATE,
                        output=True)

        #Read file data
        fdata = af.readframes(CHUNKSIZE)
        #play stream
        while fdata:
                stream.write(fdata)
                npiparray = np.fromstring(fdata,dtype=np.int16)
                fdata = af.readframes(CHUNKSIZE)
                ftdata = np.fft.fft(npiparray, 2048)
                # Grab half of the fourier data
                ftdata = ftdata[:len(ftdata)//2]
                #save old value for smoothing
                previous_fft = current_fft
                #RATE holds current sampling rate
                for index in range(len(FREQS)):
                        current_fft[index] = np.abs(ftdata[round(FREQS[index]/(RATE*2/2048))])
                #record any max fft values
                for index in range(len(current_fft)):
                        if (current_fft[index] > max_fft[index]):
                                max_fft[index] = current_fft[index]

                for i in range(len(current_fft)):
                       current_fft[i]= ((1-FFT_SMOOTH_FACTOR)*current_fft[i]) + (FFT_SMOOTH_FACTOR * previous_fft[i])

                for index in range(len(current_fft)):
                        scaled_fft[index] = current_fft[index]/max_fft[index]
                level = int(scaled_fft[0]*10)
                if (level>8):
                        level = 8
                level = level.to_bytes(1, byteorder = 'big', signed=True)
                ser.write(level)

except KeyboardInterrupt:
        print("Ctrl+C Pressed!")
finally:
        print("Quiting Cleanly")
        stream.stop_stream()
        stream.close()

        #close PyAudio
        p.terminate()
