import sys

if(len(sys.argv) > 1):
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print('{0} + {1} = {2}'.format(num1, num2, num1+num2))
    except ValueError:
        print("Values incorrectly given")

else:
    print("Not enough numbers given")

