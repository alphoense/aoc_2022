import string

import numpy as np

from helpers.day import Day


class Day3(Day):
    val_str = string.ascii_lowercase + string.ascii_uppercase

    def call(self, example_str: str):
        first_halp = example_str[:int(len(example_str) / 2)]
        second_half = example_str[int(len(example_str) / 2):]
        return min(set(first_halp) & set(second_half))

    def task_1(self):
        sum = 0
        for item in self.file_content:
            sum += self.val_str.index(self.call(example_str=item)) + 1
        return sum

    def task_2(self):
        sum = 0
        our_array = np.array(self.file_content)
        chunked_arrays = np.array_split(our_array, len(self.file_content) / 3)
        chunked_list = [list(array) for array in chunked_arrays]

        for item in chunked_list:
            character = min(set(item[0]) & set(item[1]) & set(item[2]))
            sum += self.val_str.index(character) + 1

        return sum


aoc_day = Day3()

print(aoc_day.task_1())
print(aoc_day.task_2())

aoc_day_input = Day3("input.txt")
print(aoc_day_input.task_1())

print(aoc_day_input.task_2())

