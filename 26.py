def histogram(items):
    for n in items:
        output = ""
        times = n

        while times > 0:
            output += "*"
            times -= 1

        print(output)


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

histogram(numbers)
