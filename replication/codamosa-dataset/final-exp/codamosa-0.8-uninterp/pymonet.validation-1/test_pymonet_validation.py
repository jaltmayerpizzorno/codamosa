# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    float_0 = -569.28623
    validation_0 = module_0.Validation(dict_0, float_0)

def test_case_2():
    int_0 = 446
    str_0 = '@k6Str3u-\x0cb!'
    float_0 = -697.01
    validation_0 = module_0.Validation(str_0, float_0)
    var_0 = validation_0.__eq__(int_0)

def test_case_3():
    int_0 = 5172
    str_0 = 'eM;(Z5@OXj>5w&UH3p$'
    list_0 = [str_0]
    validation_0 = module_0.Validation(int_0, list_0)
    var_0 = validation_0.__str__()

def test_case_4():
    float_0 = -1411.44
    bytes_0 = b'\x1a\x15%cz`\xecz\x07'
    validation_0 = module_0.Validation(float_0, bytes_0)
    var_0 = validation_0.is_fail()
    str_0 = '%*I?\nO)Iq%^N|\x0ct>1LPb'
    str_1 = ''
    validation_1 = module_0.Validation(str_0, str_1)

def test_case_5():
    float_0 = -26.39
    str_0 = 'p`,xf5ed8t.A'
    dict_0 = {str_0: str_0}
    validation_0 = module_0.Validation(str_0, dict_0)
    var_0 = validation_0.to_box()
    list_0 = [float_0, float_0]
    set_0 = {float_0, float_0}
    validation_1 = module_0.Validation(list_0, set_0)
    validation_2 = module_0.Validation(validation_1, list_0)
    var_1 = validation_2.__str__()