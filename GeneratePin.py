def pin(number):
    import random
    pin = ""
    for i in range(number):
        #concatinate a random digit to the pin
        pin += str(random.randint(0, 9))
    return pin
print(pin(5))



