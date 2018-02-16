#! /usr/bin/env python2


def isValidNumber(number):
    stringedNumber = str(number)
    if stringedNumber[0:2] == "37" or stringedNumber[0:2] == "34":
        if not len(stringedNumber) == 15:
            return "Card number not vaild"
    if not (len(str(number)) == 16):
        print("if 1 failed")
        print(len(str(number)))
        return "Card number not vaild"
    if str(number)[0:4] == "6011":
        return "Discover"


assert isValidNumber(6011000000000000) == "Discover", "The test failed"
assert isValidNumber(3781908473920192) == "Card number not vaild", "The test failed 2"
