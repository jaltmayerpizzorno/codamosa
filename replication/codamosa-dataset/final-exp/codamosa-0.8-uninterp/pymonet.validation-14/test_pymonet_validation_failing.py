# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    try:
        str_0 = '-zMr8t|4jH6cGktJ'
        int_0 = None
        tuple_0 = None
        validation_0 = module_0.Validation(int_0, tuple_0)
        bool_0 = False
        validation_1 = module_0.Validation(str_0, bool_0)
        str_1 = None
        list_0 = [str_0, str_0, bool_0, str_1]
        var_0 = validation_1.map(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x8f\x00EIQ\x86m/\x9e\x17\x01\xa2\xd8\xaa*\xf7'
        bool_0 = False
        validation_0 = module_0.Validation(bytes_0, bool_0)
        list_0 = [validation_0, validation_0, validation_0, bytes_0]
        str_0 = '\x0c\nluh\x0cj>Hz+'
        validation_1 = module_0.Validation(list_0, str_0)
        var_0 = validation_1.to_either()
        str_1 = 'mVM[|4/CS[\\-wwxaq}al'
        dict_0 = {str_1: str_1}
        bool_1 = False
        tuple_0 = ()
        validation_2 = module_0.Validation(bool_1, tuple_0)
        var_1 = validation_2.bind(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "(K>&aYSZw'[O\x0c.2{"
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        set_0 = {str_0, str_0, str_0}
        validation_0 = module_0.Validation(dict_0, set_0)
        str_1 = ">9a=E'"
        list_0 = [validation_0, str_0, str_1, str_0]
        var_0 = validation_0.ap(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        bytes_0 = b'D\xbf\x1a\xb1\xe0FY\xf1\xc1\xd8\xf7\xd3\x12\xb9'
        validation_0 = module_0.Validation(bool_0, bytes_0)
        int_0 = 1301
        str_0 = 'Box[value={}]'
        validation_1 = module_0.Validation(int_0, str_0)
        var_0 = validation_0.to_maybe()
        var_1 = validation_1.to_either()
        bytes_1 = b'Ll\x11\x9f'
        var_2 = validation_0.to_try()
        var_3 = validation_1.__str__()
        tuple_0 = (str_0, bytes_1)
        str_1 = '&[^x?a|E)}H[Aw!5'
        validation_2 = module_0.Validation(tuple_0, str_1)
        var_4 = validation_1.__str__()
        complex_0 = None
        var_5 = validation_1.bind(complex_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        int_0 = 1034
        str_0 = 'Box[value={}]'
        validation_0 = module_0.Validation(int_0, str_0)
        var_0 = validation_0.to_either()
        bytes_0 = b'Ll\x11\x9f'
        var_1 = validation_0.__str__()
        tuple_0 = (str_0, bytes_0)
        str_1 = '&[^x?a|E)}H[Aw!5'
        validation_1 = module_0.Validation(tuple_0, str_1)
        var_2 = validation_1.__eq__(validation_0)
        list_1 = [list_0, list_0, list_0]
        int_1 = -2302
        validation_2 = module_0.Validation(list_1, int_1)
        var_3 = validation_0.__str__()
        int_2 = -2071
        validation_3 = module_0.Validation(str_0, int_2)
        complex_0 = None
        var_4 = validation_0.bind(complex_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        bytes_0 = b'D\xbf\x1a\xb1\xe0FY\xf1\xc1\xd8\xf7\xd3\x12\xb9'
        validation_0 = module_0.Validation(bool_0, bytes_0)
        list_0 = []
        int_0 = 1301
        str_0 = 'Box[value={}]'
        validation_1 = module_0.Validation(int_0, str_0)
        var_0 = validation_0.to_maybe()
        var_1 = validation_1.to_either()
        var_2 = validation_0.to_try()
        var_3 = validation_1.__str__()
        var_4 = validation_1.__eq__(validation_1)
        list_1 = [list_0, list_0, list_0]
        int_1 = -2302
        validation_2 = module_0.Validation(list_1, int_1)
        var_5 = validation_1.__str__()
        int_2 = -2071
        validation_3 = module_0.Validation(str_0, int_2)
        complex_0 = None
        var_6 = validation_1.bind(complex_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = -2402.9307
        str_0 = '\n        Returns new ImmutableList with only this elements that passed\n        info argument returns True\n\n        :param fn: function to call with ImmutableList value\n        :type fn: Function(A) -> bool\n        :returns: ImmutableList[A]\n        '
        tuple_0 = ()
        validation_0 = module_0.Validation(str_0, tuple_0)
        var_0 = validation_0.to_either()
        list_0 = [float_0]
        validation_1 = module_0.Validation(float_0, list_0)
    except BaseException:
        pass