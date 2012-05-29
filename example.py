#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# eyeone/example.py
#
# (c) 2010-2012 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created --
# last mod 2012-05-29 KS

import time

from ctypes import c_float
try:    # normal import, if eyeone module is installed correctly
    from eyeone import constants
    from eyeone import eyeone
except:    # if you running this in the eyeone folder
    import constants
    import eyeone

# from eyeone.eyeone import EyeOne # looks a bit weird, but is correct (load
                                   # the object eyeone the submodule eyeone
                                   # out of the module eyeone
eyeone = eyeone.EyeOne(dummy=True)

# Check if eyeone Pro is connected.
if (eyeone.I1_IsConnected() == constants.eNoError):
    print("eyeone Pro is connected.")
else:
    print("Connection could not be found.")

# Print version and serial number of eyeone Pro
print("SDK_Version: " +
        str(eyeone.I1_GetOption("Version")))
print("Device serial number: " +
        str(eyeone.I1_GetOption("SerialNumber")) + "\n")

if(eyeone.I1_SetOption(constants.I1_MEASUREMENT_MODE,
    constants.I1_SINGLE_EMISSION) ==
        constants.eNoError):
    print("Measurement mode set to single emission.")
else:
    print("Failed to set measurement mode.")

# Set color space
if(eyeone.I1_SetOption(constants.COLOR_SPACE_KEY,
    constants.COLOR_SPACE_RGB) ==
        constants.eNoError):
    print("Color space set to RGB.")
else:
    print("Failed to set color space.")


## Calibration

print("\nPlease put eyeone Pro on calibration plate and press \
key to start calibration.")
while(eyeone.I1_KeyPressed() != constants.eNoError):
    time.sleep(0.1)
if (eyeone.I1_Calibrate() == constants.eNoError):
    print("Calibration done.")
else:
    print("Calibration failed.")

## Initializing some variables to retrieve measurements.

# (c_float * constants.TRISTIMULUS_SIZE) creates an _ctypes.ArrayType
# object, wich has to be called to initialize one
# __main__.c_float_Array_TRIESTIMULUS_SIZE object.
# For more details see ctypes documentation.
colorspace = (c_float * constants.TRISTIMULUS_SIZE)()
spectrum = (c_float * constants.SPECTRUM_SIZE)()

# Trigger measurement and retrieve spectrum and color space.
print("\nPlease put eyeone Pro in measurement position and press \
key to start measurement.")
while(eyeone.I1_KeyPressed() != constants.eNoError):
    time.sleep(0.1)
if(eyeone.I1_TriggerMeasurement() != constants.eNoError):
    print("Measurement failed.")
if(eyeone.I1_GetSpectrum(spectrum, 0) != constants.eNoError):
    print("Failed to get spectrum.")
if(eyeone.I1_GetTriStimulus(colorspace, 0) != constants.eNoError):
    print("Failed to get color space.")

# print color space and spectrum

print("RGB values: " + str(colorspace[:]) + "\n")
print("Spectrum:\n" + str(spectrum[:]))

# try to plot spectrum with pylab/matplotlib
try:
    from pylab import plot,show,xlabel,ylabel
    xlabel("Measurement points (presumably wavelength)")
    ylabel("Intensity")
    plot(spectrum, "Go-")
    show() # does not return in idle
except:
    print("pylab is not installed -- no plotting.")

time.sleep(1)

