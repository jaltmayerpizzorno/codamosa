# Automatically generated by Pynguin.
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

def test_case_0():
    simple_namespace_0 = module_0.SimpleNamespace()
    var_0 = module_1.to_namedtuple(simple_namespace_0)

def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
    var_0 = module_1.to_namedtuple(list_0)

def test_case_2():
    float_0 = 2536.87741
    str_0 = '*KFds+,v @Z0\t)t'
    dict_0 = {str_0: float_0, str_0: float_0}
    tuple_0 = (float_0, float_0, dict_0, str_0)
    var_0 = module_1.to_namedtuple(tuple_0)

def test_case_3():
    int_0 = 1448
    var_0 = dict(a=int_0, b=int_0)
    var_1 = module_1.to_namedtuple(var_0)
    var_2 = module_1.to_namedtuple(var_1)

def test_case_4():
    float_0 = 1268.207
    bytes_0 = b'a\xa5\x9e\x9b{\r\xd9E\xac\xd3'
    tuple_0 = (float_0, bytes_0)
    var_0 = module_1.to_namedtuple(tuple_0)

def test_case_5():
    var_0 = []
    var_1 = module_1.to_namedtuple(var_0)
    var_2 = ()
    ordered_dict_0 = module_2.OrderedDict()
    str_0 = 'x'
    str_1 = ''
    var_3 = module_2.namedtuple(str_0, str_1)
    var_4 = module_1.to_namedtuple(var_2)
    ordered_dict_1 = module_2.OrderedDict()
    var_5 = module_2.namedtuple(str_0, str_1)
    ordered_dict_2 = module_2.OrderedDict()
    var_6 = ()
    var_7 = module_2.namedtuple(str_0, str_1)
    var_8 = [ordered_dict_2, var_6, var_7]
    var_9 = module_1.to_namedtuple(var_8)
    ordered_dict_3 = module_2.OrderedDict()
    var_10 = module_2.namedtuple(str_0, str_1)
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    var_11 = module_1.to_namedtuple(int_3)
    int_4 = (int_0, int_1, int_2)
    var_12 = module_1.to_namedtuple(int_4)