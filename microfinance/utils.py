import random
import string



def randomPassword(stringLength=2):
    """Generate a random password """
    key01  = 'EMF0'
    letters = string.ascii_uppercase
    digits = string.digits
    password = key01
    password += ''.join(random.choice(letters) for i in range(stringLength))
    password += ''.join(random.choice(digits) for i in range(stringLength))

    passwordList = list(password)
    password = ''.join(passwordList)



    return password





def unique_order_pin_agence(instance):
    new_pincode = randomPassword()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(pincode = new_pincode).exists()
    if qs_exists:
        return unique_order_pin_agence(instance)
    return new_pincode


def randomPassword2(stringLength=2):
    """Generate a random password """
    key01  = 'CLI0'
    letters = string.ascii_uppercase
    digits = string.digits
    password = key01
    password += ''.join(random.choice(letters) for i in range(stringLength))
    password += ''.join(random.choice(digits) for i in range(stringLength))

    passwordList = list(password)
    password = ''.join(passwordList)



    return password


def unique_order_pin_client(instance):
    new_pincode = randomPassword2()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(pincode = new_pincode).exists()
    if qs_exists:
        return unique_order_pin_agence(instance)
    return new_pincode



def randomPassword3(stringLength=2):
    """Generate a random password """
    key01  = 'TC0'
    letters = string.ascii_uppercase
    digits = string.digits
    password = key01
    password += ''.join(random.choice(letters) for i in range(stringLength))
    password += ''.join(random.choice(digits) for i in range(stringLength))

    passwordList = list(password)
    password = ''.join(passwordList)



    return password


def unique_order_pin_type_cpte(instance):
    new_pincode = randomPassword3()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(pincode = new_pincode).exists()
    if qs_exists:
        return unique_order_pin_type_cpte(instance)
    return new_pincode




def randomPassword4(stringLength=2):
    """Generate a random password """
    key01  = 'DEP0'
    letters = string.ascii_uppercase
    digits = string.digits
    password = key01
    password += ''.join(random.choice(letters) for i in range(stringLength))
    password += ''.join(random.choice(digits) for i in range(stringLength))

    passwordList = list(password)
    password = ''.join(passwordList)



    return password


def unique_order_pin_depot(instance):
    new_pincode = randomPassword4()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(pincode = new_pincode).exists()
    if qs_exists:
        return unique_order_pin_depot(instance)
    return new_pincode



def randomPassword5(stringLength=2):
    """Generate a random password """
    key01  = 'DEP0'
    letters = string.ascii_uppercase
    digits = string.digits
    password = key01
    password += ''.join(random.choice(letters) for i in range(stringLength))
    password += ''.join(random.choice(digits) for i in range(stringLength))

    passwordList = list(password)
    password = ''.join(passwordList)



    return password


def unique_order_pin_retrait(instance):
    new_pincode = randomPassword5()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(pincode = new_pincode).exists()
    if qs_exists:
        return unique_order_pin_retrait(instance)
    return new_pincode