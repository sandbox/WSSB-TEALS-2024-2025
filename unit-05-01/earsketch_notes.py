# Earsketch notes

##
## Unit 1: Example video
##


##
## 1.1 Components
##

# Content Manager (left): Your scripts and sounds

# DAW (top-center): The song timeline and "play" button
## Digital Audio Workstation, is software that produces 
## or edits audio on a computer, be it in a professional
## studio or in home laptop-based studios.

# Editor (mid-center): The code editor and "run" button

# Console (bottom-center): The script output and errors


##
## 1.2 Intro Script / Create new account
## 

# Intro Script: This code adds one sound to the DAW

# Setup Section
from earsketch import *
setTempo(120)

# Music Section
fitMedia(TECHNO_SYNTHPLUCK_001, 1, 1, 9)


##
## 1.3 fitMedia()
##

## 4 parameters:
# Sound: the sound constant from the sound browser
# Track: the track number
# Start: the starting measure
# End: the ending measure

## fitMedia() example:
fitMedia(Y18_DRUM_SAMPLES_2, 2, 1, 5)

## Example 1
# Setup
from earsketch import *
setTempo(120)
# Music
fitMedia(Y18_DRUM_SAMPLES_2, 1, 1, 5)

## Practice
# Using sounds that you like:
# Place sounds on two different tracks
# Place sounds from measure 2 to 12
# Create a short song with three tracks that is eight measures long or more

###
### Lab 5.01
###

## https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/units/5_unit/01_lesson/lab.md.html

## Beats
DUBSTEP_BASS_WOBBLE_007
DUBSTEP_PAD_003
DUBSTEP_DRUMLOOP_MAIN_005
DUBSTEP_LEAD_004