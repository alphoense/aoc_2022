from helpers.day import Day


# WINS_OVER = {"Rock": "Scissors",
#              "Scissors": "Paper",
#              "Paper": "Rock"}
# WINS_OVER = {1: ["A", "X"],  # rock
#              2: ["B", "Y"],  # paper
#              3: ["C", "Z"]  # scissors

class Day2(Day):
    TRANSLATE = {
        "A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3
    }
    WINS_OVER = {
        3: 2,
        2: 1,
        1: 3
    }

    def __init__(self):
        super().__init__(file_name="input.txt")
        self.file_content = [item.split(" ") for item in self.file_content]

    def task_1(self):
        # rm duplicates -> draw = +1
        sum = 0
        for elem in self.file_content:
            elems = [self.TRANSLATE[e] for e in elem]
            if len(set(elems)) == 1:
                sum += elems[1] + 3
            elif (elems[1], elems[0]) in self.WINS_OVER.items():
                sum += elems[1] + 6
            else:
                sum += elems[1]
        return sum

    def task_2(self):
        # Y - draw
        # X - lose
        # Z - win
        sum = 0
        for elem in self.file_content:
            translated_elems = [self.TRANSLATE[item] for item in elem]
            if elem[1] == "Y":
                sum += translated_elems[0] + 3
            elif elem[1] == "X":
                sum += self.WINS_OVER[translated_elems[0]]
            else:
                sum += [k for k, v in self.WINS_OVER.items() if v == translated_elems[0]][0] + 6
        return sum


aoc_day = Day2()

print(aoc_day.task_1())
print(aoc_day.task_2())
