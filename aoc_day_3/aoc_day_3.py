import string

import numpy as np

from helpers.day import Day


class Day3(Day):
    val_str = string.ascii_lowercase + string.ascii_uppercase

    def call(self, character):
        return self.val_str.index(character) + 1

    def task_1(self):
        sum = 0
        for item in self.file_content:
            first_halp = item[:int(len(item) / 2)]
            second_half = item[int(len(item) / 2):]
            sum += self.call(min(set(first_halp) & set(second_half)))
        return sum

    def task_2(self):
        sum = 0
        our_array = np.array(self.file_content)
        chunked_arrays = np.array_split(our_array, len(self.file_content) / 3)
        chunked_list = [list(array) for array in chunked_arrays]

        for item in chunked_list:
            character = min(set(item[0]) & set(item[1]) & set(item[2]))
            sum += self.call(character)

        return sum


aoc_day = Day3()

print(aoc_day.task_1())
print(aoc_day.task_2())

aoc_day_input = Day3("input.txt")
print(aoc_day_input.task_1())

print(aoc_day_input.task_2())
