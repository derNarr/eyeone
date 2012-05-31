#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# eyeone/eyeone.py
#
# (c) 2010-2012 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: (1) class EyeOne
#
# input: --
# output: --
#
# created --
# last mod 2012-05-31 13:09 KS
#
# This file defines a class which implements the python adapted variable
# definitions and function prototypes of the EyeOne.h and the
# MeasurementConditions.h of the EyeOne SKD 3.4.3 from x-rite
#
# Maybe some Copyrights belongs to X-Rite Inc.

from ctypes import cdll, c_int, c_long, c_float, c_char_p
import time
import random
#from exceptions import OSError, ImportError, BaseException, KeyError
# if it fails to load dll

import constants

###########################################################
### Prototypes of exported functions (EyeOne.dll) BEGIN ###
###########################################################

# I don't if it is possible to implement the callback the error handling ,
# so it is missing. TODO


class EyeOne(object):
    """
    Encapsulates the functions of EyeOne.dll.

    EyeOne gives you an object eyeone with the following methods
    available. For the methods ctypes prototypes are defined.

    * I1_IsConnected -- checks if EyeOne Pro is connected
    * I1_KeyPressed -- checks if key on EyeOne Pro has been pressed
    * I1_GetNumberOfAvailableSamples
    * I1_Calibrate -- triggers calibration
    * I1_TriggerMeasurement -- triggers measurement
    * I1_GetSpectrum -- gets spectrum
    * I1_GetTriStimulus -- gets color vector
    * I1_GetDensities
    * I1_SetSubstrate
    * I1_SetOption -- sets options
    * I1_GetOption -- gets options

    Additionally there are some method for convenience:

        calibrate : calibrates the EyeOne
        is_calibrated : bool, which states if the eyeone is calibrated
    """

    def __init__(self, dummy=False):
        """
        Loads runtime library (on win32 EyeOne.dll).

        If dummy=True, no runtime library is loaded. The EyeOne object
        behaves very similar to a "real" object, but does not connect to
        EyeOne Pro and gives some artificial data.

        For now the dummy gives no error codes. So the dummy behaves as a
        EyeOne Pro without any problems.
        """
        self.dummy = dummy
        self.is_calibrated = False

        try:
            if self.dummy is True:
                raise BaseException()
            self.eyeone = cdll.EyeOne
            ## initialize c_functions and set prototypes
            # I1_IsConnected
            self.eyeone.I1_IsConnected.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_IsConnected.argtypes = []
            self.eyeone.I1_IsConnected.__doc__ = self.I1_IsConnected.__doc__
            self.I1_IsConnected = self.eyeone.I1_IsConnected
            # I1_KeyPressed
            self.eyeone.I1_KeyPressed.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_KeyPressed.argtypes = []
            self.eyeone.I1_KeyPressed.__doc__ = self.I1_KeyPressed.__doc__
            self.I1_KeyPressed = self.eyeone.I1_KeyPressed
            # I1_GetNumberOfAvailableSamples
            self.eyeone.I1_GetNumberOfAvailableSamples.restype = c_long
            self.eyeone.I1_GetNumberOfAvailableSamples.argtypes = []
            self.eyeone.I1_GetNumberOfAvailableSamples.__doc__ = \
                    self.I1_GetNumberOfAvailableSamples.__doc__
            self.I1_GetNumberOfAvailableSamples = \
                    self.eyeone.I1_GetNumberOfAvailableSamples
            
            ## trigger measurements / calibrations
            # I1_Calibrate
            self.eyeone.I1_Calibrate.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_Calibrate.argtypes = []
            self.eyeone.I1_Calibrate.__doc__ = self.I1_Calibrate.__doc__
            self.I1_Calibrate = self.eyeone.I1_Calibrate
            # I1_TriggerMeasurement
            self.eyeone.I1_TriggerMeasurement.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_TriggerMeasurement.argtypes = []
            self.eyeone.I1_TriggerMeasurement.__doc__ = \
                    self.I1_TriggerMeasurement.__doc__
            self.I1_TriggerMeasurement = self.eyeone.I1_TriggerMeasurement
            # I1_GetSpectrum
            self.eyeone.I1_GetSpectrum.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_GetSpectrum.argtypes = \
                    [c_float * constants.SPECTRUM_SIZE, c_long]
            self.eyeone.I1_GetSpectrum.__doc__ = self.I1_GetSpectrum.__doc__
            self.I1_GetSpectrum = self.eyeone.I1_GetSpectrum
            # I1_GetTriStimulus
            self.eyeone.I1_GetTriStimulus.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_GetTriStimulus.argtypes = \
                    [c_float * constants.TRISTIMULUS_SIZE, c_long]
            self.eyeone.I1_GetTriStimulus.__doc__ = \
                    self.I1_GetTriStimulus.__doc__
            self.I1_GetTriStimulus = self.eyeone.I1_GetTriStimulus
            # I1_GetDensities
            self.eyeone.I1_GetDensities.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_GetDensities.argtypes = \
                    [c_float * constants.DENSITY_SIZE, c_long]
            self.eyeone.I1_GetDensities.__doc__ = \
                    self.I1_GetDensities.__doc__
            self.I1_GetDensities = self.eyeone.I1_GetDensities
            # I1_SetSubstrate
            self.eyeone.I1_SetSubstrate.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_SetSubstrate.argtypes = \
                    [c_float * constants.SPECTRUM_SIZE, c_long]
            self.eyeone.I1_SetSubstrate.__doc__ = \
                    self.I1_SetSubstrate.__doc__
            self.I1_SetSubstrate = self.eyeone.I1_SetSubstrate
            # I1_SetOption
            self.eyeone.I1_SetOption.restype = c_int #enum I1_ErrorType
            self.eyeone.I1_SetOption.argtypes = \
                    [c_char_p, c_char_p] #option/key, value
            self.eyeone.I1_SetOption.__doc__ = self.I1_SetOption.__doc__
            self.I1_SetOption = self.eyeone.I1_SetOption
            # I1_GetOption
            self.eyeone.I1_GetOption.restype = c_char_p #value
            self.eyeone.I1_GetOption.argtypes = [c_char_p] #option/key
            self.eyeone.I1_GetOption.__doc__ = self.I1_GetOption.__doc__
            self.I1_GetOption = self.eyeone.I1_GetOption

        except(OSError, ImportError, BaseException): 
            print('''
                  ##################### WARNING ####################
                  # Cannot load EyeOne.dll. Creating EyeOne dummy! #
                  ##################################################
                  ''')
            # set standard values for dummy
            self.calibrated = False
            self.measurement_triggered = False
            self.options = dict()


    ######################################################################
    ### function definitions below are only called if object is ##########
    ### initialized with dummy=True ######################################
    ####### doc-strings are also used for the dll-functions ##############
    ######################################################################
    def I1_IsConnected(self):
        """
        Tests if EyeOne Pro is connected.
        
        Returns enum I1_ErrorType (c_int). eNoError (0), if connected.
        eDeviceNotConnected (2), if no EyeOne Pro is present.

        For details see constants.py
        """
        # only called if self.dummy==True
        return constants.eNoError

    def I1_KeyPressed(self):
        """
        Tests if key has been pressed.
        
        Returns enum I1_ErrorType (c_int). eNoError (0), if button was
        pressed. eKeyNotPressed (4), if button was not pressed.

        For dummy key stays always pressed.

        For details see constants.py
        """
        #only called if self.dummy==True
        return constants.eNoError

    def I1_GetNumberOfAvailableSamples(self):
        """
        Returns amount of currently available samples (c_long).
        """
        #only called if self.dummy==True
        return c_long(10) #TODO change to plausible number

    def I1_Calibrate(self):
        """
        Calibrates EyeOne Pro.
        
        Returns enum I1_ErrorType (c_int). eNoError (0), if no error occurs
        during calibration.

        For details see constants.py
        """
        # only called if self.dummy==True
        self.calibrated = True
        return constants.eNoError

    def I1_TriggerMeasurement(self):
        """
        Triggers measurement.

        Triggers measurement depending on measurement mode set by
        I1_SetOption. If measurement mode is set to I1_SINGLE_EMISSION or
        I1_SCANNING_REFLECTANCE it is necessary to calibrate the EyeOne Pro
        before any measurement can be triggered. Use GetSpectrum(index),
        I1_GetTriStimulus(index) or I1_GetDensity(index) to fetch result.
               
        Returns enum I1_ErrorType (c_int). eNoError (0), if no error occurs
        during calibration; eDeviceNotConnected (2), if no device is
        available; eDeviceNotCalibrated (3), if a (re)calibration is
        necessary.

        For details see constants.py
        """
        #only called if self.dummy==True
        if self.calibrated:
            self.measurement_triggered = True
            return constants.eNoError
        else:
            self.measurement_triggered = False
            return constants.eDeviceNotCalibrated


    def I1_GetSpectrum(self, spectrum, index):
        """
        Gets spectrum of a previous triggered measurement.

        Input: spectrum is a c_float array with SPECTRUM_SIZE elements.
        index is a c_int. Spectrum values are stored in array.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs; eNoDataAvailable (8), if no measurement has been
        triggered or if specified index is out of range.

        General remarks: Use 0 as Index to fetch the result of a
        previously triggered single measurement. To fetch a result of a
        previously triggered scan specify an index between 0 and
        (I1_GetNumberOfScannedSamples() - 1).

        For details see constants.py
        """
        # only called if self.dummy==True
        if not isinstance(spectrum, c_float * constants.SPECTRUM_SIZE):
            raise TypeError('''spectrum has to be instance of c_float *
            SPECTRUM_SIZE''')
        if self.measurement_triggered:
            spectrum[:] = [random.uniform(0, 1) for i in
                    range(constants.SPECTRUM_SIZE)]
            return constants.eNoError
        else:
            return constants.eNoDataAvailable

    def I1_GetTriStimulus(self, tri_stimulus, index):
        """
        Gets color vector of a previously triggered measurement.

        Input: tri_stimulus is a c_float array with TRISTIMULUS_SIZE
        elements. index is a c_int. Color values are stored in array.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs; eNoDataAvailable (8), if no measurement has been
        triggered or if specified index is out of range.

        General remarks: Use 0 as Index to fetch the result of a
        previously triggered single measurement. To fetch a result of a
        previously triggered scan specify an index between 0 and
        (I1_GetNumberOfScannedSamples() - 1).

        For details see constants.py
        """
        # only called if self.dummy==True
        if not isinstance(tri_stimulus,
                c_float * constants.TRISTIMULUS_SIZE):
            raise TypeError('''tri_stimulus has to be instance of c_float *
            TRISTIMULUS_SIZE''')
        if self.measurement_triggered:
            tri_stimulus[:] = [random.uniform(0, 1) for i in
                    range(constants.TRISTIMULUS_SIZE)]
            return constants.eNoError
        else:
            return constants.eNoDataAvailable

    def I1_GetDensities(self, densities, index):
        """
        Gets all densities (cyan, magenta, yellow, black) of a previous
        triggered measurement.

        Input: densities is a c_float array with DENSITY_SIZE elements.
        index is a c_int. Color values are stored in array.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs; eNoDataAvailable (8), if no measurement has been
        triggered or if specified index is out of range.

        General remarks: Use 0 as index to fetch the result of a
        previously triggered single measurement. To fetch a result of a
        previously triggered scan specify an index between 0 and
        (I1_GetNumberOfScannedSamples() - 1).

        If pxAutoDensity is not null, \*pxAutoDensity will be set
        accordingly.

        For details see constants.py
        """
        # only called if self.dummy==True
        if not isinstance(densities, c_float *
                constants.DENSITY_SIZE):
            raise TypeError('''densities has to be instance of c_float *
            DENSITY_SIZE''')
        if self.measurement_triggered:
            return constants.eNoError
        else:
            return constants.eNoDataAvailable

    def I1_SetSubstrate(self, substrate_spectrum):
        """
        Sets substrate spectrum for density calculations.

        Input: substrate_spectrum is a c_float array with SPECTRUM_SIZE
        elements.

        Returns enum I1_ErrorType (c_int). eNoError (0), if no error
        occurs.

        SetSubstrate(substrate_spectrum) has to be called before the first
        call of GetDensity().
        """
        # only called if self.dummy==True
        if not isinstance(substrate_spectrum, c_float *
                constants.SPECTRUM_SIZE):
            raise TypeError('''substrate_spectrum has to be instance of
            c_float * SPECTRUM_SIZE''')
        self.density_spectrum_set = True
        return constants.eNoError

    def I1_SetOption(self, option, value):
        """
        Sets given option/key (c_char_p) to given value (c_char_p).
        
        Possible options (see SDK manual or constants.py for possible
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

        For details see constants.py
        """
        # only called if self.dummy==True
        if not isinstance(value, c_char_p):
            value = c_char_p(value)
        if isinstance(option, c_char_p):
            self.options[option.value] = value
        return constants.eNoError

    def I1_GetOption(self, option):
        """
        Gets option/key (c_char_p).
        
        Possible options (see SDK manual or constants.py for possible
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

        For details see constants.py
        """
        # only called if self.dummy==True
        if not isinstance(option, c_char_p):
            option = c_char_p(option)
        try:
            return self.options[option.value]
        except KeyError:
            print("WARNING: option might not be there in a real eyeone")
            print('''If option is not set explicitly, I1_GetOption returns
                    "Undefined" in dummy mode.''')
            return c_char_p("Undefined") 

    def calibrate(self, measurement_mode=constants.I1_SINGLE_EMISSION,
            color_space=constants.COLOR_SPACE_CIExyY, 
            final_prompt="\nPlease put EyeOne-Pro in measurement position"
            + "and hit button to start measurement."):
        """
        Sets EyeOne Pro to measurement mode and color space measurement
        mode and calibrates EyeOne Pro for use.

        :Parameters:

            measurement_mode : *eyeone.constants.I1_SINGLE_EMISSION* 
                or other string defined in eyeone.constants
            color_space : *eyeone.constants.COLOR_SPACE_CIExyY*
                or other string defined in eyeone.constants
            final_prompt : string or None
                the final prompt is printed to stdout in the end and the
                EyeOne waits for a button press. If None nothing is printed
                and EyeOne do not wait for button press.

        If successful, method returns True, otherwise False. Check also the
        attribute EyeOne.is_calibrated. It stores a boolean, which is True,
        when the EyeOne is already calibrated.

        """
        # set EyeOne Pro variables
        if(self.I1_SetOption(constants.I1_MEASUREMENT_MODE,
            measurement_mode) == constants.eNoError):
            print("Measurement mode set to " + measurement_mode + ".")
        else:
            print("Failed to set measurement mode.")
            return False
        if(self.I1_SetOption(COLOR_SPACE_KEY, color_space) == eNoError):
            print("Color space set to " + color_space + ".")
        else:
            print("Failed to set color space.")
            return False
        # calibrate EyeOne Pro
        print("\nPlease put EyeOne Pro on calibration plate and "
        + "press key to start calibration.")
        while(self.I1_KeyPressed() != eNoError):
            time.sleep(0.01)
        if (self.I1_Calibrate() == eNoError):
            print("Calibration of EyeOne Pro done.")
        else:
            print("Calibration of EyeOne Pro failed. Please RESTART "
            + "calibration")
            return False
        self.is_calibrated = True
        if final_prompt == None:
            return True
        # prompt for click on button of EyeOne Pro
        print(final_prompt)
        while(eyeone.I1_KeyPressed() != eNoError):
            time.sleep(0.01)
        return True


if __name__ == "__main__":
    try:
        eyeone = EyeOne()
    except IOError:
        print('''EyeOne.dll NOT FOUND. Is driver of EyeOne Pro
        installed?\nLoad dummy.''')
        eyeone = EyeOne(dummy=True)

    if eyeone.I1_IsConnected() == constants.eNoError:
        print("EyeOne Pro is connected.")

    eyeone.I1_Calibrate()
    eyeone.I1_TriggerMeasurement()
    spectrum = (c_float * constants.SPECTRUM_SIZE)()
    eyeone.I1_GetSpectrum(spectrum, 0)
    print("This is a spectrum:")
    print([float(f) for f in spectrum])

