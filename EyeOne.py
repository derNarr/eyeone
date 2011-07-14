#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# eyeone/EyeOne.py
#
# (c) 2010-2011 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# This file defines a class which implements the python adapted variable
# definitions and function prototypes of the EyeOne.h and the
# MeasurementConditions.h of the EyeOne SKD 3.4.3 from x-rite
#
# Maybe some Copyrights belongs to X-Rite Inc.
#
# last mod 2011-05-24, KS

from ctypes import cdll,c_int,c_long,c_float,c_char_p 
from exceptions import IOError, TypeError # if it fails to load dll

import EyeOneConstants

###########################################################
### Prototypes of exported functions (EyeOne.dll) BEGIN ###
###########################################################

# I don't really understand the errorhandling, so it is missing. TODO


class EyeOne(object):
    """
    encapsulates the functions of the EyeOne.dll.

    EyeOne gives you an object EyeOne with the following Methods
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

    def __init__(self, dummy=False):
        """
        loads runtime library (on win32 EyeOne.dll).

        If dummy=True, no runtime library is loaded. The EyeOne object
        behave very similar to a "real" object, but does not connect to
        the EyeOne and gives some artificial data.

        For now the dummy gives no error codes. So the dummy behaves as a
        EyeOne without any problems.
        """
        self.dummy = dummy

        if not self.dummy:
            try:
                self.eye_one = cdll.EyeOne
            except:
                raise(IOError, '''Cannot load EyeOne.dll. Please install
                        EyeOne.dll before running this again or use
                        EyeOne(dummy=True) to create EyeOne object.''')
            ## initialize c_functions and set prototypes
            # I1_IsConnected
            self.eye_one.I1_IsConnected.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_IsConnected.argtypes = []
            self.eye_one.I1_IsConnected.__doc__= self.I1_IsConnected.__doc__
            self.I1_IsConnected = self.eye_one.I1_IsConnected
            # I1_KeyPressed
            self.eye_one.I1_KeyPressed.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_KeyPressed.argtypes = []
            self.eye_one.I1_KeyPressed.__doc__= self.I1_KeyPressed.__doc__
            self.I1_KeyPressed = self.eye_one.I1_KeyPressed
            # I1_GetNumberOfAvailableSamples
            self.eye_one.I1_GetNumberOfAvailableSamples.restype = c_long
            self.eye_one.I1_GetNumberOfAvailableSamples.argtypes = []
            self.eye_one.I1_GetNumberOfAvailableSamples.__doc__= self.I1_GetNumberOfAvailableSamples.__doc__
            self.I1_GetNumberOfAvailableSamples = self.eye_one.I1_GetNumberOfAvailableSamples
            
            ## trigger measurements / calibrations
            # I1_Calibrate
            self.eye_one.I1_Calibrate.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_Calibrate.argtypes = []
            self.eye_one.I1_Calibrate.__doc__= self.I1_Calibrate.__doc__
            self.I1_Calibrate = self.eye_one.I1_Calibrate
            # I1_TriggerMeasurement
            self.eye_one.I1_TriggerMeasurement.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_TriggerMeasurement.argtypes = []
            self.eye_one.I1_TriggerMeasurement.__doc__= self.I1_TriggerMeasurement.__doc__
            self.I1_TriggerMeasurement = self.eye_one.I1_TriggerMeasurement
            # I1_GetSpectrum
            self.eye_one.I1_GetSpectrum.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_GetSpectrum.argtypes = [c_float * EyeOneConstants.SPECTRUM_SIZE, c_long]
            self.eye_one.I1_GetSpectrum.__doc__= self.I1_GetSpectrum.__doc__
            self.I1_GetSpectrum = self.eye_one.I1_GetSpectrum
            # I1_GetTriStimulus
            self.eye_one.I1_GetTriStimulus.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_GetTriStimulus.argtypes = [c_float * EyeOneConstants.TRISTIMULUS_SIZE, c_long]
            self.eye_one.I1_GetTriStimulus.__doc__= self.I1_GetTriStimulus.__doc__
            self.I1_GetTriStimulus = self.eye_one.I1_GetTriStimulus
            # I1_GetDensities
            self.eye_one.I1_GetDensities.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_GetDensities.argtypes = [c_float * EyeOneConstants.DENSITY_SIZE, c_long]
            self.eye_one.I1_GetDensities.__doc__= self.I1_GetDensities.__doc__
            self.I1_GetDensities = self.eye_one.I1_GetDensities
            # I1_SetSubstrate
            self.eye_one.I1_SetSubstrate.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_SetSubstrate.argtypes = [c_float * EyeOneConstants.SPECTRUM_SIZE, c_long]
            self.eye_one.I1_SetSubstrate.__doc__= self.I1_SetSubstrate.__doc__
            self.I1_SetSubstrate = self.eye_one.I1_SetSubstrate
            # I1_SetOption
            self.eye_one.I1_SetOption.restype = c_int #enum I1_ErrorType
            self.eye_one.I1_SetOption.argtypes = [c_char_p, c_char_p] #option/key, value
            self.eye_one.I1_SetOption.__doc__= self.I1_SetOption.__doc__
            self.I1_SetOption = self.eye_one.I1_SetOption
            # I1_GetOption
            self.eye_one.I1_GetOption.restype = c_char_p #value
            self.eye_one.I1_GetOption.argtypes = [c_char_p] #option/key
            self.eye_one.I1_GetOption.__doc__= self.I1_GetOption.__doc__
            self.I1_GetOption = self.eye_one.I1_GetOption

        else:
            # set standard values for dummy
            self.calibrated = False
            self.measurement_triggered = False


    ######################################################################
    ### function definitions below are only called if object is ##########
    ### initialized with dummy=True ######################################
    ####### doc-strings are also used for the dll-functions ##############
    ######################################################################
    def I1_IsConnected(self):
        """
        tests if the Eye One is connected.
        
        Returns enum I1_ErrorType (c_int). eNoError (0), if connected.
        eDeviceNotConnected (2), if no EyeOne is present.

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        return EyeOneConstants.eNoError

    def I1_KeyPressed(self):
        """
        tests if button has been pressed.
        
        Returns enum I1_ErrorType (c_int). eNoError (0), if button was
        pressed. eKeyNotPressed (4), if button was not pressed.

        For the dummy the button was always pressed.

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        return EyeOneConstants.eNoError

    def I1_GetNumberOfAvailableSamples(self):
        """
        returns amount of currently available samples (c_long).
        """
        #only called if self.dummy==True
        return c_long(10) #TODO change to plausible number

    def I1_Calibrate(self):
        """
        calibrates the Eye One.
        
        Returns enum I1_ErrorType (c_int). eNoError (0), if no error occurs
        during calibration.

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        self.calibrated = True
        return EyeOneConstants.eNoError

    def I1_TriggerMeasurement(self):
        """
        triggers a measurement.

        Triggers a measurement depending on the measurement mode set by
        I1_SetOption. If the measurement mode is set to I1_SINGLE_EMISSION
        or I1_SCANNING_REFLECTANCE it is necessary to calibrate the Eye-One
        before any measurement can be triggered. Use GetSpectrum(index),
        I1_GetTriStimulus(index) or I1_GetDensity(index) to fetch the
        result.
               
        Returns enum I1_ErrorType (c_int). eNoError (0), if no error occurs
        during calibration; eDeviceNotConnected (2), if no device is
        available; eDeviceNotCalibrated (3), if a (re)calibration is
        necessary.

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        if self.calibrated:
            self.measurement_triggered = True
            return EyeOneConstants.eNoError
        else:
            self.measurement_triggered = False
            return EyeOneConstants.eDeviceNotCalibrated


    def I1_GetSpectrum(self, spectrum, index):
        """
        gets the spectrum of a previous triggered measurement.

        Input: spectrum is a c_float array with SPECTRUM_SIZE elements.
        index is a c_int. The spectrum values are stored in the array.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs; eNoDataAvailable (8), if no measurement has been
        triggered or if the specified index is out of range.

        General remarks: Use 0 as Index, to fetch the result of a
        previously triggered single measurement. To fetch a result of a
        previously triggered scan, specify an index between 0 and
        (I1_GetNumberOfScannedSamples() - 1).

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        if not isinstance(spectrum, c_float * EyeOneConstants.SPECTRUM_SIZE):
            raise(TypeError, "spectrum has to be instance of c_float * SPECTRUM_SIZE")
        if self.measurement_triggered:
            return EyeOneConstants.eNoError
        else:
            return EyeOneConstants.eNoDataAvailable

    def I1_GetTriStimulus(self, tri_stimulus, index):
        """
        gets the color vector of a previous triggered measurement.

        Input: tri_stimulus is a c_float array with TRISTIMULUS_SIZE elements.
        index is a c_int. The color values are stored in the array.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs; eNoDataAvailable (8), if no measurement has been
        triggered or if the specified index is out of range.

        General remarks: Use 0 as Index, to fetch the result of a
        previously triggered single measurement. To fetch a result of a
        previously triggered scan, specify an index between 0 and
        (I1_GetNumberOfScannedSamples() - 1).

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        if not isinstance(tri_stimulus, c_float * EyeOneConstants.TRISTIMULUS_SIZE):
            raise(TypeError, "tri_stimulus has to be instance of c_float * TRISTIMULUS_SIZE")
        if self.measurement_triggered:
            return EyeOneConstants.eNoError
        else:
            return EyeOneConstants.eNoDataAvailable

    def I1_GetDensities(self, densities, index):
        """
        gets all the densities (cyan, magenta, yellow, black) of a previous
        triggered measurement.


        Input: densities is a c_float array with DENSITY_SIZE elements.
        index is a c_int. The color values are stored in the array.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs; eNoDataAvailable (8), if no measurement has been
        triggered or if the specified index is out of range.

        General remarks: Use 0 as Index, to fetch the result of a
        previously triggered single measurement. To fetch a result of a
        previously triggered scan, specify an index between 0 and
        (I1_GetNumberOfScannedSamples() - 1).

        If pxAutoDensity is not null, *pxAutoDensity will be set
        accordingly.

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        if not isinstance(densities, c_float * EyeOneConstants.DENSITY_SIZE):
            raise(TypeError, "densities has to be instance of c_float * DENSITY_SIZE")
        if self.measurement_triggered:
            return EyeOneConstants.eNoError
        else:
            return EyeOneConstants.eNoDataAvailable

    def I1_SetSubstrate(self, substrate_spectrum):
        """
        sets the substrate spectrum for density calculations.

        Input: substrate_spectrum is a c_float array with SPECTRUM_SIZE
        elements.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs.

        SetSubstrate(substrate_spectrum) has to be called before the first
        call of GetDensity().
        """
        #only called if self.dummy==True
        if not isinstance(substrate_spectrum, c_float * EyeOneConstants.SPECTRUM_SIZE):
            raise(TypeError, "substrate_spectrum has to be instance of c_float * SPECTRUM_SIZE")
        self.density_spectrum_set = True
        return EyeOneConstants.eNoError

    def I1_SetOption(self, option, value):
        """
        sets given option/key (c_char_p) to given value (c_char_p).
        
        Possible options (for SDK manual or EyeOneConstants.py for possible
        values):
        * COLOR_SPACE_KEY
        * ILLUMINATION_KEY
        * OBSERVER_KEY
        * DENSITY_STANDARD_KEY
        * DENSITY_FILTER_MODE_KEY
        * I1_MEASUREMENT_MODE (I1_SINGLE_EMISSION, I1_SINGLE_REFLECTANCE
                    (default), I1_SCANNING_REFLECTANCE)
        * I1_IS_RECOGNITION_ENABLED (I1_YES, I1_NO (default))                

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs.

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        #if not isinstance(option, c_char_p):
        #    raise(TypeError, "option has to be instance of c_char_p (ctypes)")
        #if not isinstance(value, c_char_p):
        #    raise(TypeError, "value has to be instance of c_char_p (ctypes)")
        # TODO implement options in dummy
        return EyeOneConstants.eNoError

    def I1_GetOption(self, option):
        """
        gets option/key (c_char_p).
        
        Possible options (for SDK manual or EyeOneConstants.py for possible
        values):
        * COLOR_SPACE_KEY
        * ILLUMINATION_KEY
        * OBSERVER_KEY
        * DENSITY_STANDARD_KEY
        * DENSITY_FILTER_MODE_KEY
        * I1_MEASUREMENT_MODE (I1_SINGLE_EMISSION, I1_SINGLE_REFLECTANCE
                    (default), I1_SCANNING_REFLECTANCE)
        * I1_IS_RECOGNITION_ENABLED (I1_YES, I1_NO (default))                

        Returns value (c_char_p).

        For details see EyeOneConstants.py
        """
        #only called if self.dummy==True
        #if not isinstance(option, c_char_p):
        #    raise(TypeError, "option has to be instance of c_char_p (ctypes)")
        # TODO implement options in dummy
        print("I1_GetOption return value always \"Undefined\" for dummy.")
        return c_char_p("Undefined") 


if __name__ == "__main__":
    try:
        eye_one = EyeOne()
    except IOError:
        print("EyeOne.dll NOT FOUND. Is the driver of Eye One installed?\nload dummy")
        eye_one = EyeOne(dummy=True)

    if eye_one.I1_IsConnected() == EyeOneConstants.eNoError:
        print("Eye One is connected")

    eye_one.I1_Calibrate()
    eye_one.I1_TriggerMeasurement()
    spectrum = (c_float * EyeOneConstants.SPECTRUM_SIZE)()
    eye_one.I1_GetSpectrum(spectrum, 0)
    print("This is a spectrum:")
    print([float(f) for f in spectrum])

   
