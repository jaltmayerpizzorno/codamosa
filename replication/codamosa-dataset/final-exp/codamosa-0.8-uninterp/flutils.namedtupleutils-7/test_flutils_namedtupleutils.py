# Automatically generated by Pynguin.
import flutils.namedtupleutils as module_0
import types as module_1
import collections as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Q'
    int_0 = 1
    int_1 = {int_0: int_0, int_0: str_0, str_0: int_0, str_0: int_0, int_0: int_0, str_0: int_0}
    var_0 = module_0.to_namedtuple(int_1)
    var_1 = module_0.to_namedtuple(var_0)

def test_case_2():
    str_0 = 'g/7z({gxSWd5\rf'
    str_1 = 'yX<YBY*OxC'
    dict_0 = {str_1: str_1, str_1: str_1, str_0: str_1, str_1: str_1}
    simple_namespace_0 = module_1.SimpleNamespace(**dict_0)
    int_0 = 1471
    tuple_0 = (simple_namespace_0, int_0)
    var_0 = module_0.to_namedtuple(tuple_0)

def test_case_3():
    dict_0 = {}
    simple_namespace_0 = module_1.SimpleNamespace(**dict_0)
    var_0 = module_0.to_namedtuple(simple_namespace_0)

def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)

def test_case_5():
    ordered_dict_0 = module_2.OrderedDict()
    list_0 = [ordered_dict_0]
    tuple_0 = (list_0,)
    var_0 = module_0.to_namedtuple(tuple_0)

def test_case_6():
    bool_0 = None
    dict_0 = {}
    simple_namespace_0 = module_1.SimpleNamespace(**dict_0)
    var_0 = module_0.to_namedtuple(simple_namespace_0)
    list_0 = [bool_0, var_0]
    simple_namespace_1 = module_1.SimpleNamespace(**dict_0)
    var_1 = module_0.to_namedtuple(list_0)