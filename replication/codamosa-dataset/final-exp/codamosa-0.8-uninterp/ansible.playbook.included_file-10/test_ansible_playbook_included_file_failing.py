# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0

def test_case_0():
    try:
        str_0 = 'filename'
        included_file_0 = module_0.IncludedFile(str_0, str_0, str_0, str_0, str_0)
        var_0 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'filename'
        str_1 = 'args'
        str_2 = 'is_role'
        included_file_0 = module_0.IncludedFile(str_0, str_1, str_1, str_1, str_2)
        var_0 = included_file_0.add_host(str_1)
        var_1 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'L{yo*\x0b[)'
        list_0 = [str_0, str_0, str_0]
        bool_0 = False
        float_0 = 1129.346
        dict_0 = {}
        int_0 = 214
        str_1 = '\x0b?[JE-?['
        str_2 = '<\nq=bPk/rf3@@\nwA'
        bytes_0 = b'\xb8\xed-7\x93wW{\x1b\xdf\x91\x18\xb7\xf7\xd0\xd7\x0c\xd7'
        tuple_0 = (bytes_0,)
        str_3 = 'q_I]6BB\x0bz hU\x0ba'
        tuple_1 = (tuple_0, str_3)
        included_file_0 = module_0.IncludedFile(dict_0, int_0, str_1, str_2, tuple_1)
        var_0 = included_file_0.process_include_results(str_0, list_0, bool_0, float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'filename'
        str_1 = 'args'
        str_2 = 'task'
        str_3 = 'is_role'
        included_file_0 = module_0.IncludedFile(str_0, str_1, str_2, str_2, str_3)
        str_4 = 'hosts'
        var_0 = included_file_0.add_host(str_4)
        var_1 = included_file_0.add_host(str_4)
    except BaseException:
        pass