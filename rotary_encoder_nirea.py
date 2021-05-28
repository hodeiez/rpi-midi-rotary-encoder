#!/usr/bin/python3
# by William Hofferbert
# watches raspberry pi GPIO pins and translates that
# behavior into midi data. Midi data is accessible to
# other clients through a virtual midi device that is
# created with amidithru, via os.system

import RPi.GPIO as GPIO
import time
import mido
import os
import re

#
# script setup
#

# midi device naming and setup
name = "MidiKontrol"

# set up pi GPIO pins for rotary encoder
#Rotary 1
sw_pin1 = 3
dt_pin1 = 5
clk_pin1 = 7
#Rotary 2
sw_pin2 = 11
dt_pin2 = 13
clk_pin2 = 15

#Rotary 3

sw_pin3 = 19
dt_pin3 = 21
clk_pin3 = 23

#Rotary 4
sw_pin4 = 29
dt_pin4 = 33
clk_pin4 = 35

# mode
mode = 0
# button midi info; cc#12 = effect control 1
button_state = 0
button_state1 = 0
button_channel = 0
button_cc_num = 12
# don't let button signals trigger until X ms have passed
button_stagger_time = 220
button_stagger_time1 = 220

# knob midi info; cc#7 = volume, default position near half
position = 63
rotary_increment = 1
rotary_channel = 0
rotary_cc_num = 7
#Knob2 midi values on different modes
position2 = 63
rotary_increment2 = 1
rotary_cc_numA1 = 15
rotary_cc_numA2 = 21
rotary_cc_numA3 = 86
rotary_cc_numA4 = 103
rotary_cc_numA5 = 102
rotary_cc_numA6 = 85
rotary_cc_numA7 = 20
rotary_cc_numA8 = 108
#Knob3 midi values on different modes
position3 = 63
rotary_increment3 = 1
rotary_cc_numB1 = 17
rotary_cc_numB2 = 23
rotary_cc_numB3 = 88
rotary_cc_numB4 = 105
rotary_cc_numB5 = 104
rotary_cc_numB6 = 87
rotary_cc_numB7 = 22
rotary_cc_numB8 = 109
#Knob4 midi values on different modes
position4 = 63
rotary_increment4 = 1
rotary_cc_numC1 = 19
rotary_cc_numC2 = 25
rotary_cc_numC3 = 90
rotary_cc_numC4 = 107
rotary_cc_numC5 = 106
rotary_cc_numC6 = 89
rotary_cc_numC7 = 24
rotary_cc_numC8 = 110

# wait some seconds for other software after reboot
init_sleep_secs = 10

#
# subroutines
#
#method for modeselection with first push button.
def modeselect1(unused):
    global button_state1
    global button_stagger_time1
    global mode
    # do not trigger button actions unless 220 ms have passed
    if (short_circuit_time(button_stagger_time)):
      return
    #print("Button was released!")
    if (button_state == 1):
      button_state = 0
    else:
      button_state = 1
      if (mode < 7):
    mode++
        elif (mode == 7):
         mode = 0
    return mode

def ret_mili_time():
  current_milli_time = int(round(time.time() * 1000))
  return current_milli_time


def short_circuit_time(val):
  global last_time
  myTime = ret_mili_time()
  time_diff = myTime - last_time
  if (time_diff > val):
    last_time = myTime
    return 0
  else:
    return 1


def send_cc(channel, ccnum, val):
  msg = mido.Message('control_change', channel=channel, control=ccnum, value=val)
  #output = mido.open_output(output_name)
  output.send(msg)


def rotary_callback2(unused):
  # rotating clockwise will cause pins to be different
  global position2
  global rotary_increment2
  global mode
  # rotary encoder voltages are equal when going counter-clockwise
  if (GPIO.input(sw_pin2) == GPIO.input(clk_pin2)):
    position2 -= rotary_increment2
    if (position2 < 0):
      position2 = 0
    #print("counterclockwise, pos = %s", position)
  else:
    position2 += rotary_increment2
    if (position > 127):
      position = 127
    #print("clockwise, pos = %s", position)
        if (mode=0)
        send_cc(rotary_channel, rotary_cc_numA1, position2)
        elif (mode=1)
        send_cc(rotary_channel, rotary_cc_numA2, position2)
        elif (mode=2)
        send_cc(rotary_channel, rotary_cc_numA3, position2)
        elif (mode=3)
        send_cc(rotary_channel, rotary_cc_numA4, position2)
        elif (mode=4)
        send_cc(rotary_channel, rotary_cc_numA5, position2)
        elif (mode=5)
        send_cc(rotary_channel, rotary_cc_numA6, position2)
        elif (mode=6)
        send_cc(rotary_channel, rotary_cc_numA7, position2)
        elif (mode=7)
        send_cc(rotary_channel, rotary_cc_numA8, position2)

