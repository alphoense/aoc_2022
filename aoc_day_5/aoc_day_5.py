import re

from helpers.day import Day


class Day5(Day):
    def __init__(self, file_name="test_input.txt"):
        with open(file_name, "r") as f:
            self.file_content = f.read().rstrip()
        self.matrix, self.commands = self.file_content.split("\n\n")
        self.matrix = self.matrix.replace("    ", "[x]")
        self.commands = [item for item in self.commands.split("\n")]

        for i in "[] ":
            self.matrix = self.matrix.replace(i, "")

    def call(self):
        all_rows = [list(item) for item in self.matrix.split("\n")]
        l = len(all_rows[-1])
        m = [None] * l
        for i in range(l):
            for j in range(len(all_rows) - 1):
                if not m[i]:
                    m[i] = []
                try:
                    if all_rows[j][i] and all_rows[j][i] != "x":
                        m[i].append(all_rows[j][i])
                except:
                    pass
        return [item[::-1] for item in m]

    def task_1(self):
        matrix = self.call()

        for c in self.commands:
            numbers = [int(item) for item in re.findall(r'\d+', c)]

            how_many = numbers[0]
            move_from = numbers[1] - 1
            move_to = numbers[2] - 1

            matrix[move_to] = matrix[move_to] + matrix[move_from][-abs(how_many):][::-1]
            matrix[move_from] = matrix[move_from][:len(matrix[move_from]) - how_many]

        return ''.join(item[-1] for item in matrix)

    def task_2(self):
        matrix = self.call()

        for c in self.commands:
            numbers = [int(item) for item in re.findall(r'\d+', c)]

            how_many = numbers[0]
            move_from = numbers[1] - 1
            move_to = numbers[2] - 1

            matrix[move_to] = matrix[move_to] + matrix[move_from][-abs(how_many):]
            matrix[move_from] = matrix[move_from][:len(matrix[move_from]) - how_many]
            # print(f"Command: {c} -> {temp}")

        return ''.join(item[-1] for item in matrix)


aoc_day = Day5()
print(aoc_day.task_1())
print(aoc_day.task_2())

aoc_day_input = Day5("input.txt")
print(aoc_day_input.task_1())
print(aoc_day_input.task_2())
