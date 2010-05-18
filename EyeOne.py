#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# EyeOne/EyeOne.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# This are for python adapted variable definitions of the EyeOne.h and the
# MeasurementConditions.h of the EyeOne SKD 3.4.3 from x-rite
#
# Maybe some Copyrights belongs to X-Rite Inc.
#
# last mod 2010-04-20, KS

"""
EyeOne.py gives you an object EyeOne with the following Methods
available. For the methods there are ctypes prototypes defined.
- I1_IsConnected -- checks if the EyeOne is connected
- I1_KeyPressed -- checks if the button on the EyeOne has been pressed
- I1_GetNumberOfAvailableSamples
- I1_Calibrate -- triggers calibration
- I1_TriggerMeasurement -- triggers measurement
- I1_GetSpectrum -- get the spectrum
- I1_GetTriStimulus -- get the colorvector
- I1_GetDensities
- I1_SetSubstrate
- I1_SetOption -- set options
- I1_GetOption -- get options
"""

from ctypes import cdll,c_int,c_long,c_float,c_char_p 
from exceptions import IOError # if it fails to load dll

import EyeOneConstants

###########################################################
### Prototypes of exported functions (EyeOne.dll) BEGIN ###
###########################################################

# I don't really understand the errorhandling, so it is missing. TODO

try:
    EyeOne = cdll.EyeOne
except:
    print("Failed to load EyeOne.dll.")
    print("Please install EyeOne.dll before running this again.")
    raise(IOError, "Cannot load EyeOne.dll")



### Information about driver and API ###

#Test if the Eye-One is connected
#return eNoError (0) if connected
#return eDeviceNotConnected (2) if no Eye-One is present
EyeOne.I1_IsConnected.restype = c_int #enum I1_ErrorType
EyeOne.I1_IsConnected.argtypes = []

#Test if the button has been pressed
#return eNoError (0) if button was pressed
#return eKeyNotPressed (4) if button was not pressed
EyeOne.I1_KeyPressed.restype = c_int #enum I1_ErrorType
EyeOne.I1_KeyPressed.argtypes = []

#returns amount of currently available samples 
EyeOne.I1_GetNumberOfAvailableSamples.restype = c_long
EyeOne.I1_GetNumberOfAvailableSamples.argtypes = []


### trigger measurements / calibrations ###

#Calibrate the Eye-One
EyeOne.I1_Calibrate.restype = c_int #enum I1_ErrorType
EyeOne.I1_Calibrate.argtypes = []

#Trigger measurement
#
#Triggers a meausrement depending on the measurement mode set by I1_SetOption
#If the measurement mode is set to I1_SINGLE_EMISSION or I1_SCANNING_REFLECTANCE it is necessary
#to calibrate the Eye-One before any measurement can be triggered
#
#use GetSpectrum(index), I1_GetTriStimulus(index) or I1_GetDensity(index) to fetch the result
#
#returns eDeviceNotConnected (2) if no device is available
#returns eDeviceNotCalibrated (3) if a (re)calibration is necessary
EyeOne.I1_TriggerMeasurement.restype = c_int #enum I1_ErrorType
EyeOne.I1_TriggerMeasurement.argtypes = []


### get samples ### 

#General remarks:
#Use 0 as Index, to fetch the result of a previously triggered single measurement
#To fetch a result of a previously triggered scan, specify an index between 0 - (I1_GetNumberOfScannedSamples() - 1)
#If no measurement has been triggered or if the specified index is out of range eNoDataAvailable is returned

#Get the spectrum of a previous triggered measurement 
EyeOne.I1_GetSpectrum.restype = c_int #enum I1_ErrorType
EyeOne.I1_GetSpectrum.argtypes = [c_float * EyeOneConstants.SPECTRUM_SIZE, c_long]

#Get the color vector of a previous triggered measurement 
EyeOne.I1_GetTriStimulus.restype = c_int #enum I1_ErrorType
EyeOne.I1_GetTriStimulus.argtypes = [c_float * EyeOneConstants.TRISTIMULUS_SIZE, c_long]

#Get the all densities (cyan, magenta, yellow, black) of a previous triggered measurement 
#if pxAutoDensity is not null, *pxAutoDensity will be set accordingly
EyeOne.I1_GetDensities.restype = c_int #enum I1_ErrorType
EyeOne.I1_GetDensities.argtypes = [c_float * EyeOneConstants.DENSITY_SIZE, c_long]


### special functions for Density ###

#Set the substrate spectrum for density calculations
#This method has to be called before the first call to GetDensity()
EyeOne.I1_SetSubstrate.restype = c_int #enum I1_ErrorType
EyeOne.I1_SetSubstrate.argtypes = [c_float * EyeOneConstants.SPECTRUM_SIZE]


### setting measurement mode & conditions ### 

#possible options (see MeasurementConditions.h for possible values)
#COLOR_SPACE_KEY
#ILLUMINATION_KEY
#OBSERVER_KEY
#DENSITY_STANDARD_KEY
#DENSITY_FILTER_MODE_KEY
#
#I1_MEASUREMENT_MODE, possible values : I1_SINGLE_EMISSION, I1_SINGLE_REFLECTANCE, I1_SCANNING_REFLECTANCE
#default: I1_SCANNING_REFLECTANCE
#I1_IS_RECOGNITION_ENABLED, possible values : I1_YES, I1_NO, default : I1_NO
EyeOne.I1_SetOption.restype = c_int #enum I1_ErrorType
EyeOne.I1_SetOption.argtypes = [c_char_p, c_char_p] #key, value

EyeOne.I1_GetOption.restype = c_char_p
EyeOne.I1_GetOption.argtypes = [c_char_p] #key

#########################################################
### Prototypes of exported functions (EyeOne.dll) END ###
#########################################################

#++++++++++++++++++++++ END -- EyeOne.h +++++++++++++++++++++++++++++++++

