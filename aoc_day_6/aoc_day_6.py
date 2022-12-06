from helpers.day import Day


class Day6(Day):
    def call(self, marker: int = 4) -> int:
        file_len = len(self.file_content[0])
        for i in range(file_len - marker):
            if len(set(self.file_content[0][i:i + marker])) == marker:
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
print(aoc_day_input.task_2())
