class NumberProcessor:

    def __init__(self, numbers):
        self.numbers = numbers

    def get_even(self):
        even = []
        for i in self.numbers:
            if i % 2 == 0:
                even.append(i)
        return even

    def get_odd(self):
        odd = []
        for i in self.numbers:
            if i % 2 != 0:
                odd.append(i)
        return odd

    def process(self):
        return self.get_even(), self.get_odd()


# Usage
nums = [1, 32, 4, 54, 6, 7, 8, 9]

obj = NumberProcessor(nums)

even, odd = obj.process()

print("Even:", even)
print("Odd:", odd)
