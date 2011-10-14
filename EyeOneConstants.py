#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# eyeone/EyeOneConstants.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# Maybe some Copyrights belong to X-Rite Inc.

"""
These are variable definitions  of the EyeOne.h and the
MeasurementConditions.h of the EyeOne SKD 3.4.3 from x-rite adapted for
python.
"""

#++++++++++++++++++++++ BEGIN -- MeasurementConditions.h ++++++++++++++++

#------------------------------------------------------------------------
#  definitions for string-constants used in MeasurementConditions
#------------------------------------------------------------------------

UNDEFINED                    = "Undefined"


  # Illumination 
ILLUMINATION_KEY             = "Colorimetric.Illumination"
ILLUMINATION_A               = "A"
ILLUMINATION_B               = "B"
ILLUMINATION_C               = "C"
ILLUMINATION_D50             = "D50"
ILLUMINATION_D55             = "D55"
ILLUMINATION_D65             = "D65"
ILLUMINATION_D75             = "D75"
ILLUMINATION_F2              = "F2"
ILLUMINATION_F7              = "F7"
ILLUMINATION_F11             = "F11"
ILLUMINATION_EMISSION        = "Emission"

  # Observer 
OBSERVER_KEY                 = "Colorimetric.Observer"
OBSERVER_TWO_DEGREE          = "TwoDegree"
OBSERVER_TEN_DEGREE          = "TenDegree"

  # WhiteBase 
WHITE_BASE_KEY               = "Colorimetric.WhiteBase"
WHITE_BASE_ABSOLUTE          = "Absolute"
WHITE_BASE_PAPER             = "Paper"
WHITE_BASE_AUTOMATIC         = "Automatic"
  
  # DensityStandard 
DENSITY_STANDARD_KEY         = "Colorimetric.DensityStandard"
DENSITY_STANDARD_DIN         = "DIN"
DENSITY_STANDARD_DINNB       = "DINNB"
DENSITY_STANDARD_ANSIA       = "ANSIA"
DENSITY_STANDARD_ANSIE       = "ANSIE"
DENSITY_STANDARD_ANSII       = "ANSII"
DENSITY_STANDARD_ANSIT       = "ANSIT"
DENSITY_STANDARD_SPI         = "SPI"

  # DensityFilterMode 
DENSITY_FILTER_MODE_KEY      = "Colorimetric.DensityFilterMode"
DENSITY_FILTER_MODE_BLACK    = "Black"
DENSITY_FILTER_MODE_CYAN     = "Cyan"
DENSITY_FILTER_MODE_MAGENTA  = "Magenta"
DENSITY_FILTER_MODE_YELLOW   = "Yellow"
DENSITY_FILTER_MODE_MAX      = "Max"
DENSITY_FILTER_MODE_AUTO     = "Auto"


  # Maximum / minimum wavelength 
WAVE_LENGTH_730              = "730nm"
WAVE_LENGTH_380              = "380nm"

  # ColorSpace 
COLOR_SPACE_KEY              = "ColorSpaceDescription.Type"
COLOR_SPACE_CIELab           = "CIELab"
COLOR_SPACE_CIELCh           = "CIELCh"
COLOR_SPACE_CIELuv           = "CIELuv"
COLOR_SPACE_CIELChuv         = "CIELChuv"
COLOR_SPACE_CIE_UV_Y1960     = "CIEuvY1960"
COLOR_SPACE_CIE_UV_Y1976     = "CIEuvY1976"
COLOR_SPACE_CIEXYZ           = "CIEXYZ"
COLOR_SPACE_CIExyY           = "CIExyY"

COLOR_SPACE_HunterLab        = "HunterLab"
COLOR_SPACE_RXRYRZ           = "RxRyRz"
COLOR_SPACE_LAB_MG           = "LABmg"
COLOR_SPACE_LCH_MG           = "LCHmg"
COLOR_SPACE_RGB              = "RGB"

SPECTRUM_SIZE                = 36
TRISTIMULUS_SIZE             = 3
DENSITY_SIZE                 = 4

#++++++++++++++++++++++ END -- MeasurementConditions.h ++++++++++++++++++


#++++++++++++++++++++++++ BEGIN -- EyeOne.h +++++++++++++++++++++++++++++

# definitions for specific EyeOne key/values used with I1_GetOption()
# general key/values
I1_LAST_ERROR                    = "LastError"
I1_EXTENDED_ERROR_INFORMATION    = "ExtendedErrorInformation"

I1_YES                           = "yes"
I1_NO                            = "no"

