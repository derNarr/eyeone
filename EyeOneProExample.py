#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# eyeone/EyeOneProExample.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-04-20, KS

import time

from ctypes import c_float
try:    # normal import, if eyeone module is installed correctly 
    from eyeone import EyeOneConstants
    from eyeone import EyeOne 
except:    # if you running this in the eyeone folder
    import EyeOneConstants
    import EyeOne

#from eyeone.EyeOne import EyeOne # looks a bit weard, but is correct (load 
                                 # the object EyeOne the submodule EyeOne 
                                 # out of the module EyeOne
EyeOne = EyeOne.EyeOne(dummy=True)

# Check if the EyeOne Pro is connected.
if (EyeOne.I1_IsConnected() == EyeOneConstants.eNoError):
    print("Eye-One ist verbunden...")
else:
    print("Keine Verbindung gefunden...")

# Print version and serial number of the EyeOne Pro
print("SDK_Version: " +
        str(EyeOne.I1_GetOption("Version")))
print("Device serial number: " +
        str(EyeOne.I1_GetOption("SerialNumber")) + "\n")

if(EyeOne.I1_SetOption(EyeOneConstants.I1_MEASUREMENT_MODE, 
    EyeOneConstants.I1_SINGLE_EMISSION) ==
        EyeOneConstants.eNoError):
    print("measurement mode set to single emission.")
else:
    print("failed to set measurement mode.")

# Set the Colorspace
if(EyeOne.I1_SetOption(EyeOneConstants.COLOR_SPACE_KEY, 
    EyeOneConstants.COLOR_SPACE_RGB) ==
        EyeOneConstants.eNoError):
    print("color space set to RGB.")
else:
    print("failed to set color space.")


## Calibration

print("\nPlease put the EyeOne-Pro on the calibration plate and press the \
key to start calibration.")
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)
if (EyeOne.I1_Calibrate() == EyeOneConstants.eNoError):
    print("calibration done.")
else:
    print("calibration failed.")

## Initilizing some variables to retrive mesuarments.

# (c_float * EyeOneConstants.TRISTIMULUS_SIZE) creates an _ctypes.ArrayType
# object, wich has to be called to initilize one
# __main__.c_float_Array_TRIESTIMULUS_SIZE object.
# For more details see the ctypes documentation.
colorspace = (c_float * EyeOneConstants.TRISTIMULUS_SIZE)()
spectrum = (c_float * EyeOneConstants.SPECTRUM_SIZE)()

# Trigger measurement and retrive spectrum and colorspace.
print("\nPlease put the EyeOne-Pro in measurement position and press the \
key to start measurement.")
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)
if(EyeOne.I1_TriggerMeasurement() != EyeOneConstants.eNoError):
    print("Measurement failed.")
if(EyeOne.I1_GetSpectrum(spectrum, 0) != EyeOneConstants.eNoError):
    print("Failed to get spectrum.")
if(EyeOne.I1_GetTriStimulus(colorspace, 0) != EyeOneConstants.eNoError):
    print("Failed to get colorspace.")
    
# print colorspace and spectrum

print("RGB values are: " + str(colorspace[:]) + "\n")
print("Spectrum:\n" + str(spectrum[:]))

# try to plot spectrum with pylab/matplotlib
try:
    from pylab import plot,show,xlabel,ylabel
    xlabel("mesuament points (presumably wavelength)")
    ylabel("intesity")
    plot(spectrum, "go-")
    show() #does not return in idle
except:
    print("pylab not installed -- no plotting")

time.sleep(1)

