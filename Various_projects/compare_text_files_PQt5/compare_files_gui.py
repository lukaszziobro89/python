import tkinter
from tkinter.filedialog import *


# returns path of input file
def file_path():
    root = tkinter.Tk()
    root.withdraw()
    open_file = askopenfile(filetypes=[("Only text files", "*.txt")])
    return open_file.name


# returns symmetric difference between input files
def find_differences(first_batch, second_batch):
        diff = set(first_batch).symmetric_difference(second_batch)
        return diff


# returns modified path to file
def path_to_file(input_filename):
    current_directory = str(os.getcwd())
    initial_path = current_directory + '\\' + str(input_filename) + '.txt'
    first_replace = initial_path.replace('\\\\', '\\')
    final_path = first_replace.replace('\\', '//')
    return final_path
