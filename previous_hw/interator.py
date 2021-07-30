import json
from pprint import pprint
from const_for_logs import result_file_name as fl_name, result_dir as file_dir
from decorator_log import loger_constructor_decor as decor_log


@decor_log(f'iterator {fl_name}', file_dir)
class Country:

    def __init__(self, json_list):
        self._json_list = json_list
        self._max = len(json_list)
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index == self._max:
            raise StopIteration
        return self._json_list[self._index]['translations']['rus']['common']


result_dict = {}
countries_list = json.load(open('countries.json'))
for country in Country(countries_list):
    result_dict.setdefault(country, f"https://ru.wikipedia.org/wiki/{country.replace(' ', '_')}")

pprint(result_dict)
