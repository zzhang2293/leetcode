import random


class Bitmap:

    def __init__(self, num: int) -> None:
        self.mapping = [0] * ((num + 31) // 32)
        self.value = num - 1

    def add(self, num: int) -> None:
        """ add a value into the bitmap """
        if num < 0 or num > self.value: return
        position, offset = num // 32, num % 32
        self.mapping[position] |= 1 << offset
        return

    def remove(self, num: int) -> None:
        """ remove a value from the bitmap """
        if num < 0 or num > self.value: return
        position, offset = num // 32, num % 32
        if self.mapping[position] & 1 << offset != 0:
            self.mapping[position] ^= 1 << offset
        return

    def find(self, num: int) -> bool:
        """ find a value in the bitmap """
        if num < 0 or num > self.value: return False
        position, offset = num // 32, num % 32
        return False if self.mapping[position] & 1 << offset == 0 else True

    def reverse(self, num: int) -> None:
        if num < 0 or num > self.value: return
        position, offset = num // 32, num % 32
        self.mapping[position] ^= 1 << offset
        return


def test():
    test_time = 100000
    print("test start")
    bitmap = Bitmap(10000)
    test_set = set()
    for i in range(test_time):
        random_num = random.random()
        num = random.randint(0, 10000 - 1)
        if random_num < 0.33:
            bitmap.add(num)
            test_set.add(num)
        elif random_num < 0.66:
            bitmap.remove(num)
            test_set.remove(num) if num in test_set else None
        elif random_num < 1:
            bitmap.reverse(num)
            if num in test_set:
                test_set.remove(num)
            else:
                test_set.add(num)
    for i in range(10000):
        if bitmap.find(i) != (i in test_set):
            print(i)
            print(bitmap.find(i))
            print("error")
            break
    print("test finish")


test()
