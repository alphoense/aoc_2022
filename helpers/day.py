import time


def count_time(func):
    start = time.time()
    func()
    stop = time.time() - start
    return f"Time for func: {stop}"


class Day:

    def __init__(self, file_name: str = "test_input.txt"):
        with open(file_name, "r") as f:
            self.file_content = list(map(str.strip, f.readlines()))

    def call(self):
        pass

    def task_1(self):
        pass

    def task_2(self):
        pass
