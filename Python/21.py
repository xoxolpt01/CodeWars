'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false


'''


def validate_pin(pin):
    if len(pin) == 4:

        for i in pin:
            try:
                x = int(i)
            except:
                return False
        return True

    elif len(pin) == 6:
        for i in pin:
            try:
                k = int(i)
            except:
                return False
        return True
    else:
        return False



print(validate_pin('-1.234'))