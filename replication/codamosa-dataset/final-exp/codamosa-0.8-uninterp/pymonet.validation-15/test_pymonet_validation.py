# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n        Transform Box into Validation.\n\n        :returns: failed Validation monad with previous value as error\n        :rtype: Validation[None, [A]]\n        '
    validation_0 = module_0.Validation(str_0, str_0)

def test_case_2():
    set_0 = set()
    float_0 = 330.2
    validation_0 = module_0.Validation(set_0, float_0)
    dict_0 = {}
    str_0 = 'O2$k;_\r'
    validation_1 = module_0.Validation(dict_0, str_0)
    var_0 = validation_1.__eq__(validation_0)

def test_case_3():
    float_0 = -481.990371
    str_0 = 'XUKS_{Z?'
    validation_0 = module_0.Validation(float_0, str_0)
    list_0 = [str_0]
    validation_1 = module_0.Validation(validation_0, list_0)
    var_0 = validation_1.__str__()

def test_case_4():
    bytes_0 = b"+\xa7m\xb22w\xe8'\xb3?"
    str_0 = '#|m1=_Re&\r~'
    validation_0 = module_0.Validation(bytes_0, str_0)
    var_0 = validation_0.__str__()
    var_1 = validation_0.to_maybe()
    var_2 = validation_0.is_success()

def test_case_5():
    tuple_0 = ()
    float_0 = 352.0
    validation_0 = module_0.Validation(float_0, tuple_0)
    var_0 = validation_0.to_maybe()
    validation_1 = module_0.Validation(tuple_0, tuple_0)
    var_1 = validation_1.is_success()

def test_case_6():
    str_0 = 'AS<\x0bw+5P0lFvTK-$/4kT'
    list_0 = [str_0, str_0]
    validation_0 = module_0.Validation(str_0, list_0)
    var_0 = validation_0.to_lazy()

def test_case_7():
    bytes_0 = b'\x9c\xed\x85'
    bool_0 = True
    float_0 = -41.0
    str_0 = 'PYSRkL0L#'
    int_0 = -6002
    validation_0 = module_0.Validation(str_0, int_0)
    var_0 = validation_0.to_box()
    validation_1 = module_0.Validation(float_0, bool_0)
    set_0 = {bytes_0}
    int_1 = None
    bool_1 = True
    tuple_0 = (set_0, bytes_0, int_1, bool_1)
    validation_2 = module_0.Validation(set_0, tuple_0)
    var_1 = validation_2.to_lazy()

def test_case_8():
    int_0 = True
    bytes_0 = b'*\x7fQ\x18\xb4'
    list_0 = []
    validation_0 = module_0.Validation(bytes_0, list_0)
    var_0 = validation_0.to_either()
    str_0 = 'PNz^]U0S~b&>hYeM\n'
    validation_1 = module_0.Validation(int_0, str_0)
    var_1 = validation_1.to_lazy()
    var_2 = validation_1.to_either()

def test_case_9():
    bytes_0 = b"+\xa7m\xb22w\xe8'\xb3?"
    str_0 = '#|m1=_Re&\r~'
    int_0 = -26
    validation_0 = module_0.Validation(int_0, int_0)
    validation_1 = module_0.Validation(bytes_0, str_0)
    var_0 = validation_1.__str__()
    var_1 = validation_1.to_try()
    bool_0 = None
    float_0 = 461.0804
    var_2 = validation_1.__eq__(validation_1)
    set_0 = {bool_0}
    dict_0 = {bytes_0: set_0, bytes_0: set_0}
    validation_2 = module_0.Validation(dict_0, bytes_0)
    var_3 = validation_2.is_fail()
    var_4 = validation_2.to_maybe()
    validation_3 = module_0.Validation(set_0, bytes_0)
    var_5 = validation_3.to_maybe()
    str_1 = ":D\x0be%XueL'ZOB{e"
    var_6 = validation_3.is_success()
    var_7 = validation_2.__str__()
    validation_4 = module_0.Validation(bool_0, str_1)
    tuple_0 = (float_0,)
    var_8 = validation_2.__eq__(tuple_0)