# EyeOne key/values 
I1_VERSION                       = "Version"
I1_MAJOR_VERSION                 = "MajorVersion"
I1_MINOR_VERSION                 = "MinorVersion"
I1_REVISION_VERSION              = "RevisionVersion"
I1_BUILD_VERSION                 = "BuildVersion"
I1_SERIAL_NUMBER                 = "SerialNumber"
I1_IS_CONNECTED                  = "Connection"
I1_IS_KEY_PRESSED                = "IsKeyPressed"
I1_IS_RECOGNITION_ENABLED        = "Recognition"
I1_LAST_CALIBRATION_TIME         = "LastCalibrationTime"
I1_CALIBRATION_COUNT             = "LastCalibrationCounter"
I1_NUMBER_OF_AVAILABLE_SAMPLES   = "AvailableSamples"
I1_AVAILABLE_MEASUREMENT_MODES   = "AvailableMeasurementModes"
I1_IS_BEEP_ENABLED               = "Beep"
I1_LAST_AUTO_DENSITY_FILTER      = "LastAutoDensityFilter"
I1_IS_ADAPTIVE_MODE_ENABLED      = "AdaptiveMode"
I1_IS_NETPROFILER_ENABLED        = "NetProfiler"
I1_INTEGRATION_TIME              = "IntegrationTime"

I1_PHYSICAL_FILTER               = "PhysicalFilter" # read only
I1_UNDEFINED_FILTER              = "0"    
I1_NO_FILTER                     = "1"
I1_UV_FILTER                     = "2"

I1_SCREEN_TYPE                   = "ScreenType"    # mandatory for i1-display
I1_LCD_SCREEN                    = "LCD"
I1_CRT_SCREEN                    = "CRT"

I1_PATCH_INTENSITY               = "PatchIntensity" # used with i1-display
I1_BLEAK                         = "Bleak"
I1_BRIGHT                        = "Bright"
I1_AUTO                          = "Auto"

I1_DEVICE_TYPE                   = "DeviceType"
I1_EYEONE                        = "EyeOne"      # this is the default device 
I1_EYEONE_1                      = "EyeOne1"     # this is the first alternative device found on the USB bus 
I1_EYEONE_2                      = "EyeOne2"     # ...  # all other definitions must be created on demand 
I1_EYEONE_127                    = "EyeOne127"   # this is the last device on the bus 
I1_DISPLAY                       = "EyeOneDisplay"

I1_DEVICE_SUBTYPE                = "DeviceSubType"
I1_REGULAR                       = "Regular"
I1_LT                            = "Lt"

I1_MEASUREMENT_MODE              = "MeasurementMode"
I1_SINGLE_EMISSION               = "SingleEmission"
I1_SINGLE_REFLECTANCE            = "SingleReflectance"
I1_SINGLE_AMBIENT_LIGHT          = "SingleAmbientLight"
I1_SCANNING_REFLECTANCE          = "ScanningReflectance"
I1_SCANNING_AMBIENT_LIGHT        = "ScanningAmbientLight"

I1_RESET                         = "Reset" # reset command parameters: I1_ALL, DeviceTypes, MeasurementModes
I1_ALL                           = "All"

# dirty implementation of one way enum I1_ErrorType BEGIN TODO
eNoError                         =  0      # no error 
eDeviceNotReady                  =  1      # device not ready	
eDeviceNotConnected              =  2      # device not connected	
eDeviceNotCalibrated             =  3      # device not calibrated 
eKeyNotPressed                   =  4      # if no key has been pressed 
eNoSubstrateWhite                =  5      # no substrate white reference set 
eWrongMeasureMode                =  6      # wrong measurement mode 
eStripRecognitionFailed          =  7      # if the measurement mode is set to scanning and recognition is enabled 
eNoDataAvailable                 =  8      # measurement not triggered, index out of range (scanning) 
eException                       =  9      # internal exception, use I1_GetOption(I1_LAST_ERROR) for more details 
eInvalidArgument                 = 10      # if a passed method argument is invalid (i.e. NULL) 
eUnknownError                    = 12      # unknown error occurred 
eWrongDeviceType                 = 13      # operation not supported by this device type 
I1_ADDITIONAL_ERRORS             = 14      # extend error types
# dirty enum END                   

# dirty implementation of one way enum I1_DeviceMessage BEGIN TODO
eDeviceButtonPressed             = 0       # key on device pressed 
eDeviceDisconnected              = 1       # device disconnected 
I1_ADDITIONAL_MESSAGES           = 2       # extend messages 
# dirty enum END


### NOTICE the prototypes of the function are in eyeone/EyeOne.py ###

#++++++++++++++++++++++ END -- EyeOne.h +++++++++++++++++++++++++++++++++



