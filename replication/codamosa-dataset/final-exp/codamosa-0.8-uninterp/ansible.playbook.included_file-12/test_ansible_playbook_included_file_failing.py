# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0
import ansible.utils.display as module_1

def test_case_0():
    try:
        int_0 = -1364
        bytes_0 = b'\x9aO\xa4\x1e\x94\xb5:-\xdb\x8bR\x01\xe2\x88\n\xf3\xb8'
        bool_0 = False
        str_0 = 'Oa^`XK&F]Qj+\nr?'
        included_file_0 = module_0.IncludedFile(int_0, bytes_0, bool_0, str_0, int_0)
        var_0 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 708
        bytes_0 = b'\x046V\xf4A\xd2DF\xfbf\xca\xcb\xd2'
        str_0 = 'GUIDELINES'
        set_0 = {str_0}
        included_file_0 = module_0.IncludedFile(bytes_0, str_0, set_0, bytes_0)
        var_0 = included_file_0.__eq__(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'O6IO5VsCd.q{j(G'
        bytes_0 = b'\x85\xbe;\xe8\xee\xb33\xcb\x15q\xf1\xddz\xbci2\x80e\n\xa6'
        bytes_1 = b'\x10\xbd\xa7jT\x9b\x1a\xb7\xc6\x8ft\x829\x8d\xf6\x11\t/E'
        bytes_2 = b'"y\xa3Q\x12\x15\x069\x88\xe3g'
        int_0 = 1446
        str_1 = 'R& \x0cqc{50$:mR\n'
        float_0 = 1264.6
        str_2 = 'pkg_mgr'
        dict_0 = {str_2: str_1, int_0: float_0}
        included_file_0 = module_0.IncludedFile(int_0, str_1, float_0, str_2, dict_0)
        var_0 = included_file_0.process_include_results(str_0, bytes_0, bytes_1, bytes_2)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        str_0 = 'i"u\'7t\x0bfPr.:UV{'
        str_1 = '.9K\x0bk7X'
        int_0 = -1605
        float_0 = 184.031501
        bool_0 = False
        included_file_0 = module_0.IncludedFile(tuple_0, int_0, float_0, bool_0)
        bytes_0 = None
        var_0 = included_file_0.add_host(bytes_0)
        str_2 = '(I@(g\t<iYxTL_-mP5x'
        int_1 = -1692
        bool_1 = True
        var_1 = included_file_0.__repr__()
        included_file_1 = module_0.IncludedFile(int_1, tuple_0, float_0, bool_1, float_0)
        included_file_2 = module_0.IncludedFile(str_0, tuple_0, str_1, str_2, included_file_1)
        var_2 = included_file_2.__repr__()
        str_3 = '=#|j'
        included_file_3 = module_0.IncludedFile(str_0, str_3, included_file_1, included_file_1)
        dict_0 = None
        var_3 = included_file_0.add_host(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        str_0 = 'i"u\'7t\x0bfPr.:UV{'
        str_1 = '.9K\x0bk7X'
        int_0 = -1605
        float_0 = 184.031501
        bool_0 = False
        included_file_0 = module_0.IncludedFile(tuple_0, int_0, float_0, bool_0)
        bytes_0 = None
        var_0 = included_file_0.add_host(bytes_0)
        str_2 = '(I@(g\t<iYxTL_-mP5x'
        int_1 = -1692
        var_1 = included_file_0.__repr__()
        included_file_1 = module_0.IncludedFile(str_0, tuple_0, str_1, str_2, included_file_0)
        str_3 = '=#|j'
        included_file_2 = module_0.IncludedFile(str_0, str_3, included_file_0, included_file_0)
        var_2 = included_file_1.process_include_results(tuple_0, str_2, included_file_0, int_1)
        var_3 = included_file_1.__eq__(included_file_2)
        str_4 = '+\t4|W\\`xs`T)|:seY='
        int_2 = 4205
        float_1 = 0.5
        dict_0 = {str_0: float_1}
        display_0 = module_1.Display(dict_0)
        var_4 = included_file_1.process_include_results(str_4, int_2, display_0, bool_0)
    except BaseException:
        pass