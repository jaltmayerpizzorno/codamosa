# Automatically generated by Pynguin.
import ansible.playbook.helpers as module_0

def test_case_0():
    try:
        bytes_0 = b'\x8b\x11\xe9\xee\xee\xfa4\xfcr<\xec\xb7#\x89\xf4\x1fS\x8a&'
        list_0 = [bytes_0, bytes_0, bytes_0]
        float_0 = 1600.1
        var_0 = module_0.load_list_of_blocks(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '4Hj+^'
        set_0 = {str_0, str_0, str_0}
        bytes_0 = b'J\x99\x87\x98\x048\xde\xa8\xe4\xb1d'
        var_0 = module_0.load_list_of_blocks(set_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1372.6
        float_1 = 2605.963
        var_0 = module_0.load_list_of_tasks(float_0, float_1)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -484
        tuple_0 = ()
        dict_0 = {int_0: tuple_0, tuple_0: int_0, tuple_0: int_0}
        var_0 = module_0.load_list_of_roles(int_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        list_0 = [bool_0, bool_0]
        bytes_0 = b''
        str_0 = '<+I'
        var_0 = module_0.load_list_of_blocks(list_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -4788
        list_0 = [int_0, int_0, int_0, int_0]
        bytes_0 = b']s\xf8\x1f\x02\x82C|'
        var_0 = module_0.load_list_of_roles(list_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -484
        tuple_0 = ()
        dict_0 = {int_0: tuple_0, tuple_0: int_0, tuple_0: int_0}
        list_0 = [dict_0, dict_0, dict_0, tuple_0]
        bytes_0 = b'\xbe\xd5\xfb\t\xbfr\x87\xe4)\x8a-\x0c\xff\x81;\x1e\xd4\xbf'
        var_0 = module_0.load_list_of_tasks(list_0, bytes_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'name'
        str_1 = 'firstutask'
        str_2 = {str_0: str_1}
        str_3 = 'block'
        str_4 = {str_3: str_1}
        str_5 = [str_2, str_4, str_4]
        var_0 = None
        var_1 = module_0.load_list_of_tasks(str_5, var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'name'
        str_1 = {}
        str_2 = 'block'
        str_3 = {str_0: str_2}
        str_4 = 'some_other_block'
        str_5 = {str_0: str_4}
        str_6 = [str_3, str_5]
        str_7 = {str_2: str_6}
        str_8 = 'last_task'
        str_9 = {str_0: str_8}
        str_10 = [str_1, str_7, str_9]
        var_0 = module_0.load_list_of_tasks(str_10, str_4)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '{{loop}}'
        str_1 = {str_0: str_0, str_0: str_0}
        str_2 = [str_1]
        bool_0 = False
        var_0 = module_0.load_list_of_tasks(str_2, str_2, str_2, str_2, bool_0, str_2, str_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'include'
        str_1 = 'loop'
        str_2 = '{{loop}}'
        str_3 = {str_0: str_0, str_1: str_2}
        str_4 = [str_3]
        bool_0 = True
        var_0 = module_0.load_list_of_tasks(str_4, str_1, str_1, str_1, bool_0, str_1, str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'include'
        str_1 = 'loop'
        str_2 = 'tes.yaml'
        str_3 = {str_0: str_2, str_1: str_0}
        str_4 = [str_3]
        bool_0 = False
        var_0 = module_0.load_list_of_tasks(str_4, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'name'
        str_1 = 'block'
        str_2 = 'rescue'
        str_3 = 'always'
        str_4 = 'ignore_errors'
        str_5 = 'List of tasks'
        var_0 = []
        var_1 = []
        bool_0 = False
        str_6 = 'One task'
        str_7 = {str_0: str_6}
        str_8 = 'Another task'
        str_9 = {str_0: str_8}
        str_10 = [str_7, str_9]
        var_2 = {str_0: str_5, str_2: var_0, str_3: var_1, str_4: bool_0, str_1: str_10}
        var_3 = []
        var_4 = []
        var_5 = {str_0: str_5, str_1: var_2, str_2: var_3, str_3: var_4, str_4: bool_0}
        str_11 = 'A task'
        str_12 = {str_0: str_11}
        var_6 = [var_5, str_12]
        var_7 = None
        var_8 = module_0.load_list_of_tasks(var_6, var_7, var_7, var_7, var_7)
    except BaseException:
        pass