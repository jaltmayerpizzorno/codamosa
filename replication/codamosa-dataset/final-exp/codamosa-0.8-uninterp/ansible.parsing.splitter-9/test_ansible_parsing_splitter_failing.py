# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.parse_kv(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'SL"\n&#BM'
        int_0 = -752
        var_0 = module_0.parse_kv(str_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '<3i`Ba$349<"(['
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '!-]i}Pfa\n9m/cbmF5Qyi'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.join_args(dict_0)
        var_1 = module_0.parse_kv(str_0)
        float_0 = None
        var_2 = module_0.join_args(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "'a=b' c='d e' f='g'"
        var_0 = module_0.parse_kv(str_0)
        bytes_0 = b'\xfb'
        var_1 = module_0.parse_kv(bytes_0)
        str_1 = '~yi"`UQ\'_|&v$r'
        var_2 = module_0.parse_kv(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\nE'
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'key=value'
        var_0 = module_0.parse_kv(str_0)
        var_1 = module_0.parse_kv(str_0)
        var_2 = module_0.parse_kv(str_0)
        str_1 = 'Fkpym{{B\x0bfn4,n7~'
        var_3 = module_0.parse_kv(str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'wu{{>k$91%!Hf\nBrCs)'
        str_1 = 'TL'
        var_0 = module_0.parse_kv(str_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'key=value'
        str_1 = 'D9+OZ&dG'
        var_0 = module_0.parse_kv(str_0)
        var_1 = module_0.parse_kv(str_0)
        str_2 = "key ='val :e'"
        str_3 = 'r\\='
        var_2 = module_0.parse_kv(str_3)
        var_3 = module_0.parse_kv(str_2)
        str_4 = 'M=cwXl\tJmTV'
        str_5 = '--allmatches'
        var_4 = module_0.parse_kv(str_4, str_5)
        var_5 = module_0.parse_kv(str_1)
    except BaseException:
        pass