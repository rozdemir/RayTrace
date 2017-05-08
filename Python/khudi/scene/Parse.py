#!/usr/bin/env python
""" generated source for module Parse """
from __future__ import print_function
# package: khudi.scene
# 
#  * @section DESCRIPTION
#  *
#  * The Parse Class class.
#  *
#  
class Parse(object):
    """ generated source for class Parse """
    class digit(object):
        """ generated source for class digit """
        n = int()
        v = []

        def __init__(self):
            """ generated source for method __init__ """
            self.n = 0
            self.v = [None] * 3

    Digit = None

    def __init__(self):
        """ generated source for method __init__ """
        self.Digit = self.digit()

    def readComment(self, COUNT, buffer_):
        """ generated source for method readComment """
        DONE = 0
        while True:
            if buffer_[COUNT] == '\n':
                DONE = 1
            elif buffer_[COUNT] == '\r':
                DONE = 1
            else:
                pass
            COUNT += 1
            if DONE == 1:
                break
        return COUNT

    # 
    #  Read digits (number)
    #  = 1024 will return 1024
    #  = 120, 121.5, 122 will return 120 121 122, 3 numbers in structure Value
    #  with Digit.n = 3 and Digit.v[0] = 120, Digit.v[1] = 121.5 and Digit.v[2] = 122
    #  = 4a80 returns an error
    #  = 4 80 returns an error
    # 
    def readDigits(self, COUNT, buffer_, ERROR_NUMBER, filename):
        """ generated source for method readDigits """
        DONE = 0
        SIGN = 0
        DIGIT = 0
        tempBuf = ""
        try:
            self.Digit.n = 0
            while True:
                if buffer_[COUNT] == ' ':
                    pass
                elif buffer_[COUNT] == '=':
                    while True:
                        COUNT += 1
                        if buffer_[COUNT] == ' ':

                            if DIGIT <= 0:

                                DIGIT = 0


                        elif buffer_[COUNT] == '-':
                            if SIGN > 0 or DIGIT > 0:
                                DONE = 1
                                self.Digit.n = 0
                            else:
                                SIGN += 1
                                tempBuf += buffer_[COUNT]
                                DIGIT += 1


                        elif buffer_[COUNT] == '+':
                            if SIGN > 0 or DIGIT > 0:
                                DONE = 1
                                self.Digit.n = 0
                            else:
                                SIGN += 1
                                tempBuf += buffer_[COUNT]
                                DIGIT += 1


                        elif buffer_[COUNT] == ';':
                            self.Digit.v[self.Digit.n] = float(tempBuf)
                            self.Digit.n += 1
                            DONE = 1
                            DIGIT = 0


                        elif buffer_[COUNT] == ',':
                            if self.Digit.n > 3:
                                print("\nScene::readDigits: [" + tempBuf + " ] Error reading digits in file " + filename)
                                self.Digit.v[0] = self.Digit.v[1] = self.Digit.v[2] = 0
                                ERROR_NUMBER = 101
                            else:
                                self.Digit.v[self.Digit.n] = float(tempBuf)
                                self.Digit.n += 1
                                SIGN = 0
                                DIGIT = 0
                                tempBuf = ""


                        else:
                            #  Check for a decimal and a digit (0 - 9)
                            if buffer_[COUNT] != '.' and not str.isdigit(buffer_[COUNT]):
                                DONE = 1
                                self.Digit.n = 0


                            tempBuf += buffer_[COUNT]
                            DIGIT += 1

                        if DONE == 1:
                            break
                else:
                    DONE = 1
                COUNT += 1
                if DONE == 1:
                    break
            if self.Digit.n == 0:
                print("\nScene::readDigits: [" + tempBuf + " ] Error reading digits in file " + filename)
                self.Digit.v[0] = self.Digit.v[1] = self.Digit.v[2] = 0
                ERROR_NUMBER = 101
        except Exception as e:
            print("Erorr: ReadDigit:: Wrong number format")
            raise e
        return COUNT

    # 
    #  Get the word in char[] array from the String buffer starting from the COUNT
    # 
    def sscanf(self, buffer_, COUNT):
        """ generated source for method sscanf """
        index = buffer_.find("\n", COUNT)
        str_ = buffer_[COUNT:index]
        index = str_.find(' ')
        if index > 0:
            str_ = str_[0:index]
        return (str_.strip())

