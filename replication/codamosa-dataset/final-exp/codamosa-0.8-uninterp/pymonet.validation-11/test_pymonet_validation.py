# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    str_0 = 'BoD^dOCUh\x0c^`~!c*<'
    validation_0 = module_0.Validation(list_0, str_0)

def test_case_2():
    str_0 = '-2nX<[oP\x0c,[EjL:Rx'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    validation_0 = module_0.Validation(str_0, dict_0)
    var_0 = validation_0.to_maybe()

def test_case_3():
    str_0 = '\n        Transform Maybe to Either.\n\n        :returns: Right monad with previous value when Maybe is not empty, in other case Left with None\n        :rtype: Either[A | None]\n        '
    str_1 = 'Bu"'
    tuple_0 = (str_1,)
    list_0 = []
    validation_0 = module_0.Validation(list_0, tuple_0)
    var_0 = validation_0.to_either()
    validation_1 = module_0.Validation(str_0, tuple_0)
    var_1 = validation_0.to_maybe()

def test_case_4():
    str_0 = "u't"
    set_0 = set()
    float_0 = 2068.0
    validation_0 = module_0.Validation(set_0, float_0)
    validation_1 = module_0.Validation(str_0, validation_0)
    var_0 = validation_1.to_box()

def test_case_5():
    bool_0 = False
    bytes_0 = b'\xe8\x8c\xe0\x93H`\x05,'
    str_0 = '#d\rulz\n^\t].WN'
    int_0 = True
    str_1 = '\x0b1qQnN6/!'
    tuple_0 = (bytes_0, int_0, str_1, str_1)
    validation_0 = module_0.Validation(str_0, tuple_0)
    var_0 = validation_0.to_lazy()
    validation_1 = module_0.Validation(bool_0, bytes_0)
    var_1 = validation_1.to_box()

def test_case_6():
    str_0 = "\n        Take function and call constructor function passing returned value to fn function.\n\n        It's only way to call function store in Lazy\n        :param fn: Function(constructor_fn) -> B\n        :returns: result od folder function\n        :rtype: B\n        "
    bytes_0 = b'O\xbbH\xe2\xb8!#\xf3\x94\\\xb2\x8e\tb\x87\xa2\xb8\x0e'
    dict_0 = {str_0: str_0, bytes_0: str_0}
    str_1 = '&g~Kz0W=!>9'
    validation_0 = module_0.Validation(dict_0, str_1)
    var_0 = validation_0.is_fail()
    var_1 = validation_0.to_maybe()
    str_2 = 'Of$"w{y%\n\x0c=wdebcoh'
    var_2 = validation_0.__eq__(validation_0)
    var_3 = validation_0.to_try()
    validation_1 = module_0.Validation(bytes_0, str_2)
    var_4 = validation_1.__eq__(str_0)
    set_0 = {bytes_0, bytes_0}
    str_3 = 'Y'
    var_5 = validation_1.__eq__(str_3)
    list_0 = [bytes_0, set_0, set_0, set_0]
    validation_2 = module_0.Validation(list_0, set_0)
    var_6 = validation_0.__str__()

def test_case_7():
    str_0 = "\n        Take function and call constructor function passing returned value to fn function.\n\n        It's only way to call function store in Lazy\n        :param fn: Function(constructor_fn) -> B\n        :returns: result od folder function\n        :rtype: B\n        "
    dict_0 = {str_0: str_0, str_0: str_0}
    list_0 = [str_0, dict_0, str_0]
    validation_0 = module_0.Validation(dict_0, list_0)
    bool_0 = False
    float_0 = -1543.1
    validation_1 = module_0.Validation(bool_0, float_0)
    var_0 = validation_1.__eq__(validation_0)
    bytes_0 = b'O\xbbH\xe2\xb8!#\xf3\x94\\\xb2\x8e\tb\x87\xa2\xb8\x0e'
    dict_1 = {str_0: str_0, bytes_0: str_0}
    str_1 = '&g~KzsW=!>p'
    validation_2 = module_0.Validation(dict_1, str_1)
    var_1 = validation_2.to_maybe()
    str_2 = 'Of$"w{y%\n\x0c=wdebcoh'
    var_2 = validation_2.to_try()
    validation_3 = module_0.Validation(bytes_0, str_2)
    set_0 = {bytes_0}
    var_3 = validation_3.__eq__(str_2)
    list_1 = [bytes_0, set_0, set_0, set_0]
    bytes_1 = b'\x12\x0cG\xba\xa4L\xbb\xfd\xa47\x18\xe4\xa7\x7f\xf7,\xa6;\xbc'
    validation_4 = module_0.Validation(list_1, bytes_1)
    var_4 = validation_4.to_box()