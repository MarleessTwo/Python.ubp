def recursive(number):
    if number <= 10:
        print(number)
        number += 1
        return recursive(number)


recursive(1)
