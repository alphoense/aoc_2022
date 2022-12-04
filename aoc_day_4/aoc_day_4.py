from helpers.day import Day


class Day4(Day):

    def __init__(self, file_name="test_input.txt"):
        super().__init__(file_name=file_name)
        self.file_content = [item.split(",") for item in self.file_content]
        self.range_arr = list(range(1, 100))

    def call(self, ranges):
        range_1 = [int(x) for x in ranges[0].split("-")]
        range_2 = [int(x) for x in ranges[1].split("-")]
        arr_1 = self.range_arr[range_1[0] - 1:range_1[1]]
        arr_2 = self.range_arr[range_2[0] - 1:range_2[1]]
        return arr_1, arr_2

    def task_1(self):
        subsets_count = 0
        for ranges in self.file_content:
            arr_1, arr_2 = self.call(ranges)
            is_subset = set(arr_1).issubset(set(arr_2)) or set(arr_2).issubset(set(arr_1))
            subsets_count += 1 if is_subset else 0
        return subsets_count

    def task_2(self):
        subsets_count = 0
        for ranges in self.file_content:
            arr_1, arr_2 = self.call(ranges)
            combined_list = list(set(arr_1) | set(arr_2))
            subsets_count += 1 if len(combined_list) < len(arr_2) + len(arr_1) else 0
        return subsets_count


aoc_day = Day4()
print("----test data-----")
print(aoc_day.task_1())
print(aoc_day.task_2())

print("----input data-----")
aoc_day_input = Day4(file_name="input.txt")
print(aoc_day_input.task_1())
print(aoc_day_input.task_2())
