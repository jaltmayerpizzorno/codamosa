# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    try:
        int_0 = 4677
        base_error_0 = module_0.BaseError(key=int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 502
        int_1 = -3320
        position_0 = module_0.Position(int_0, int_1, int_0)
        bool_0 = position_0.__eq__(position_0)
        base_error_0 = module_0.BaseError(position=position_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        str_1 = 'Must be a real date.'
        list_0 = [str_0, str_1, str_1, str_0]
        message_0 = module_0.Message(text=str_1, index=list_0)
        list_1 = [message_0, message_0, message_0]
        message_1 = module_0.Message(text=str_0, position=list_1)
        list_2 = [message_1, message_0]
        base_error_0 = module_0.BaseError(messages=list_2)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        int_1 = -4226
        int_2 = -1018
        position_0 = module_0.Position(int_1, int_1, int_2)
        bool_0 = position_0.__eq__(int_0)
        validation_result_0 = module_0.ValidationResult()
        list_0 = []
        base_error_0 = module_0.BaseError(text=validation_result_0, messages=list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -1263.0
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        base_error_0 = module_0.BaseError(text=dict_0, position=dict_0)
        str_0 = None
        int_0 = 4
        int_1 = 1
        int_2 = None
        position_0 = module_0.Position(int_1, int_0, int_2)
        message_0 = module_0.Message(text=str_0, code=str_0, key=int_1)
        bool_0 = message_0.__eq__(int_2)
        bool_1 = position_0.__eq__(str_0)
        list_0 = [message_0]
        validation_error_0 = module_0.ValidationError(text=str_0, key=int_2, messages=list_0)
        validation_result_0 = module_0.ValidationResult(error=validation_error_0)
        iterator_0 = validation_result_0.__iter__()
        validation_error_1 = module_0.ValidationError(messages=list_0)
        base_error_1 = module_0.BaseError(key=int_2, messages=list_0)
        list_1 = base_error_1.messages(add_prefix=int_0)
        str_1 = base_error_1.__str__()
        validation_error_2 = module_0.ValidationError(key=int_1, position=position_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -2640.0
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        base_error_0 = module_0.BaseError(text=dict_0, position=dict_0)
        str_0 = None
        int_0 = 4
        int_1 = 1
        int_2 = None
        position_0 = module_0.Position(int_1, int_0, int_2)
        message_0 = module_0.Message(text=str_0, code=str_0, key=int_1)
        bool_0 = message_0.__eq__(int_2)
        bool_1 = position_0.__eq__(str_0)
        list_0 = [message_0]
        validation_error_0 = module_0.ValidationError(text=str_0, key=int_2, messages=list_0)
        validation_result_0 = module_0.ValidationResult(error=validation_error_0)
        iterator_0 = validation_result_0.__iter__()
        int_3 = base_error_0.__len__()
        parse_error_0 = module_0.ParseError(code=str_0, position=position_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'allow_null'
        list_0 = [str_0, str_0, str_0, str_0]
        str_1 = 'Must be a real date.'
        message_0 = module_0.Message(text=str_1, index=list_0)
        validation_result_0 = module_0.ValidationResult()
        str_2 = validation_result_0.__repr__()
        str_3 = 'MO.'
        int_0 = 2163
        position_0 = module_0.Position(int_0, int_0, int_0)
        bool_0 = position_0.__eq__(validation_result_0)
        base_error_0 = module_0.BaseError(key=str_0, messages=str_3)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 6125
        int_1 = -826
        int_2 = 2010
        int_3 = 949
        position_0 = module_0.Position(int_1, int_2, int_3)
        bool_0 = position_0.__eq__(int_0)
        base_error_0 = module_0.BaseError()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\n    Parse and validate a YAML string, returning positionally marked error\n    messages on parse or validation failures.\n\n    content - A YAML string or bytestring.\n    validator - A Field instance or Schema class to validate against.\n\n    Returns a two-tuple of (value, error_messages)\n    '
        validation_error_0 = module_0.ValidationError(text=str_0, code=str_0)
        int_0 = 2929
        int_1 = 3266
        int_2 = 2
        position_0 = module_0.Position(int_0, int_1, int_2)
        list_0 = [str_0, str_0, int_0]
        validation_result_0 = module_0.ValidationResult()
        int_3 = -30
        int_4 = -275
        position_1 = module_0.Position(int_3, int_4, int_4)
        message_0 = module_0.Message(text=str_0, index=list_0, position=validation_result_0, end_position=position_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'Y>>;YLs~8'
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = 6
        int_1 = -707
        position_0 = module_0.Position(int_0, int_0, int_1)
        message_0 = module_0.Message(text=str_0, key=str_0, index=list_0, position=position_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '<PoJ9 1.NC#T[cwy\n*'
        list_0 = []
        int_0 = 4100
        list_1 = [int_0]
        int_1 = -385
        int_2 = 2291
        position_0 = module_0.Position(int_1, int_0, int_2)
        message_0 = module_0.Message(text=str_0, index=list_1, position=position_0)
        bool_0 = message_0.__eq__(int_2)
        int_3 = message_0.__hash__()
        str_1 = 'Must be less than or equal to {maximum}.'
        tuple_0 = (list_0, int_3, str_1, list_0)
        base_error_0 = module_0.BaseError(text=str_1, key=str_0)
        list_2 = base_error_0.messages()
        str_2 = base_error_0.__str__()
        validation_error_0 = module_0.ValidationError(code=str_0, messages=tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = True
        int_0 = 1694
        position_0 = module_0.Position(int_0, int_0, int_0)
        bool_1 = position_0.__eq__(bool_0)
        message_0 = None
        list_0 = [message_0, message_0, message_0, message_0]
        base_error_0 = module_0.BaseError(position=position_0, messages=list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = -1263.0
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        base_error_0 = module_0.BaseError(text=dict_0, position=dict_0)
        str_0 = None
        int_0 = 4
        int_1 = 1
        int_2 = None
        position_0 = module_0.Position(int_1, int_0, int_2)
        message_0 = module_0.Message(text=str_0, code=str_0, key=int_1)
        bool_0 = message_0.__eq__(int_2)
        bool_1 = position_0.__eq__(str_0)
        list_0 = [message_0]
        validation_error_0 = module_0.ValidationError(text=str_0, key=int_2, messages=list_0)
        validation_result_0 = module_0.ValidationResult(error=validation_error_0)
        str_1 = base_error_0.__str__()
        iterator_0 = validation_result_0.__iter__()
        validation_error_1 = module_0.ValidationError(messages=list_0)
        validation_result_1 = module_0.ValidationResult(value=str_1, error=validation_error_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'ura"T-iTEe'
        base_error_0 = module_0.BaseError(text=str_0)
        int_0 = base_error_0.__hash__()
        str_1 = 'no_match'
        int_1 = 0
        int_2 = 1205
        position_0 = module_0.Position(int_1, int_1, int_2)
        message_0 = module_0.Message(text=str_1, code=str_1, position=position_0)
        str_2 = message_0.__repr__()
        int_3 = message_0.__hash__()
        str_3 = '6V8fnN[t'
        int_4 = 1529
        message_1 = module_0.Message(text=str_3, key=int_4, position=position_0, start_position=position_0, end_position=position_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        base_error_0 = module_0.BaseError(messages=list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'B\x0b'
        int_0 = -13
        int_1 = 2008
        position_0 = module_0.Position(int_0, int_0, int_1)
        message_0 = module_0.Message(text=str_0, end_position=position_0)
        str_1 = message_0.__repr__()
        parse_error_0 = None
        base_error_0 = module_0.BaseError(text=str_1, position=parse_error_0)
        str_2 = base_error_0.__str__()
        int_2 = base_error_0.__hash__()
        str_3 = base_error_0.__repr__()
        list_0 = []
        int_3 = 4100
        position_1 = module_0.Position(int_2, int_2, int_3)
        bool_0 = position_1.__eq__(list_0)
        int_4 = None
        bool_1 = message_0.__eq__(message_0)
        list_1 = [int_4]
        bool_2 = position_1.__eq__(bool_0)
        int_5 = -385
        bool_3 = position_1.__eq__(list_0)
        int_6 = 0
        int_7 = 2291
        list_2 = base_error_0.messages()
        position_2 = module_0.Position(int_5, int_6, int_7)
        message_1 = module_0.Message(text=str_3, index=list_1, position=position_2)
        int_8 = -2502
        int_9 = 1
        position_3 = module_0.Position(int_8, int_5, int_9)
        message_2 = module_0.Message(text=str_0, index=list_1, start_position=position_3)
        bool_4 = message_2.__eq__(message_0)
        int_10 = base_error_0.__len__()
        bool_5 = base_error_0.__eq__(int_8)
        validation_error_0 = module_0.ValidationError(key=int_5, position=position_3, messages=list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 211
        int_1 = 2399
        int_2 = -387
        position_0 = module_0.Position(int_1, int_0, int_2)
        bool_0 = position_0.__eq__(int_0)
        str_0 = '&(..)YwFwv6IvlD'
        position_1 = None
        set_0 = {bool_0}
        bool_1 = position_0.__eq__(set_0)
        message_0 = module_0.Message(text=str_0, key=int_0, position=position_1, start_position=position_1)
        list_0 = [message_0, message_0]
        base_error_0 = module_0.BaseError(messages=list_0)
        str_1 = base_error_0.__str__()
        position_2 = module_0.Position(int_0, int_0, int_0)
        base_error_1 = module_0.BaseError()
    except BaseException:
        pass