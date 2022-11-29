class Day:

    def __init__(self, file_name: str = "test_input.txt"):
        with open(file_name, "r") as f:
            self.file_content = list(map(str.strip, f.readlines()))

    def task_1(self):
        pass

    def task_2(self):
        pass


aoc_day = Day()
assert aoc_day.task_1() == 1
assert aoc_day.task_2() == 1
