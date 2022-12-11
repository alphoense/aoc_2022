from ctypes import Array
import itertools

from helpers.day import Day


class Node:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent



class Day7(Day):
    def __init__(self, file_name="test_input.txt"):
        super().__init__(file_name=file_name)
        # clean output
        self.file_content = [line[len("$ "):] if line.startswith("$ ") else line for line in self.file_content]

    def call(self):
        folders_with_folders = {}
        files = {}
        folders_with_files = {}
        curr_dir = ""
        for line in self.file_content:
            if ".." not in line:
                if line.startswith("cd"):
                    curr_dir = line.split(" ")[1]
                    # print(f"Current dir is {curr_dir}")
                    if not folders_with_folders.get(curr_dir):
                        folders_with_folders[curr_dir] = []
                    if not folders_with_files.get(curr_dir):
                        folders_with_files[curr_dir] = 0
                elif line.startswith("ls"):
                    print(f"ls next line")
                elif line.startswith("dir"):
                    dir_child = line.split(" ")[1]
                    # print(f"In curr dir {curr_dir} is a dirr {dir_child}")
                    folders_with_folders[curr_dir].append(dir_child)
                elif line.split(" ")[0].isdigit():
                    size, name = line.split(" ")
                    # print(f"In curr dir {curr_dir} is a file {name} with size {size}")
                    folders_with_files[curr_dir] += int(size)
                    if not files.get(name):
                        files[name] = int(size)
                else:
                    print("IDK what happened")
        return folders_with_folders, folders_with_files, files

    def task_1(self):
        folders_with_folders, folders_with_files, files = self.call()
        print("-------------")
        for item in [folders_with_folders, folders_with_files, files]:
            print(item)
        print("-------------")
        size_hash = {}

        for k, v in folders_with_folders.items():
            size_hash[k] = sum([folders_with_files[folder] for folder in v]) + folders_with_files[k]
        temp_folders_with_folders = folders_with_folders
        filled_folders = {}

        while all(isinstance(ele, list) for ele in list(folders_with_folders.values())):
            for k, v in folders_with_folders.items():
                if not v:
                    # fill empty folders
                    folders_with_folders[k] = folders_with_files[k] if folders_with_files.get(k) else [0]
                    if filled_folders.get(k):
                        filled_folders[k].append(folders_with_folders[k])
                    else:
                        filled_folders[k] = folders_with_folders[k]
                elif isinstance(v, list):
                    for item in v:
                        if filled_folders.get(item):
                            filled_folders[k] += filled_folders[item]
                        else:
                            filled_folders[k] = filled_folders[item] if filled_folders.get(item) else 0
        print(f"filed folder {filled_folders}")
        print(size_hash)
        # def get_value(items):
        #     total_sum = 0
        #     for i in items:
        #         try:
        #             total_sum += int(i)
        #         except ValueError:
        #             print(f"Problematic item is {i} -> {temp_tree[i]}")
        #             if size_hash.get(i):
        #                 size_hash[i] += get_value(temp_tree[i])
        #             else:
        #                 size_hash[i] = get_value(temp_tree[i])
        #
        #             total_sum += size_hash[i]
        #     return total_sum
        # print(tree)
        # print(temp_tree)
        # get_value(temp_tree["/"])
        # print(size_hash)
        # total_sum = 0
        # for k, v in size_hash.items():
        #     if v <= 100000:
        #         print(f"{k} : {v}")
        #         total_sum += v
        # print(f"TOTAL: {total_sum}")

    def task_2(self):
        pass


aoc_day = Day7()
print(aoc_day.task_1())
print(aoc_day.task_2())
#
# aoc_day_input = Day7("input.txt")
# print(aoc_day_input.task_1())
# print(aoc_day_input.task_2())
