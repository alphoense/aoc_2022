import itertools

from helpers.day import Day


class Day10(Day):
    def __init__(self, file_name="test_input.txt"):
        super().__init__(file_name=file_name)
        self.stack = [item.split(" ") for item in self.file_content]
        self.stack = list(itertools.chain(*self.stack))
        self.init_vals()

    def init_vals(self):
        self.val = 1
        self.cycle = 0

    def task_1(self):
        sum1 = 0
        for i in range(len(self.stack)):
            if i in [19, 59, 99, 139, 179, 219]:
                sum1 += (self.cycle + 1) * self.val
            try:
                num_to_add = int(self.stack[i])
                self.val += num_to_add
            except ValueError:
                pass
            self.cycle += 1
        return sum1

    def task_2(self):
        self.init_vals()
        crt = ""
        for i in range(0, len(self.stack)):
            if self.cycle % 40 in range(self.val - 1, self.val + 2):
                crt += "#"
            else:
                crt += "."
            try:
                num_to_add = int(self.stack[i])
                self.val += num_to_add
            except ValueError:
                pass
            self.cycle += 1
            if i % 40 == 0 and i > 39:
                print(''.join(crt[i - 40:i]))
        print(''.join(crt[len(crt) - 40:len(crt)]))


aoc_day = Day10()
print(aoc_day.task_1())
print(aoc_day.task_2())
#
#
aoc_day_input = Day10("input.txt")
print(aoc_day_input.task_1())
print(aoc_day_input.task_2())
