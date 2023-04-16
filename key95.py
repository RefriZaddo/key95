import os
import random
import fnmatch, re
import time

def modSeven(n: int):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    if sum % 7 == 0:
        return True
    else:
        return False

def keyCheck(key):
    if key in str(re.compile(fnmatch.translate("?????-OEM-???????-?????")).match(key)):
        keyParts = key.split("-")
        keyParts.remove("OEM")
        partOne = int(''.join(map(str,list(keyParts[0])[:3])))
        partTwo = int(''.join(map(str,list(keyParts[0])[3:])))
        partThree = int(keyParts[1])
        if 0 <= partOne <= 366:
            validOne = True
        else:
            validOne = False
        if 0 <= partTwo <= 3 or 95 <= partTwo <= 99:
            validTwo = True
        else:
            validTwo = False
        if modSeven(partThree):
            validThree = True
        else:
            validThree = False
        if validOne and validTwo and validThree:
            return True
        else:
            return False


    elif key in str(re.compile(fnmatch.translate("???-???????")).match(key)):
        keyParts = key.split("-")
        for part in keyParts:
            keyParts[keyParts.index(part)] = int(keyParts[keyParts.index(part)])
        if 0 <= keyParts[0] <= 998 and not keyParts[0] in [333, 444, 555, 666, 777, 888]:
            validOne = True
        else:
            validOne = False
        if modSeven(keyParts[1]):
            validTwo = True
        else:
            validTwo = False
        if validOne and validTwo:
            return True
        else:
            return False

    else:
        return False

while True:
    print("Welcome to Key95!\n1) Key generator\n2) Key checker\n3) Quit")
    keyninetyfive = input("[Key95 1.0]>>>")
    if int(keyninetyfive) == 1:
        print("1) Windows 95 RTM CD key (10-digit format)\n2) Windows 95 OSR2/OSR2.5 OEM key")
        keygen = input("[Keygen|Key95 1.0]>>>")
        amount = input("Amount: ")
        if int(keygen) == 1:
            for i in range(1, int(amount)+1, 1):
                rtmKey = "-".join([str(random.randint(0, 998)).zfill(3), str(random.randint(0, 9999999)).zfill(7)])
                while not keyCheck(rtmKey):
                    rtmKey = "-".join([str(random.randint(0, 998)).zfill(3), str(random.randint(0, 9999999)).zfill(7)])
                print("Key", str(i) + ":", rtmKey)
            input("Press Enter to continue...")
        elif int(keygen) == 2:
            print("Activation year interval?\n1) 1995-1999\n2) 2000-2003")
            activationDate = input("[OEM Keygen|Key95 1.0]>>>")
            oemYear = ''
            for i in range(1, int(amount)+1, 1):
                if int(activationDate) == 1:
                    oemYear = str(random.randint(95, 99))
                elif int(activationDate) == 2:
                    oemYear = str(random.randint(0, 3)).zfill(2)
                oemKey = "-".join([str(random.randint(1, 366)).zfill(3) + oemYear, "OEM",str(random.randint(0, 99999)).zfill(7),str(random.randint(0,99999)).zfill(5)])
                while not keyCheck(oemKey):
                    oemKey = "-".join([str(random.randint(1, 366)).zfill(3) + oemYear, "OEM",str(random.randint(0, 99999)).zfill(7),str(random.randint(0, 99999)).zfill(5)])
                print("Key", str(i) + ":", oemKey)
            input("Press Enter to continue...")
            os.system("clear" if os.name == "posix" else "cls")
            continue
        else:
            print("ERR not an option - Restarting script...")
            time.sleep(1)
            os.system("clear" if os.name == "posix" else "cls")
            continue
    elif int(keyninetyfive) == 2:
        print("Key:")
        key = input("[Keycheck|Key95 1.0]")
        if keyCheck(key):
            print("Valid")
        else:
            print("Invalid")
        input("Press Enter to continue...")
        os.system("clear" if os.name == "posix" else "cls")
        continue
    elif int(keyninetyfive) == 3:
        break
    else:
        print("ERR not an option - Restarting script...")
        time.sleep(1)
        os.system("clear" if os.name == "posix" else "cls")
        continue
    os.system("clear" if os.name == "posix" else "cls")
quit()
