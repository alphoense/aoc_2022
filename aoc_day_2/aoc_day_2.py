from typing import Dict

from helpers.day import Day


class Day2(Day):
    def call(self, dict_operator: Dict):
        value = 0
        for item in self.file_content:
            value += dict_operator[item]
        return value

    def task_1(self):
        # WINS_OVER = {1: ["A", "X"],  # rock
        #              2: ["B", "Y"],  # paper
        #              3: ["C", "Z"]  # scissors
        results = {
            "A X": 1 + 3,
            "A Y": 2 + 6,
            "A Z": 3,
            "B X": 1,
            "B Y": 2 + 3,
            "B Z": 3 + 6,
            "C X": 1 + 6,
            "C Y": 2,
            "C Z": 3 + 3
        }
        return self.call(dict_operator=results)

    def task_2(self):
        # WINS_OVER = {1: ["A", "X"],  # rock
        #              2: ["B", "Y"],  # paper
        #              3: ["C", "Z"]  # scissors
        # Y - draw
        # X - lose
        # Z - win
        results = {
            "A X": 3,
            "A Y": 1 + 3,
            "A Z": 2 + 6,
            "B X": 1,
            "B Y": 2 + 3,
            "B Z": 3 + 6,
            "C X": 2,
            "C Y": 3 + 3,
            "C Z": 1 + 6
        }
        return self.call(dict_operator=results)


aoc_day = Day2(file_name="input.txt")
print(aoc_day.task_1())
print(aoc_day.task_2())

# TRANSLATE = {
#     "A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3
# }
# WINS_OVER = {
#     3: 2,
#     2: 1,
#     1: 3
# }

# def task_1(self):
#     sum = 0
#     for elem in self.f:
#         elems = [self.TRANSLATE[e] for e in elem]
#         if len(set(elems)) == 1:
#             sum += elems[1] + 3
#         elif (elems[1], elems[0]) in self.WINS_OVER.items():
#             sum += elems[1] + 6
#         else:
#             sum += elems[1]
#     return sum
#
# def task_2(self):
#     # Y - draw
#     # X - lose
#     # Z - win
#     sum = 0
#     for elem in self.f:
#         translated_elements = [self.TRANSLATE[item] for item in elem]
#         if elem[1] == "Y":
#             sum += translated_elements[0] + 3
#         elif elem[1] == "X":
#             sum += self.WINS_OVER[translated_elements[0]]
#         else:
#             sum += [k for k, v in self.WINS_OVER.items() if v == translated_elements[0]][0] + 6
#     return sum
