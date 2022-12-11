from helpers.day import Day, count_time


class Day6(Day):
    def __init__(self, file_name="test_input.txt"):
        super().__init__(file_name=file_name)
        self.file_content = self.file_content[0]

    def call(self, marker: int = 4) -> int:
        file_len = len(self.file_content)
        for i in range(file_len - marker):
            if len(set(self.file_content[i:i + marker])) == marker:
                return i + marker

    def task_1(self) -> int:
        return self.call()

    def task_2(self) -> int:
        return self.call(marker=14)


aoc_day = Day6()
print(aoc_day.task_1())
print(aoc_day.task_2())

aoc_day_input = Day6("input.txt")
print(aoc_day_input.task_1())
print(count_time(aoc_day_input.task_1))
print(aoc_day_input.task_2())
print(count_time(aoc_day_input.task_2))

# 7
# 19
# 1833
# Time for func: 0.0007951259613037109
# 3425
# Time for func: 0.002691030502319336