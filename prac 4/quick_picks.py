import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
        user_quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in user_quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            user_quick_pick.append(number)
        user_quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in user_quick_pick))