# Roy Sanchez
# Program: sinePitch.py
# Description: sineWave class creates a sine wave, saves int representation of pitch to chunks
# chunks are saved to stream
# User input correlates to int representation of pitch and plays audio.
'''
# PyAudio Documentation:
  https://people.csail.mit.edu/hubert/pyaudio/docs/#:~:text=To%20use%20PyAudio%2C%20first%20instantiate,desired%20audio%20parameters%20using%20pyaudio.
# Examples referenced for adding chunks (of audio frames) to a stream
# and the creation of a sine wave. As well as use of the try: and except: block
  https://www.programcreek.com/python/example/52624/pyaudio.PyAudio
# Midi note number to frequency conversion:
  https://en.wikipedia.org/wiki/MIDI_tuning_standard
'''

import pyaudio
import numpy as np
import wave

CHUNK = 1024

'''
class sineSynth():

sin_freq

sin_amp

sin_dur

Create sine wave with values 

convert to array

convert to byte

push to stream and output

'''
audio_list = []
audio_array_list = []
byte_array = []

# Holds parameters for frequenct, amplitude, duration
class sineSynth():
    def __init__(self, frequency, amplitude, duration): # empty placeholders for freq, amp, dur
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        
    def sin_freq(self,d): # Calculate freq of sin
        if d < 0 or d > 128:
            print("Number inputted does not follow midi note guidelines")
            return 1
        else:
            self.frequency = (2 ** ((d - 69) / 12) * 440)
            return self.frequency
        
    def sin_amp(self, a): # Calculate amp of sin
        a = self.amplitude
        return a
    
    def sin_dur(self, dur):
        dur = self.duration
        return dur

def contents_of_audioList():
     for i in audio_list:
                
        audio = (i * (2 ** 15 - 1) / np.max(np.abs(i)))   # computes the absolute value from the maximum of the array
        audio = audio.astype(np.int16)  # Converting to 16-bit data
        audio_array_list.append(audio)

def contents_of_byteArray():
    for i in audio_array_list:
        print(i)
        byteAudio = i.tobytes() # converts array to bytes
        byte_array.append(byteAudio)
        
def sin_wave():

    while(1):
        x = input("Would you like to add another note? (Yes or No)").lower()
        if(x == 'yes'):
            freq = int(input("Enter a midi note number (0 - 128): ")) # Frequency input
            amp = int(input("Enter a int number that correlates to amplitude (0 == no sound. 1 == sound and 1+ == louder sound)")) # Amplitude input
            dur = int(input("Enter a int number that correlates to duration in seconds: ")) # Duration input

            sine_obj = sineSynth(freq, amp, dur) #add freq, amp, dur
    
            frequency = sine_obj.sin_freq(freq)
            # FORMAT = pyaudio.paInt16
            CHANNELS = 2
            sampling_rate = 44100
            duration = sine_obj.sin_amp(amp)
            nSamps = int(duration * sampling_rate)
            amplitude = sine_obj.sin_dur(dur)
            phase = 0.0
            p = pyaudio.PyAudio()


    
            sw = np.arange(0, nSamps * 2, 1)  # Values contained within  an array
            sine_wave = amplitude * np.sin(2 * np.pi * frequency * sw / sampling_rate + phase) # Creation of a sine waveform 

            audio_list.append(sine_wave)
        
        elif(x == 'no'):
            
            contents_of_audioList()
            contents_of_byteArray()

            for byte in byte_array:
        
                # Possibly using the .open function will not work. May have to convert sample to wav and then push to stream
                #
                #
                try:
                    # byteAudio = audio.tobytes() # converts array to bytes
    
                    stream = p.open(
                        format=p.get_format_from_width(width = 2),
                        channels = 2,
                        rate = sampling_rate,
                        output = True,
                        frames_per_buffer = CHUNK
                        )
    
                    # Read data based on chunk size
                    # date = byteAudio.readframes(CHUNK)

                    # Play stream
                    while len(byte) > 0:
                        print("Entered")
                        for byte in byte_array:
                            stream.write(byte) # writes to stream and plays audio
                        stream.close()
                        p.terminate()
    
                except (wave.Error):
                    raise ValueError("Cannot read file, is it not a wav?")

        else:
            print("Wrong value inputted.")
            return 1
sin_wave()
