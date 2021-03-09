### Packages ###

import os, random, time
import RPI.GPIO as GPIO
import simpleaudio as sa


### Config ###

# Path to wave files
audio_path = './'
# GPIO pin number the switch is connected to
switch_gpio_pin_number = 18


### Setup GPIO ###

# Setting GPIO mode to Broadcom
GPIO.setmode(GPIO.BCM)
# Set the GPIO pin to input and pull up
GPIO.setup(switch_gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)


### Functions ###

def get_wave_files(path: str):
  # List of files in a given path
  files = os.listdir(path)
  # New empty list to populate with .wav files
  wave_files = []
  # For every file in given path
  for file in files:
    # If the file is type .wav
    if file.endswith('.wav'):
      # Append to wav file list
      wave_files.append(path + file)
  # Return list of wav files in a given path
  return wave_files

def pick_random_clip(clips: list):
  # Get the length of a list of clips
  number_of_clips = len(clips)
  # If the length is greater than 0
  if number_of_clips > 0:
    # Use random to pick a random clip
    random_int = random.randint(1, len(clips))
    # Minus 1 from the int to get the index
    random_index = random_int - 1
    # Return random clip
    return clips[random_index]
  else:
    # Return null if clips list was empty
    return null
    
def play_clip(clip_path):
  try:
    # Use simple audio to load the wave file
    wave_object = sa.WaveObject.from_wave_file(clip_path)
    # Use simple audio to play the wave file
    play_object = wave_object.play()
    # Wait for the wave file to finish playing
    play_object.wait_done()
  except FileNotFoundError:
    # Return an error if the wave file was not found
    print('Wav File ' + file_name + ' does not exist')

def switch_press():
  # Get a list of wave files from a given path
  wave_files = get_wave_files(audio_path)
  # Select a wave file from the path at random
  selected_wave_file = pick_random_clip(wave_files)
  # Play the randomly selected wave file
  play_clip(selected_wave_file)


### Main ###
while True:
  # Get the state of the switch via GPIO
  switch_state = GPIO.input(switch_gpio_pin_number)
  # If the state is False, the switch is in the closed position (Pressed)
  if switch_state == False:
    # Trigger the switch press function to play a random wave file
    switch_press()
    # Set a grace period before it can be triggered again
    time.sleep(1)
