def recursive(number):
    if number <= 500:
        print(number)
        number += 1
        recursive(number)


recursive(1)
