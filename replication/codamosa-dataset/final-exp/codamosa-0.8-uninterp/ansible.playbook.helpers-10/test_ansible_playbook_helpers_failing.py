# Automatically generated by Pynguin.
import ansible.playbook.helpers as module_0

def test_case_0():
    try:
        set_0 = set()
        list_0 = [set_0]
        tuple_0 = None
        bytes_0 = b't\xb7\t\xd1\x02K%\xf3\xaf'
        var_0 = module_0.load_list_of_blocks(list_0, tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'U\n'
        bytes_0 = b''
        set_0 = {bytes_0}
        str_1 = 'P-$P}5'
        complex_0 = None
        bool_0 = True
        float_0 = 0.2
        var_0 = module_0.load_list_of_blocks(complex_0, bool_0, float_0)
        bool_1 = None
        tuple_0 = (bytes_0, set_0, str_1, bool_1)
        list_0 = [str_0]
        var_1 = module_0.load_list_of_blocks(str_0, tuple_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        int_0 = -1994
        float_0 = 2626.44547
        list_0 = [set_0, int_0, int_0, set_0]
        var_0 = module_0.load_list_of_tasks(set_0, int_0, float_0, list_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        int_0 = 1
        int_1 = {str_0: int_0}
        int_2 = {str_0: int_1}
        int_3 = [int_1, int_1, int_1, int_1, int_2]
        bool_0 = False
        var_0 = module_0.load_list_of_tasks(int_3, int_0, int_0, int_0, int_0, bool_0, int_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'set_fact'
        int_0 = 1
        int_1 = {str_0: int_0}
        int_2 = {str_0: int_1}
        int_3 = 2
        int_4 = [int_2, int_3]
        var_0 = None
        bool_0 = False
        var_1 = module_0.load_list_of_tasks(int_4, var_0, var_0, var_0, var_0, bool_0, var_0, var_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        list_0 = [bool_0]
        list_1 = [bool_0, list_0]
        var_0 = module_0.load_list_of_roles(list_0, list_1)
    except BaseException:
        pass

def test_case_6():
    try:
        set_0 = set()
        str_0 = 'T_Sp'
        var_0 = module_0.load_list_of_roles(set_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        bytes_0 = b'\xfd\x9d\xea8\xfbX\x11\xf8\xa5\xee\x9b\x87m=\xeaQP*\xab'
        var_0 = module_0.load_list_of_roles(list_0, list_0, bytes_0)
        float_0 = 2.0
        complex_0 = None
        set_0 = {float_0, bytes_0, bytes_0}
        complex_1 = None
        var_1 = module_0.load_list_of_blocks(complex_0, set_0, float_0, complex_1, list_0)
        list_1 = [float_0]
        float_1 = -1123.0
        var_2 = module_0.load_list_of_tasks(float_0, list_1, float_1)
    except BaseException:
        pass

def test_case_8():
    try:
        set_0 = set()
        list_0 = [set_0, set_0, set_0]
        list_1 = [set_0, list_0]
        tuple_0 = None
        bytes_0 = b't\xb7\t\xd1\x02K%\xf3\xaf'
        var_0 = module_0.load_list_of_blocks(list_1, tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = None
        list_0 = [bytes_0, bytes_0]
        str_0 = 'f8._Ka \x0ci\t?U&dsw'
        var_0 = module_0.load_list_of_blocks(list_0, str_0)
        float_0 = 100.0
        str_1 = None
        dict_0 = {bytes_0: str_1}
        str_2 = 'V$QWH0y3>Eb.)UaZR9j'
        var_1 = module_0.load_list_of_blocks(float_0, dict_0, str_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'X'
        int_0 = 1
        int_1 = {str_0: int_0}
        int_2 = {str_0: int_1}
        int_3 = {str_0: int_2}
        int_4 = {str_0: int_3}
        int_5 = [int_2, int_4]
        bool_0 = False
        var_0 = module_0.load_list_of_tasks(int_5, int_1, int_1, int_1, int_1, bool_0, int_1, int_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'set_fact'
        str_1 = 'X'
        int_0 = 1
        int_1 = {str_1: int_0}
        int_2 = {str_0: int_1}
        int_3 = {str_1: int_0}
        int_4 = [int_2, int_3]
        bool_0 = False
        var_0 = module_0.load_list_of_tasks(int_4, int_1, int_1, int_1, int_1, bool_0, int_1, int_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'st\x0bB_fact'
        str_1 = 'X'
        int_0 = {}
        int_1 = 2
        int_2 = {str_1: int_1}
        int_3 = {str_0: int_2}
        int_4 = [int_0, int_3]
        var_0 = None
        bool_0 = False
        var_1 = module_0.load_list_of_tasks(int_4, var_0, var_0, var_0, var_0, bool_0, var_0, var_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'set_eacy'
        int_0 = 1
        int_1 = {str_0: int_0}
        int_2 = {str_0: int_1}
        int_3 = {}
        int_4 = {str_0: int_3}
        int_5 = [int_2, int_4]
        var_0 = module_0.load_list_of_tasks(int_5, int_3, int_5, int_5, int_5, str_0, int_5, int_5)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'X'
        int_0 = 1
        int_1 = {str_0: int_0}
        int_2 = {str_0: int_1, int_0: str_0}
        int_3 = {str_0: int_2}
        int_4 = {str_0: int_3}
        int_5 = [int_2, int_4]
        bool_0 = False
        var_0 = module_0.load_list_of_tasks(int_5, int_1, int_1, int_1, int_1, bool_0, int_1, int_1)
    except BaseException:
        pass