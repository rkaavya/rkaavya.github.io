class Facs:

    def fact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


n = int(input("Enter a number for factorial:"))

obj = Facs()
f = obj.fact(n)
print("Factorial is:", f)