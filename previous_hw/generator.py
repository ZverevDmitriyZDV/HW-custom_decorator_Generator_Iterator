import hashlib
from const_for_logs import result_file_name as fl_name, result_dir as file_dir
from decorator_log import loger_constructor_decor as decor_log


@decor_log(f'generator {fl_name}', file_dir)
def hash_line(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            yield line, hashlib.md5(line.encode('utf-8')).hexdigest()


test = 'test_input.txt'
for data in hash_line(test):
    print(*data)
