# Automatically generated by Pynguin.
import argparse as module_0
import httpie.context as module_1
import httpie.core as module_2

def test_case_0():
    try:
        namespace_0 = module_0.Namespace()
        environment_0 = module_1.Environment()
        exit_status_0 = module_2.program(namespace_0, environment_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x0c\xa6\xfe\x12\xff\x16\x05\xe7g\xe8\x00'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        str_0 = '5P]Q'
        list_1 = module_2.decode_raw_args(list_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        exit_status_0 = module_2.main()
        str_0 = '--download'
        str_1 = 'https://www.yazilimperver.com/wp-content/uploads/2019/07/python-tutorial.jpg'
        str_2 = '-o'
        str_3 = 'python-tutorial.jpg'
        list_0 = [str_0, str_0, str_3]
        exit_status_1 = module_2.main(list_0)
        str_4 = [str_1, str_0, str_1, str_2, str_3]
        exit_status_2 = module_2.main(str_4)
        str_5 = None
        list_1 = [str_0, str_5, str_4]
        exit_status_3 = module_2.main(list_1)
    except BaseException:
        pass