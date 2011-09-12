<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# eyeone/EyeOneProExample.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)

import time

from ctypes import c_float
try:    # normal import, if eyeone module is installed correctly 
    from eyeone import EyeOneConstants
    from eyeone import EyeOne 
except:    # if you running this in the eyeone folder
    import EyeOneConstants
    import EyeOne

# from eyeone.EyeOne import EyeOne # looks a bit weird, but is correct (load 
                                   # the object EyeOne the submodule EyeOne 
                                   # out of the module EyeOne
EyeOne = EyeOne.EyeOne(dummy=True)

# Check if EyeOne Pro is connected.
if (EyeOne.I1_IsConnected() == EyeOneConstants.eNoError):
    print("EyeOne Pro is connected.")
else:
    print("Connection could not be found.")

# Print version and serial number of EyeOne Pro
print("SDK_Version: " +
        str(EyeOne.I1_GetOption("Version")))
print("Device serial number: " +
        str(EyeOne.I1_GetOption("SerialNumber")) + "\n")

if(EyeOne.I1_SetOption(EyeOneConstants.I1_MEASUREMENT_MODE, 
    EyeOneConstants.I1_SINGLE_EMISSION) ==
        EyeOneConstants.eNoError):
    print("Measurement mode set to single emission.")
else:
    print("Failed to set measurement mode.")

# Set color space
if(EyeOne.I1_SetOption(EyeOneConstants.COLOR_SPACE_KEY, 
    EyeOneConstants.COLOR_SPACE_RGB) ==
        EyeOneConstants.eNoError):
    print("Color space set to RGB.")
else:
    print("Failed to set color space.")


## Calibration

print("\nPlease put EyeOne Pro on calibration plate and press \
key to start calibration.")
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)
if (EyeOne.I1_Calibrate() == EyeOneConstants.eNoError):
    print("Calibration done.")
else:
    print("Calibration failed.")

## Initializing some variables to retrieve measurements.

# (c_float * EyeOneConstants.TRISTIMULUS_SIZE) creates an _ctypes.ArrayType
# object, wich has to be called to initialize one
# __main__.c_float_Array_TRIESTIMULUS_SIZE object.
# For more details see ctypes documentation.
colorspace = (c_float * EyeOneConstants.TRISTIMULUS_SIZE)()
spectrum = (c_float * EyeOneConstants.SPECTRUM_SIZE)()

# Trigger measurement and retrieve spectrum and color space.
print("\nPlease put EyeOne Pro in measurement position and press \
key to start measurement.")
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)
if(EyeOne.I1_TriggerMeasurement() != EyeOneConstants.eNoError):
    print("Measurement failed.")
if(EyeOne.I1_GetSpectrum(spectrum, 0) != EyeOneConstants.eNoError):
    print("Failed to get spectrum.")
if(EyeOne.I1_GetTriStimulus(colorspace, 0) != EyeOneConstants.eNoError):
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

