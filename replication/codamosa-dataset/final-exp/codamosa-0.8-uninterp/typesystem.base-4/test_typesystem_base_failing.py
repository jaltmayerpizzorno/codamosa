# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    try:
        parse_error_0 = module_0.ParseError()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '#/'
        str_1 = "z7)p*.'F2{"
        message_0 = module_0.Message(text=str_0, code=str_0, end_position=str_1)
        str_2 = message_0.__repr__()
        int_0 = message_0.__hash__()
        base_error_0 = module_0.BaseError(key=str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ' \x0c%Eu.Q:TyayjXe'
        str_1 = 'Rlf$d\rQ'
        message_0 = module_0.Message(text=str_1, key=str_0)
        int_0 = message_0.__hash__()
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()
        int_1 = 3
        int_2 = -675
        position_0 = module_0.Position(int_1, int_2, int_2)
        message_1 = module_0.Message(text=str_0, index=iterator_0, position=position_0)
        str_2 = message_1.__repr__()
        str_3 = "v!]L*N'9D\\HIKV\t~{\n"
        base_error_0 = module_0.BaseError(text=str_3, code=str_3)
        message_2 = module_0.Message(text=str_3)
        int_3 = base_error_0.__hash__()
        int_4 = base_error_0.__hash__()
        list_0 = [message_2, message_2, message_2]
        parse_error_0 = module_0.ParseError(text=str_3, key=str_3, messages=list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 2906
        validation_result_0 = module_0.ValidationResult()
        int_1 = None
        str_0 = validation_result_0.__repr__()
        validation_error_0 = None
        int_2 = -19
        validation_result_1 = module_0.ValidationResult(error=validation_error_0)
        iterator_0 = validation_result_1.__iter__()
        position_0 = module_0.Position(int_0, int_1, int_2)
        str_1 = 'Must be less than {exclusive_maximum}.'
        message_0 = module_0.Message(text=str_1, code=str_1, start_position=position_0)
        str_2 = message_0.__repr__()
        str_3 = validation_result_0.__repr__()
        bool_0 = position_0.__eq__(message_0)
        int_3 = message_0.__hash__()
        base_error_0 = module_0.BaseError(text=str_1)
        tuple_0 = (validation_error_0, message_0, base_error_0)
        str_4 = position_0.__repr__()
        base_error_1 = module_0.BaseError(text=tuple_0, code=str_1, key=int_0)
        parse_error_0 = module_0.ParseError(code=str_4, position=position_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '#z4vq;`1^<<V&:\x0cm'
        validation_error_0 = module_0.ValidationError(text=str_0, code=str_0)
        base_error_0 = module_0.BaseError()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -1633
        bool_0 = False
        base_error_0 = module_0.BaseError(code=int_0, messages=bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 2586
        int_1 = -1355
        int_2 = 1090
        position_0 = module_0.Position(int_0, int_1, int_2)
        int_3 = 3215
        int_4 = -647
        int_5 = -2661
        position_1 = module_0.Position(int_4, int_3, int_5)
        str_0 = position_1.__repr__()
        validation_error_0 = module_0.ValidationError(text=str_0, position=position_0)
        base_error_0 = module_0.BaseError(key=str_0, messages=str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Field'
        validation_result_0 = module_0.ValidationResult()
        dict_0 = {validation_result_0: validation_result_0, str_0: str_0}
        message_0 = module_0.Message(text=str_0, end_position=dict_0)
        list_0 = [message_0, validation_result_0, dict_0]
        base_error_0 = module_0.BaseError(messages=list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 1397
        int_1 = 2586
        int_2 = -1355
        int_3 = 1090
        position_0 = module_0.Position(int_1, int_2, int_3)
        validation_result_0 = module_0.ValidationResult(value=position_0)
        bool_0 = validation_result_0.__bool__()
        int_4 = -990
        int_5 = -1468
        int_6 = 2822
        position_1 = module_0.Position(int_5, int_5, int_6)
        base_error_0 = module_0.BaseError(text=int_0, position=position_1)
        iterator_0 = base_error_0.__iter__()
        int_7 = 1587
        position_2 = module_0.Position(int_0, int_4, int_7)
        base_error_1 = module_0.BaseError(position=position_2)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'QPA1p@]6_K\\"Wq'
        list_0 = [str_0]
        list_1 = []
        int_0 = 2
        base_error_0 = module_0.BaseError(text=list_1, key=int_0)
        var_0 = base_error_0.__getitem__(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -2158
        str_0 = 'b]3lk)\x0cK=Dl__{'
        position_0 = module_0.Position(int_0, int_0, int_0)
        base_error_0 = module_0.BaseError(text=str_0, code=str_0, position=position_0)
        str_1 = base_error_0.__repr__()
        set_0 = {int_0, str_0, base_error_0}
        message_0 = module_0.Message(text=str_0, code=str_0, key=int_0, start_position=set_0, end_position=position_0)
        int_1 = message_0.__hash__()
        base_error_1 = module_0.BaseError(key=int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()
        bool_0 = validation_result_0.__bool__()
        str_0 = '_}5f+\n&E<X'
        parse_error_0 = module_0.ParseError(code=str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 2
        validation_result_0 = module_0.ValidationResult()
        bool_0 = validation_result_0.__bool__()
        validation_result_1 = module_0.ValidationResult()
        str_0 = validation_result_1.__repr__()
        int_1 = -1422
        position_0 = module_0.Position(int_1, int_0, int_1)
        base_error_0 = module_0.BaseError()
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b''
        str_0 = '<2V&j}nd(d'
        validation_result_0 = module_0.ValidationResult()
        message_0 = module_0.Message(text=str_0, code=str_0, key=str_0, position=validation_result_0)
        bool_0 = message_0.__eq__(bytes_0)
        parse_error_0 = module_0.ParseError(code=str_0, key=str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '\t)lR'
        int_0 = 3
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_0, code=str_0, end_position=position_0)
        str_1 = message_0.__repr__()
        validation_result_0 = module_0.ValidationResult()
        str_2 = position_0.__repr__()
        str_3 = 'XrBQft%4NmI'
        base_error_0 = module_0.BaseError(position=position_0, messages=str_3)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'Not a valid choice.'
        int_0 = -4122
        int_1 = 1030
        position_0 = module_0.Position(int_0, int_0, int_1)
        message_0 = module_0.Message(text=str_0, end_position=position_0)
        list_0 = [message_0]
        base_error_0 = module_0.BaseError(text=str_0, key=str_0, position=position_0, messages=list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        validation_result_0 = module_0.ValidationResult()
        str_0 = 'Id9RY|y1EHM:'
        validation_error_0 = None
        tuple_0 = (validation_error_0,)
        int_0 = 1
        int_1 = 3
        int_2 = 1925
        position_0 = module_0.Position(int_0, int_1, int_2)
        message_0 = module_0.Message(text=str_0, index=tuple_0, position=position_0, end_position=position_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'HfYx;Z}&V;^~'
        parse_error_0 = module_0.ParseError(text=str_0)
        str_1 = 'field_id'
        int_0 = 4900
        int_1 = 1
        position_0 = module_0.Position(int_0, int_1, int_1)
        message_0 = module_0.Message(text=str_0, position=str_1, start_position=position_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'f"Bv>H'
        base_error_0 = module_0.BaseError(text=str_0)
        str_1 = base_error_0.__repr__()
        int_0 = 2
        list_0 = base_error_0.messages()
        message_0 = module_0.Message(text=str_0, index=int_0)
        base_error_1 = module_0.BaseError(messages=list_0)
        int_1 = 2194
        position_0 = module_0.Position(int_0, int_1, int_1)
        str_2 = position_0.__repr__()
        str_3 = message_0.__repr__()
        str_4 = 'boolean'
        validation_result_0 = module_0.ValidationResult(error=str_4)
        str_5 = validation_result_0.__repr__()
        str_6 = base_error_0.__str__()
        int_2 = message_0.__hash__()
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 4
        str_0 = '8q,ymR87+X]5^"U]n1U'
        int_1 = 1
        list_0 = [int_0]
        message_0 = module_0.Message(text=str_0, key=int_1, index=list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'y]W\rBG4'
        int_0 = None
        position_0 = module_0.Position(int_0, int_0, int_0)
        int_1 = 4314
        int_2 = 1975
        position_1 = module_0.Position(int_1, int_1, int_2)
        message_0 = module_0.Message(text=str_0, key=str_0, position=position_1)
        str_1 = message_0.__repr__()
        str_2 = position_1.__repr__()
        iterator_0 = None
        dict_0 = {}
        str_3 = position_1.__repr__()
        base_error_0 = module_0.BaseError(text=dict_0)
        bool_0 = base_error_0.__eq__(iterator_0)
        str_4 = 'unique_items'
        int_3 = 3
        int_4 = 1
        position_2 = module_0.Position(int_3, int_4, int_3)
        parse_error_0 = module_0.ParseError(text=str_4)
        message_1 = module_0.Message(text=str_4, code=str_4, index=str_4)
        int_5 = message_1.__hash__()
        validation_result_0 = module_0.ValidationResult()
        iterator_1 = validation_result_0.__iter__()
        int_6 = message_1.__hash__()
        int_7 = 3595
        position_3 = module_0.Position(int_7, int_5, int_3)
        message_2 = module_0.Message(text=str_4, key=int_6, start_position=position_1)
        bool_1 = message_2.__eq__(int_4)
        int_8 = base_error_0.__hash__()
        str_5 = None
        list_0 = [message_1]
        base_error_1 = module_0.BaseError(code=str_5, messages=list_0)
        base_error_2 = module_0.BaseError()
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'y]W\rBG4'
        int_0 = None
        position_0 = module_0.Position(int_0, int_0, int_0)
        int_1 = 4314
        int_2 = 1975
        position_1 = module_0.Position(int_1, int_1, int_2)
        message_0 = module_0.Message(text=str_0, key=str_0, position=position_1)
        str_1 = message_0.__repr__()
        str_2 = position_1.__repr__()
        iterator_0 = None
        dict_0 = {}
        str_3 = position_1.__repr__()
        base_error_0 = module_0.BaseError(text=dict_0)
        bool_0 = base_error_0.__eq__(iterator_0)
        list_0 = []
        parse_error_0 = module_0.ParseError(messages=list_0)
    except BaseException:
        pass

def test_case_22():
    try:
        float_0 = -71.05
        int_0 = -1889
        int_1 = 1
        str_0 = "\n    Doesn't ever match.\n    "
        bytes_0 = b''
        list_0 = [int_1, int_0, float_0, bytes_0]
        validation_error_0 = module_0.ValidationError(text=str_0, code=str_0, position=list_0)
        validation_result_0 = module_0.ValidationResult(value=bytes_0, error=validation_error_0)
    except BaseException:
        pass

def test_case_23():
    try:
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()
        bool_0 = validation_result_0.__bool__()
        int_0 = 3
        optional_0 = None
        none_type_0 = None
        str_0 = '[`s'
        base_error_0 = module_0.BaseError(text=str_0, code=str_0, key=int_0)
        int_1 = base_error_0.__hash__()
        str_1 = base_error_0.__repr__()
        base_error_1 = module_0.BaseError(key=int_0, position=optional_0, messages=none_type_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '0`r\x0c\ns'
        message_0 = module_0.Message(text=str_0, key=str_0)
        list_0 = [message_0, message_0, message_0]
        validation_result_0 = module_0.ValidationResult()
        str_1 = validation_result_0.__repr__()
        validation_error_0 = module_0.ValidationError(messages=list_0)
        validation_result_1 = module_0.ValidationResult(error=validation_error_0)
        bool_0 = validation_result_1.__bool__()
        str_2 = validation_result_1.__repr__()
        base_error_0 = module_0.BaseError(messages=validation_error_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'y]W\rBG4'
        int_0 = None
        validation_result_0 = module_0.ValidationResult()
        position_0 = module_0.Position(int_0, int_0, int_0)
        bool_0 = validation_result_0.__bool__()
        int_1 = 4314
        str_1 = validation_result_0.__repr__()
        int_2 = 1975
        position_1 = module_0.Position(int_1, int_1, int_2)
        message_0 = module_0.Message(text=str_0, key=str_0, position=position_1)
        str_2 = message_0.__repr__()
        str_3 = position_1.__repr__()
        str_4 = 'unique_items'
        parse_error_0 = module_0.ParseError(text=str_4)
        message_1 = module_0.Message(text=str_4, code=str_4, index=str_4)
        iterator_0 = validation_result_0.__iter__()
        int_3 = message_1.__hash__()
        bool_1 = message_0.__eq__(message_1)
        bool_2 = validation_result_0.__bool__()
        base_error_0 = module_0.BaseError(position=position_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'y]W\rBG4'
        int_0 = None
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_0, code=str_0, start_position=position_0, end_position=position_0)
        message_1 = module_0.Message(text=str_0, code=str_0, key=str_0, position=position_0)
        list_0 = [message_0, message_1]
        base_error_0 = module_0.BaseError(messages=list_0)
        int_1 = base_error_0.__len__()
        int_2 = 4314
        int_3 = 1975
        position_1 = module_0.Position(int_2, int_2, int_3)
        message_2 = module_0.Message(text=str_0, key=str_0, position=position_1)
        str_1 = message_2.__repr__()
        iterator_0 = None
        str_2 = position_1.__repr__()
        bool_0 = base_error_0.__eq__(iterator_0)
        str_3 = 'unique_items'
        int_4 = 3
        int_5 = 1
        position_2 = module_0.Position(int_4, int_5, int_4)
        parse_error_0 = module_0.ParseError(text=str_3)
        message_3 = module_0.Message(text=str_3, code=str_3, index=str_3)
        str_4 = 'B.x>,eA/U{l\ni\x0bc]<LM+'
        message_4 = module_0.Message(text=str_2, code=str_4)
        int_6 = message_2.__hash__()
        str_5 = 'o$]x\x0bfAEEfoNL<59*\\t'
        validation_result_0 = module_0.ValidationResult(error=str_5)
        iterator_1 = base_error_0.__iter__()
        bool_1 = message_2.__eq__(message_1)
        int_7 = base_error_0.__hash__()
        bool_2 = validation_result_0.__bool__()
        str_6 = base_error_0.__str__()
        str_7 = 'value'
        base_error_1 = module_0.BaseError(code=str_7)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'y]W2BGD'
        list_0 = [str_0]
        message_0 = module_0.Message(text=str_0, code=str_0, index=list_0)
        list_1 = [message_0, message_0, message_0]
        validation_error_0 = module_0.ValidationError(messages=list_1)
        str_1 = 'drK_mrMO'
        base_error_0 = module_0.BaseError(text=str_1)
        bool_0 = base_error_0.__eq__(validation_error_0)
        str_2 = ':[{\tz-'
        int_0 = -291
        int_1 = -1655
        position_0 = module_0.Position(int_0, int_0, int_1)
        message_1 = module_0.Message(text=str_2, position=position_0)
        int_2 = -1726
        int_3 = 265
        position_1 = module_0.Position(int_2, int_2, int_3)
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()
        base_error_1 = module_0.BaseError(key=int_2, position=position_1, messages=iterator_0)
    except BaseException:
        pass