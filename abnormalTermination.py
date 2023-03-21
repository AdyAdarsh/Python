def ExceptionHandler():
    print("Exception with try ,except and else")
    print('One')
    print('Two')
    try:
        print(10 / 0) 
    except ZeroDivisionError:
        print("Exception Handled")
    else: 
        print('Four')
        print('Five')
    print()


def ExceptionTry():
    print("Exception with only try and except")
    print("One")
    print("Two")
    try:
        print(10 / 0)
    except ZeroDivisionError: 
        print("Exception Handled") 
    print("Four")
    print("Five")
    print()


def AbnormalTermination()
    print("ZeroDivisionError")
    print('One')
    print('Two')
    print(10 / 0)  
    print('Four') 
    print('Five')
    print()


ExceptionHandler()
ExceptionTry()
AbnormalTermination()
