# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '%z&o~`5f0db'
    str_1 = module_0.expand(str_0)

def test_case_2():
    str_0 = 'TVIaSIS=~/aoxemt'
    str_1 = [str_0, str_0]
    ordered_dict_0 = module_0.load_env_file(str_1)

def test_case_3():
    str_0 = '%z&o~`5f0db'
    list_0 = [str_0]
    bytes_0 = b'\xd5\x1cf\xa9\x18\xb0\xfb|\x996\x80\xf3\xfd\xff\x87\xd5O'
    ordered_dict_0 = module_0.load_env_file(list_0, bytes_0)
    str_1 = module_0.expand(str_0)

def test_case_4():
    str_0 = 'THISIS=~/a/test'
    str_1 = [str_0, str_0]
    var_0 = dict()
    str_2 = 'pf'
    list_0 = [str_1, str_0]
    dict_0 = {str_0: var_0, str_2: list_0, str_0: str_1}
    set_0 = None
    ordered_dict_0 = module_0.load_env_file(dict_0, set_0)

def test_case_5():
    str_0 = 'a=b'
    str_1 = 'c=d'
    str_2 = "e='f'"
    str_3 = 'g="h"'
    str_4 = 'i=\\n'
    str_5 = "j='\n'"
    str_6 = 'k="\n"'
    str_7 = "l='\n\n'"
    str_8 = 'm="\n\n"'
    str_9 = [str_0, str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8]
    generator_0 = module_0.parse_env_file_contents(str_9)
    var_0 = [i for i in generator_0]