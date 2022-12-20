import sys, time, os


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system("cls")


typingPrint('Hello Asim\n')
time.sleep(1)
typingPrint("Welcome to the world of python programming.\n")
time.sleep(1)
shpa_ka_na = typingInput('Shpa k n ze ba , type y or n: ')
time.sleep(1)
if shpa_ka_na == "y":
    typingPrint("\nChe shpa k bya kho tek da.")
    time.sleep(1)
else:
    typingPrint('\nche na k no hum sta khwakha da yara.')

time.sleep(1)
typingPrint("\nThis screen will clear in 3...")
time.sleep(1)
typingPrint('2...')
time.sleep(1)
typingPrint('1...')
time.sleep(1)
clearScreen()
