'''
Connor Kissack
Binary Pseudo Code Conversion
March 8, 2021
'''

VALUES = [11,12,15,16,112,118,123,145]
TARGET = 15
MIN = 0
HIGH = 7
FOUND = False
ANSWER = 0
MID = 0

while FOUND == False  and MIN <= HIGH:
    MID = ((MIN + HIGH)/2)
    MID_int = int(MID)
    if VALUES[MID_int] == TARGET:
        FOUND = True
        ANSWER = MID
    elif TARGET > VALUES[MID_int]:
        MIN = MID_int+1

    else:
        HIGH = MID_int - 1

    if FOUND == True:
        print(TARGET, "FOUND AT ARRAY INDEX", ANSWER)
    else:
        print(TARGET, "WAS NOT FOUND")