def rotary_callback3(unused):
  # rotating clockwise will cause pins to be different
  global position3
  global rotary_increment3
  global mode
  # rotary encoder voltages are equal when going counter-clockwise
  if (GPIO.input(sw_pin3) == GPIO.input(clk_pin3)):
    position3 -= rotary_increment3
    if (position3 < 0):
      position3 = 0
    #print("counterclockwise, pos = %s", position)
  else:
    position3 += rotary_increment3
    if (position > 127):
      position = 127
    #print("clockwise, pos = %s", position)
        if (mode=0)
        send_cc(rotary_channel, rotary_cc_numB1, position3)
        elif (mode=1)
        send_cc(rotary_channel, rotary_cc_numB2, position3)
        elif (mode=2)
        send_cc(rotary_channel, rotary_cc_numB3, position3)
        elif (mode=3)
        send_cc(rotary_channel, rotary_cc_numB4, position3)
        elif (mode=4)
        send_cc(rotary_channel, rotary_cc_numB5, position3)
        elif (mode=5)
        send_cc(rotary_channel, rotary_cc_numB6, position3)
        elif (mode=6)
        send_cc(rotary_channel, rotary_cc_numB7, position3)
        elif (mode=7)
        send_cc(rotary_channel, rotary_cc_numB8, position3)

def rotary_callback4(unused):
  # rotating clockwise will cause pins to be different
  global position4
  global rotary_increment4
  global mode
  # rotary encoder voltages are equal when going counter-clockwise
  if (GPIO.input(sw_pin4) == GPIO.input(clk_pin4)):
    position4 -= rotary_increment4
    if (position4 < 0):
      position4 = 0
    #print("counterclockwise, pos = %s", position)
  else:
    position4 += rotary_increment4
    if (position > 127):
      position = 127
    #print("clockwise, pos = %s", position)
        if (mode=0)
        send_cc(rotary_channel, rotary_cc_numC1, position4)
        elif (mode=1)
        send_cc(rotary_channel, rotary_cc_numC2, position4)
        elif (mode=2)
        send_cc(rotary_channel, rotary_cc_numC3, position4)
        elif (mode=3)
        send_cc(rotary_channel, rotary_cc_numC4, position4)
        elif (mode=4)
        send_cc(rotary_channel, rotary_cc_numC5, position4)
        elif (mode=5)
        send_cc(rotary_channel, rotary_cc_numC6, position4)
        elif (mode=6)
        send_cc(rotary_channel, rotary_cc_numC7, position4)
        elif (mode=7)
        send_cc(rotary_channel, rotary_cc_numC8, position4)


def rotary_callback(unused):
  # rotating clockwise will cause pins to be different
  global position
  global rotary_increment
  # rotary encoder voltages are equal when going counter-clockwise
  if (GPIO.input(sw_pin) == GPIO.input(clk_pin)):
    position -= rotary_increment
    if (position < 0):
      position = 0
    #print("counterclockwise, pos = %s", position)
  else:
    position += rotary_increment
    if (position > 127):
      position = 127
    #print("clockwise, pos = %s", position)
  send_cc(rotary_channel, rotary_cc_num, position)


def button_push(unused):
  global button_state
  global button_stagger_time
  # do not trigger button actions unless 220 ms have passed
  if (short_circuit_time(button_stagger_time)):
    return
  #print("Button was released!")
  if (button_state == 1):
    button_state = 0
  else:
    button_state = 1
  midi_state = 127 * button_state
  send_cc(button_channel, button_cc_num, midi_state)

#
# main stuff below
# TODO maybe use the pythonic if __name__ == "__main__":
#

# use P1 header pin numbering convention, ignore warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Set up the GPIO channels
GPIO.setup(dt_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # dt1
GPIO.setup(sw_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # sw1
GPIO.setup(clk_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # clk1
GPIO.setup(dt_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # dt2
GPIO.setup(sw_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # sw2
GPIO.setup(clk_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # clk2
GPIO.setup(dt_pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # dt3
GPIO.setup(sw_pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # sw3
GPIO.setup(clk_pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # clk3
GPIO.setup(dt_pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # dt4
GPIO.setup(sw_pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # sw4
GPIO.setup(clk_pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # clk4
# wait some seconds, so we don't step on MODEP's toes
time.sleep(init_sleep_secs)

# set up backend
mido.set_backend('mido.backends.rtmidi')

# system command to set up the midi thru port
# TODO would be nice to do this in python, but
# rtmidi has issues seeing ports it has created
runCmd = "amidithru '" + name + "' &"
os.system(runCmd)

# regex to match on rtmidi port name convention
#GuitarRotaryEncoder:GuitarRotaryEncoder 132:0
# TODO is it necessary to write:  "\s+(\d+)?:\d+)"  instead?
nameRegex = "(" + name + ":" + name + "\s+\d+:\d+)"
matcher = re.compile(nameRegex)
newList = list(filter(matcher.match, mido.get_output_names()))
# all to get the name of the thing we just made
output_name = newList[0]

# starting time
last_time = ret_mili_time()

# button
GPIO.add_event_detect(dt_pin1,GPIO.FALLING,callback=modeselect1)
GPIO.add_event_detect(dt_pin2,GPIO.FALLING,callback=button_push2)
GPIO.add_event_detect(dt_pin3,GPIO.FALLING,callback=button_push3)
GPIO.add_event_detect(dt_pin4,GPIO.FALLING,callback=button_push4)
# rotary encoder
GPIO.add_event_detect(clk_pin1,GPIO.BOTH,callback=rotary_callback)
GPIO.add_event_detect(clk_pin2,GPIO.BOTH,callback=rotary_callback2)
GPIO.add_event_detect(clk_pin3,GPIO.BOTH,callback=rotary_callback3)
GPIO.add_event_detect(clk_pin4,GPIO.BOTH,callback=rotary_callback4)

# keep running
while True:
    time.sleep(0.1)
