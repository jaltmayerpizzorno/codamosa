# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)

def test_case_2():
    int_0 = True
    list_0 = [int_0]
    bool_0 = False
    maybe_0 = module_0.Maybe(list_0, bool_0)

def test_case_3():
    object_0 = module_1.object()
    str_0 = '\n        Transform Box into Validation.\n\n        :returns: failed Validation monad with previous value as error\n        :rtype: Validation[None, [A]]\n        '
    bool_0 = False
    maybe_0 = module_0.Maybe(str_0, bool_0)
    bool_1 = maybe_0.__eq__(object_0)

def test_case_4():
    bytes_0 = b'vZ\x9d`\xf2\xa6\xed_\xbfB\x86\xb9\x1c\xd2\xbe\t \xf7\x85'
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)
    var_0 = maybe_0.bind(bytes_0)

def test_case_5():
    bytes_0 = b"h'Y\x8c\x87\xb9\xdf6\xdc\xda\xfa\xb7\x9e\xdc,T\x08 "
    bool_0 = True
    maybe_0 = module_0.Maybe(bytes_0, bool_0)
    dict_0 = {}
    var_0 = maybe_0.filter(dict_0)
    str_0 = '+Ou('
    str_1 = None
    str_2 = '008td,+&)Z'
    str_3 = None
    dict_1 = {str_0: bool_0, str_1: str_0, str_2: bytes_0, str_3: str_2}
    var_1 = maybe_0.map(dict_1)
    bool_1 = True
    maybe_1 = module_0.Maybe(maybe_0, bool_1)
    var_2 = maybe_1.to_try()

def test_case_6():
    int_0 = True
    bool_0 = False
    list_0 = [int_0]
    bool_1 = True
    maybe_0 = module_0.Maybe(list_0, bool_1)
    var_0 = maybe_0.ap(bool_0)
    var_1 = None
    maybe_1 = module_0.Maybe(var_1, bool_1)
    bool_2 = True
    maybe_2 = module_0.Maybe(int_0, bool_2)
    var_2 = maybe_2.to_either()
    str_0 = 'gt'
    var_3 = maybe_0.bind(str_0)

def test_case_7():
    var_0 = None
    str_0 = 'hLYc#cP;\x0c"}q'
    bool_0 = True
    maybe_0 = module_0.Maybe(str_0, bool_0)
    var_1 = maybe_0.filter(var_0)

def test_case_8():
    bool_0 = True
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    bool_1 = True
    maybe_0 = module_0.Maybe(object_0, bool_1)
    var_0 = maybe_0.get_or_else(bool_0)

def test_case_9():
    str_0 = 'GjCj%65U`px\x0ckYe{S'
    int_0 = -139
    bool_0 = False
    maybe_0 = module_0.Maybe(int_0, bool_0)
    bool_1 = True
    var_0 = maybe_0.to_either()
    maybe_1 = module_0.Maybe(str_0, bool_1)
    var_1 = maybe_1.to_validation()

def test_case_10():
    int_0 = False
    dict_0 = {int_0: int_0, int_0: int_0}
    bool_0 = False
    object_0 = None
    list_0 = [int_0]
    maybe_0 = module_0.Maybe(list_0, bool_0)
    var_0 = maybe_0.to_box()
    maybe_1 = module_0.Maybe(list_0, bool_0)
    bool_1 = maybe_1.__eq__(object_0)
    maybe_2 = module_0.Maybe(dict_0, bool_0)

def test_case_11():
    str_0 = ":X9j42'o+J@&jw"
    bool_0 = True
    maybe_0 = module_0.Maybe(str_0, bool_0)
    var_0 = maybe_0.to_box()

def test_case_12():
    tuple_0 = ()
    var_0 = None
    bool_0 = False
    maybe_0 = module_0.Maybe(var_0, bool_0)
    list_0 = [tuple_0, tuple_0]
    bool_1 = False
    maybe_1 = module_0.Maybe(list_0, bool_1)
    var_1 = maybe_1.to_lazy()