import string
from random import choice, shuffle


def randomPass():
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)

    all = lower + upper + digits
    shuffle(all)

    lengeth = int(input("how long do you want the password?: "))

    Password = ''

    for i in range(lengeth):
        Password += choice(all)
    print(Password)


randomPass()
