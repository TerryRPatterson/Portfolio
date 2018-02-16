#! /usr/bin/env python2


def isValidNumber(number):
    stringedNumber = str(number)
    if stringedNumber[0:2] == "37" or stringedNumber[0:2] == "34":
        if not len(stringedNumber) == 15:
            return "Card number not vaild"
    elif not (len(str(number)) == 16):
        return "Card number not vaild"
    if str(number)[0:4] == "6011":
        return "Discover"
    if str(number)[0] == "4":
        return "Visa"

assert isValidNumber(6011000000000000) == "Discover", "The test failed excpeted output was Discover recived %d" %isValidNumber(6011000000000000)
assert isValidNumber(3781908473920192) == "Card number not vaild", "The test failed 2"
assert isValidNumber(4000000000000000) == "Visa", "The visa test failed"
assert isValidNumber(5300000000000000) == "Master Card" && isValidNumber(5500000000000000) == "Master Card", "Text failed expected two master cards did not get"
