from const_for_logs import result_file_name as fl_name, result_dir as file_dir
from decorator_log import loger_constructor_decor as decor_log


@decor_log(fl_name, file_dir)
def test_def(a, b):
    return a + b


if __name__ == '__main__':
    test_def(1000,5000)
    test_def(100002,2500000)
    test_def(22,1215)




