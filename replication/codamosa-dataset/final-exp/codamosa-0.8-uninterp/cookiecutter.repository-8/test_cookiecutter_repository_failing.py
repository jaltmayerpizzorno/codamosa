# Automatically generated by Pynguin.
import cookiecutter.repository as module_0

def test_case_0():
    try:
        int_0 = 1024
        var_0 = module_0.is_repo_url(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '0\r`mMtU\r?w9'
        str_1 = '5'
        complex_0 = None
        var_0 = module_0.determine_repo_dir(str_1, str_0, str_0, str_1, complex_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        int_0 = None
        tuple_0 = (int_0, set_0)
        str_0 = '_)^5uFaHU%F-eh[)B'
        list_0 = []
        var_0 = module_0.determine_repo_dir(set_0, tuple_0, str_0, tuple_0, list_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'\\;dK\t+~uCrG+.~{2"
        int_0 = -2685
        bool_0 = None
        str_1 = 'VTCmFLi"*<Ns'
        str_2 = 'cv27^x"d2>(n\t6p.zip'
        float_0 = -1370.476784
        float_1 = -1741.7
        bool_1 = False
        dict_0 = {bool_0: float_0, str_1: bool_0, float_1: bool_1, str_0: int_0}
        int_1 = 2
        str_3 = '0)`mmtu\r?w9.zip'
        str_4 = '\x0b;>8dzUfNjUQKHxF41E'
        var_0 = module_0.determine_repo_dir(str_2, dict_0, int_1, str_3, str_4)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '0)`mMtU\r?w9'
        complex_0 = None
        str_1 = 'sq_5UqmMicD~I_NO,A!'
        str_2 = 'ap@ohJw?[`'
        float_0 = -1582.50802
        var_0 = module_0.determine_repo_dir(str_2, str_0, complex_0, str_1, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '0)`mMtU\r?w9'
        str_1 = 'sq_5UqmMicD~I_NO,A!'
        str_2 = 'post_gen_project'
        set_0 = set()
        str_3 = '"n$^.'
        int_0 = 3
        str_4 = 'v3<rm_ej.zip.zip'
        list_0 = [str_4, str_0]
        var_0 = module_0.determine_repo_dir(str_1, set_0, str_3, int_0, list_0, list_0, str_2)
    except BaseException:
        pass