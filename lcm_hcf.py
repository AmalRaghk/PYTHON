# python program to compute LCM and GCD ofm two integer numbers

import sys

class ComputeHcfLcm:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def calculate_hcf(self)->int:
        smaller = self.y if self.x > self.y else self.x
        for i in range(1, smaller+1):
            if((self.x % i == 0) and (self.y % i == 0)): hcf = i 
        return hcf

    def calculate_lcm(self)->int:
        greater = self.x if self.x > self.y else self.y
        while True:
            if((greater % self.x == 0) and (greater % self.y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm


if __name__ == "__main__":

    try:
        num1 = int(input("\nEnter First Integer : "))
        num2 = int(input("Enter Second Integer : "))
    except ValueError as ex:
        print("\nException : {}".format(str(ex)))
        sys.exit("Entered Value is Not an Integer\n")

    choice = input("Calculate A) H.C.F., B) L.C.M. of {} and {} (Enter A/B): ".format(num1, num2))
    obj = ComputeHcfLcm(num1, num2)
    if choice in ('a', 'A'):
        print("H.C.F. of {} and {} is = {}\n".format(num1, num2, obj.calculate_hcf()))
    elif choice in ('b', 'B'):
        print("L.C.M. of {} and {} is = {}\n".format(num1, num2, obj.calculate_lcm()))
    else: print("Nothing Chosen!\n")
