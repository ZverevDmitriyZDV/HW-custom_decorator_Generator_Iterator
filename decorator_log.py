from datetime import datetime
import os


# начало конструктора

def loger_constructor_decor(file_name, file_path=None):
    if file_path is None:
        file_place = os.path.join(os.getcwd())
    else:
        file_place = os.path.join(os.path.abspath(file_path))

    file_path = os.path.join(file_place, file_name)

    # начало декоратора
    def loger_decorator(old_function):

        def addition_def(*args, **kwargs):
            log_date = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
            func_name = old_function.__name__
            input_data = f'вводные данные:{args} и {kwargs}'
            output_data = old_function(*args, **kwargs)
            result_line = f'вызвана функция {func_name} \n' \
                          f'дата и время вызова : {log_date} \n' \
                          f'{input_data} \n' \
                          f'результирующее значение функции {func_name}: {output_data}\n' \
                          f'-----------------------------------\n'

            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(result_line)

            return output_data

        return addition_def

    # конец декоратора
    return loger_decorator
# конец конструктора
