""" ESC/POS Exceptions classes """

import os

class Error(Exception):
    """ Base class for ESC/POS errors """
    def __init__(self, msg, status=None):
        Exception.__init__(self)
        self.msg = msg
        self.resultcode = 1
        if status is not None:
            self.resultcode = status

    def __str__(self):
        return self.msg

# Result/Exit codes
# 0  = success
# 10 = No Barcode type defined
# 15 = Barcode Length Error
# 20 = Barcode size values are out of range
# 30 = Barcode text not supplied
# 40 = Image height is too large
# 50 = No string supplied to be printed
# 60 = Invalid pin to send Cash Drawer pulse
# 70 = Invalid number of tab positions
# 80 = Invalid char code


class BarcodeTypeError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 10

    def __str__(self):
        return "No Barcode type is defined"

class BarcodeLenError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 15

    def __str__(self):
        return "Barcode length is not ok. Must be "+self.msg

class BarcodeRangeError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 16

    def __str__(self):
        return "Undefined Barcode Range"

class BarcodeSizeError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 20

    def __str__(self):
        return "Barcode size is out of range"

class BarcodeCodeError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 30

    def __str__(self):
        return "Code was not supplied"

class ImageSizeError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 40

    def __str__(self):
        return "Image height is longer than 255px and can't be printed"

class TextError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 50

    def __str__(self):
        return "Text string must be supplied to the text() method"


class CashDrawerError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 60

    def __str__(self):
        return "Valid pin must be set to send pulse"


class TabError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 70

    def __str__(self):
        return "Valid tab positions must be in the range 0 to 16"


class CharCodeError(Error):
    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 80

    def __str__(self):
        return "Valid char code must be set"