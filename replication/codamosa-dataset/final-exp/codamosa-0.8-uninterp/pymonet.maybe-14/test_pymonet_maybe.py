# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    maybe_0 = module_0.Maybe(bool_0, bool_0)
    var_0 = maybe_0.to_validation()

def test_case_2():
    object_0 = module_1.object()
    int_0 = 2623
    bool_0 = False
    maybe_0 = module_0.Maybe(int_0, bool_0)
    bool_1 = maybe_0.__eq__(object_0)

def test_case_3():
    float_0 = 129.0254
    bool_0 = True
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_0 = maybe_0.to_lazy()
    var_1 = maybe_0.to_try()
    list_0 = [float_0]
    list_1 = []
    var_2 = maybe_0.map(list_1)
    var_3 = maybe_0.map(list_0)
    var_4 = maybe_0.to_either()
    var_5 = maybe_0.to_either()

def test_case_4():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    object_0 = module_1.object()
    str_0 = '{& 8Hl"faF\').3\r\tcmr'
    str_1 = None
    list_0 = []
    dict_1 = {str_0: str_0, str_1: list_0, str_0: list_0}
    maybe_0 = module_0.Maybe(dict_1, bool_0)
    bool_1 = maybe_0.__eq__(object_0)
    str_2 = 'Wgd>~#=eCLP]^2.$`.\t'
    dict_2 = {str_2: str_2, str_2: str_2}
    bool_2 = True
    maybe_1 = module_0.Maybe(dict_2, bool_2)
    var_0 = maybe_1.bind(dict_0)

def test_case_5():
    int_0 = -1486
    dict_0 = {}
    bool_0 = True
    maybe_0 = module_0.Maybe(dict_0, bool_0)
    var_0 = maybe_0.to_try()
    dict_1 = {int_0: int_0, int_0: int_0, int_0: int_0}
    list_0 = [dict_1, int_0]
    str_0 = '&\\B~X?f(pkE\rBTI]x'
    dict_2 = {str_0: str_0}
    bool_1 = True
    maybe_1 = module_0.Maybe(dict_2, bool_1)
    var_1 = maybe_1.get_or_else(list_0)

def test_case_6():
    bool_0 = False
    tuple_0 = (bool_0,)
    maybe_0 = module_0.Maybe(tuple_0, bool_0)
    var_0 = maybe_0.to_validation()
    str_0 = '\n        Returns new ImmutableList with only this elements that passed\n        info argument returns True\n\n        :param fn: function to call with ImmutableList value\n        :type fn: Function(A) -> bool\n        :returns: ImmutableList[A]\n        '
    bool_1 = False
    maybe_1 = module_0.Maybe(str_0, bool_1)
    var_1 = maybe_1.to_box()

def test_case_7():
    float_0 = 1181.3812
    set_0 = {float_0, float_0}
    bool_0 = True
    maybe_0 = module_0.Maybe(set_0, bool_0)
    list_0 = [maybe_0]
    bool_1 = True
    maybe_1 = module_0.Maybe(list_0, bool_1)
    var_0 = maybe_1.to_box()
    object_0 = module_1.object()
    dict_0 = {}
    bool_2 = True
    maybe_2 = module_0.Maybe(dict_0, bool_2)
    var_1 = maybe_2.map(object_0)
    float_1 = -72.62709
    var_2 = maybe_2.get_or_else(float_1)

def test_case_8():
    str_0 = '2IJ\n1a9Xc!0al]fe'
    list_0 = [str_0]
    bool_0 = False
    maybe_0 = module_0.Maybe(list_0, bool_0)
    var_0 = maybe_0.to_try()

def test_case_9():
    str_0 = '\n        :param semigroup: other semigroup to concat\n        :type semigroup: All[B]\n        :returns: new All with last truly value or first falsy\n        :rtype: All[A | B]\n        '
    str_1 = 'H{|9kY'
    str_2 = None
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_2: str_0}
    bool_0 = True
    maybe_0 = module_0.Maybe(dict_0, bool_0)
    var_0 = maybe_0.to_try()

def test_case_10():
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)
    var_0 = maybe_0.to_validation()

def test_case_11():
    int_0 = 1
    bool_0 = False
    maybe_0 = module_0.Maybe(int_0, bool_0)
    str_0 = '1'
    maybe_1 = module_0.Maybe(str_0, bool_0)
    var_0 = maybe_0 == maybe_1
    maybe_2 = module_0.Maybe(str_0, bool_0)
    maybe_3 = module_0.Maybe(str_0, bool_0)
    var_1 = maybe_2 == maybe_3
    maybe_4 = module_0.Maybe(str_0, bool_0)
    str_1 = '2'
    maybe_5 = module_0.Maybe(str_1, bool_0)
    var_2 = maybe_4 == maybe_5
    maybe_6 = module_0.Maybe(str_0, bool_0)
    bool_1 = True
    maybe_7 = module_0.Maybe(str_0, bool_1)
    var_3 = maybe_6 == maybe_7
    bool_2 = True
    maybe_8 = module_0.Maybe(str_0, bool_2)
    maybe_9 = module_0.Maybe(str_0, bool_0)
    var_4 = maybe_8 == maybe_9
    bool_3 = True
    maybe_10 = module_0.Maybe(str_0, bool_3)
    bool_4 = True
    maybe_11 = module_0.Maybe(str_0, bool_4)
    var_5 = maybe_10 == maybe_11