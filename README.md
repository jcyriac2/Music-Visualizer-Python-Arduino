# Music-Visualizer-Python-Arduino
This project uses a python script to perform real-time FFT on an input audio file and then send the frequency levels to an Arduino Uno to be displayed on an LED matrix.

## Current Project Status
So far,the circuit is set up to contain 1 row of 8 LEDs on a breadboard to show the frequency level for 1 frequency from the audio file.
The LEDs are driven from the parallel output pins of two 4-bit shift registers(SN74LS194AN). The Arduino is responsible for providing the data in an appropriate format to the shift registers.

## Files in this Repository
1. convertmp3towav.sh - bash script to help convert any mp3 file to wav file of sampling rate is 22050Hz; to be used by the python script

2. frequency_level_encoder.ino - Code that is flashed onto the Arduino. This code accepts the strength of particular frequencies in the audio being
played. The values are recieved serially from the computer(python script) and ranges from 0 to 8. The code then generates a byte of binary 
digits where 0 indicate that LEDs should be turned off and 1 indicates an LED should be lit. For eg. 11110000 means the first 4 LEDs must
be lit and the last 4 LEDs in the strip must be off. The arduino code then shifts this byte out to the shift registers and the LEDs respond
immediately.

3. Visualizer.py - The python script intially opens a wav audio file specified together when the script is launched. It also sets up a serial
connection to the Ardunio. It takes the audio file, extracts a small chunk of the data, plays that small chunk theough the speakers and then
performs Fast Fourier Transform(FFT) on that data. The strength levels of the required frequencies are extracted, normalized, smoothed and
a level between 0 to 8 is sent as a byte serially to the Arduino. This process repeats until the whole audio file is played. 

4. Visualizer_graphics.py - This python script helps in displaying real-time frequency strength levels of the audio to the computer screen.
Currently, the Visualization works but the FFT frequencies that are displayed aren't very sensitive to the music frequencies

## How to RUN
python Visualizer_graphics.py music_file_with_22.05KHz_sampling
