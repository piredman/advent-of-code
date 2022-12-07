import csv
from dataclasses import dataclass
from enum import Enum

_total_disk_space: int = 70000000
_update_size: int = 30000000


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: 'Directory'
    directories: list['Directory']
    files: list[File]
    size: int


_directories: list[Directory] = []
_current: Directory = None


def load_data():
    output: list = []
    with open('2022/07/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            output.append(row[0])

    return output


def process_command(input: list):
    commands = {'cd': process_cd, 'ls': process_ls}
    command = commands.get(input[0])
    arg = '' if len(input) != 2 else input[1]
    command(arg)


def process_cd(input: str):
    global _current
    global _directories

    if input == '/':
        _current = _directories[0]
        return

    if input == '..':
        if _current.parent:
            _current = _current.parent
        return

    for directory in _current.directories:
        if directory.name == input:
            _current = directory
            break


def process_ls(input: str):
    pass


def process_output(input: list):
    global _current

    if input[0] == 'dir':
        directory = Directory(input[1], _current, [], [], 0)
        _current.directories.append(directory)
        return

    file = File(input[1], int(input[0]))
    _current.files.append(file)


def determine_directories_size(directories: list[Directory]):
    size = 0
    for directory in directories:
        directory_size = determine_files_size(directory)
        if directory.directories:
            directory_size += determine_directories_size(directory.directories)

        directory.size = directory_size
        size += directory_size

    return size


def determine_files_size(directory: Directory):
    size = 0
    for file in directory.files:
        size += file.size

    return size


def process(input):
    for line in input:
        line_data: list = line.split(' ')
        if line_data[0] == '$':
            process_command(line_data[1:])
        else:
            process_output(line_data)

    determine_directories_size(_directories)


def get_directories_of_size(size: int, directories: list[Directory]):
    output: list[Directory] = []
    for directory in directories:
        if directory.size <= size:
            output.append(directory)

        result = get_directories_of_size(size, directory.directories)
        output += result

    return output


def sum_directories(directories: list[Directory]):
    output = 0
    for directory in directories:
        output += directory.size

    return output


def find_directories_to_delete(space_needed: int, directories: list[Directory], output: list[Directory]):
    for directory in directories:
        if directory.size >= space_needed:
            output.append(directory)

        if (directory.directories):
            output = find_directories_to_delete(
                space_needed, directory.directories, output)

    return output


def get_smallest(directories: list[Directory]):
    output: Directory = directories[0]
    for directory in directories:
        if directory.size < output.size:
            output = directory

    return output


def print_tree(directories: list[Directory], indent: int):
    for directory in directories:
        directory_indent = indent * ' '
        print(f'{directory_indent}- {directory.name} (dir, size={directory.size})')
        print_tree(directory.directories, indent + 2)

        file_indent = (indent + 2) * ' '
        for file in directory.files:
            print(f'{file_indent}- {file.name} (file, size={file.size})')


def print_directories(directories: list[Directory]):
    for directory in directories:
        print(f'{directory.name} (dir, size={directory.size})')


data = load_data()

_directories.append(Directory('/', None, [], [], 0))
_current = _directories[0]

process(data)
print_tree(_directories, 0)

directories_of_size = get_directories_of_size(100000, _directories)
print(f'sum: {sum_directories(directories_of_size)}')

used_disk_space = _directories[0].size
unused_disk_space = _total_disk_space - used_disk_space
needed_disk_space = _update_size - unused_disk_space
print(f'unused: {unused_disk_space}, needed: {needed_disk_space}')

large_enough_directories = find_directories_to_delete(
    needed_disk_space, _directories, [])
print_directories(large_enough_directories)

best_directory = get_smallest(large_enough_directories)
print(f'best: {best_directory.name} (dir, size={best_directory.size})')
