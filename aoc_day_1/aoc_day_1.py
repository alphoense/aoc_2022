from itertools import groupby

from aoc_day.aoc_day import Day


class Day1(Day):
    def __init__(self):
        super().__init__(file_name="input.txt")
        self.file_content = [list(g) for k, g in groupby(self.file_content, key=bool) if k]

    def count_calories_per_elves(self):
        temp = []
        for element in self.file_content:
            temp.append(sum([int(elem) for elem in element]))
        return temp

    def task_1(self):
        return max(self.count_calories_per_elves())

    def task_2(self):
        calories = self.count_calories_per_elves()
        return sum(sorted(calories, reverse=True)[0:3])


aoc_day = Day1()

print(aoc_day.task_1())
print(aoc_day.task_2())

# assert aoc_day.task_1() == 24000
# assert aoc_day.task_2() == 45000
