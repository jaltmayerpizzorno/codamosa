# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0
import ansible.parsing.splitter as module_1

def test_case_0():
    try:
        str_0 = 'j\npmH'
        list_0 = [str_0, str_0]
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.parse_kv_args(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '?9u`'
        dict_0 = {str_0: str_0, str_0: lookup_module_0}
        var_0 = lookup_module_0.parse_kv_args(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Ao'
        str_1 = 'k*)#cm_'
        dict_0 = {str_0: str_0, str_1: str_0}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0, dict_0, **dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.sanity_check()
    except BaseException:
        pass

def test_case_4():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '6\rx;U5P%\t\\2U=!@E\x0cf'
        bool_0 = False
        var_0 = lookup_module_0.run(str_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.generate_sequence()
        var_1 = lookup_module_0.reset()
        var_2 = lookup_module_0.generate_sequence()
        var_3 = list(var_2)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '1\rp-/^3C8Ej\rHK$([>'
        str_1 = '\x0b2>=\tp'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
        str_2 = ']]3=pS~U.}y$}F@'
        set_0 = set()
        lookup_module_0 = module_0.LookupModule(set_0)
        var_0 = lookup_module_0.run(dict_0, str_2)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'Y:\\'
        set_0 = set()
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bytes_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = ''
        var_0 = module_1.parse_kv(str_0)
        var_1 = lookup_module_0.parse_kv_args(var_0)
        var_2 = module_1.parse_kv(str_0)
        var_3 = lookup_module_0.parse_kv_args(var_2)
        var_4 = lookup_module_0.reset()
        str_1 = 'start=5, end=5, format=test%d'
        var_5 = module_1.parse_kv(str_1)
        var_6 = lookup_module_0.parse_kv_args(var_5)
    except BaseException:
        pass

def test_case_9():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.reset()
        var_1 = lookup_module_0.sanity_check()
    except BaseException:
        pass

def test_case_10():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.reset()
        str_0 = '1'
        var_1 = dict(start=str_0, end=str_0)
        var_2 = lookup_module_0.parse_kv_args(var_1)
        var_3 = lookup_module_0.reset()
        int_0 = 5
        var_4 = lookup_module_0.parse_kv_args(int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '2-10/c'
        var_0 = lookup_module_0.parse_simple_args(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'O'
        var_0 = lookup_module_0.parse_simple_args(str_0)
        str_1 = '01kT'
        set_0 = {lookup_module_0, str_1, str_1, str_1}
        var_1 = lookup_module_0.run(str_1, set_0)
    except BaseException:
        pass

def test_case_13():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '5'
        dict_0 = {str_0: lookup_module_0}
        list_0 = []
        var_0 = lookup_module_0.run(dict_0, list_0)
        lookup_module_1 = module_0.LookupModule()
        var_1 = lookup_module_0.sanity_check()
        str_1 = '2A-10/2'
        var_2 = lookup_module_1.parse_simple_args(str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = 4
        str_0 = 'test'
        var_0 = dict(start=int_0, count=int_1, stride=int_2, end=int_3, format=str_0)
        lookup_module_0 = module_0.LookupModule()
        str_1 = ''
        var_1 = lookup_module_0.parse_simple_args(str_1)
        str_2 = 'start=1 end=2 format=test'
        str_3 = [str_2]
        var_2 = {}
        var_3 = lookup_module_0.run(str_3, var_2)
    except BaseException:
        pass