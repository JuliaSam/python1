# python with_args.py param1 param2 param3
import os
import sys
from shutil import copyfile

print('sys.argv = ', sys.argv)

# print how to use information
def print_help():
    print('help - print how to use information')
    print('mkdir <directory_name> - create a directory')
    print('ping - print test message')
    print('ls - return working directory name')
    print('cd <full_path or relative_path> - change the working directory')
    print('cp <file_name> - make a copy of the file')
    print('rm <file_name> - remove the file')


# private util function that reads second argv parameter
def read_second_parameter():
    try:
        second_parameter = sys.argv[2]
    except IndexError:
        second_parameter = None
    return second_parameter


# copy file
def copy_file():
    suffix = '.copy'
    file_name = read_second_parameter()
    if not file_name:
        print('Parameter <FILE_NAME> is missed')
        return
    if not os.path.exists(file_name):
        print('File {} does not exist'.format(file_name))
        return
    copy_file_name = file_name + suffix
    try:
        copyfile(file_name, copy_file_name)
        print('File {} was copied to {}'.format(file_name, copy_file_name))
    except IOError:
        print('Access denied.')


# remove file
def remove_file():
    file_name = read_second_parameter()
    if not file_name:
        print('Parameter <FILE_NAME> is missed')
        return
    if not os.path.exists(file_name):
        print('File {} does not exist'.format(file_name))
        return
    if os.path.isdir(file_name):
        print('{} is a directory. This command can delete only a file.'.format(file_name))
        return
    try:
        os.remove(file_name)
        print('File {} was removed'.format(file_name))
    except OSError:
        print('Access denied.')


# print working directory
def pwd():
    print(os.getcwd())


# change current working directory
def change_directory():
    dir_path = read_second_parameter()
    if not dir_path:
        print('Parameter <FULL_PATH or RELATIVE_PATH> is missed')
        return
    try:
        os.chdir(dir_path)
        print('New working directory is: \"{}\"'.format(os.getcwd()))
    except FileNotFoundError:
        print('There is no such directory. Path is invalid.')


# create new directory
def make_dir():
    dir_name = read_second_parameter()
    if not dir_name:
        print('Parameter <DIRECTORY_NAME> is missed')
        return

    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Directory {} was created'.format(dir_name))
    except FileExistsError:
        print('Directory {} already exists'.format(dir_name))


# Print test message
def ping():
    print('pong')


# Brain part of the library
do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'ls': pwd,
    'cd': change_directory,
    'cp': copy_file,
    'rm': remove_file
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Error! You wrote incorrect key.')
        print('Write command help to read the program description.')
