# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    try:
        str_0 = '\x0bS.K#y:,S6#'
        list_0 = [str_0, str_0, str_0]
        str_1 = 'kPNgn>UaC>7!ZT:u'
        int_0 = 1627
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_1, start_position=position_0, end_position=position_0)
        bool_0 = message_0.__eq__(list_0)
        base_error_0 = module_0.BaseError()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 6
        base_error_0 = module_0.BaseError(text=int_0)
        validation_result_0 = module_0.ValidationResult(value=base_error_0)
        int_1 = 2
        int_2 = -188
        position_0 = module_0.Position(int_0, int_1, int_2)
        str_0 = validation_result_0.__repr__()
        int_3 = 1910
        int_4 = 6
        position_1 = module_0.Position(int_3, int_3, int_4)
        message_0 = module_0.Message(text=str_0, code=str_0)
        str_1 = message_0.__repr__()
        str_2 = position_1.__repr__()
        str_3 = position_1.__repr__()
        base_error_1 = module_0.BaseError(text=str_3, position=position_1, messages=str_3)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1321.0
        set_0 = {float_0, float_0, float_0}
        validation_result_0 = module_0.ValidationResult(value=set_0)
        str_0 = '3NT F'
        validation_error_0 = module_0.ValidationError(messages=str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 6
        base_error_0 = module_0.BaseError(text=int_0)
        validation_result_0 = module_0.ValidationResult(value=base_error_0)
        int_1 = 2
        int_2 = -188
        position_0 = module_0.Position(int_0, int_1, int_2)
        str_0 = base_error_0.__str__()
        str_1 = validation_result_0.__repr__()
        int_3 = 1910
        int_4 = 6
        position_1 = module_0.Position(int_3, int_3, int_4)
        message_0 = module_0.Message(text=str_1, code=str_1)
        str_2 = validation_result_0.__repr__()
        str_3 = message_0.__repr__()
        str_4 = position_1.__repr__()
        str_5 = position_1.__repr__()
        base_error_1 = module_0.BaseError(text=str_5, position=position_1, messages=str_5)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ' 8CH<X\rwY'
        list_0 = [str_0]
        int_0 = -1768
        int_1 = -1934
        position_0 = module_0.Position(int_0, int_1, int_0)
        message_0 = module_0.Message(text=str_0, index=list_0, position=position_0, start_position=position_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'number'
        validation_result_0 = module_0.ValidationResult(value=str_0)
        str_1 = '\n    Parse and validate a JSON string, returning positionally marked error\n    messages on parse or validation failures.\n\n    content - A JSON string or bytestring.\n    validator - A Field instance or Schema class to validate against.\n\n    Returns a two-tuple of (value, error_messages)\n    '
        int_0 = 2641
        int_1 = 2261
        position_0 = module_0.Position(int_0, int_1, int_1)
        message_0 = module_0.Message(text=str_1, key=str_0, position=position_0, end_position=position_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'minLength'
        str_1 = '1Zl3[b,'
        validation_error_0 = module_0.ValidationError(text=str_0, code=str_1)
        int_0 = 2244
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_1, key=str_1, index=validation_error_0, position=position_0, start_position=position_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = "j\x0btD,6c3M'("
        set_0 = set()
        int_0 = 997
        int_1 = -2466
        int_2 = None
        position_0 = module_0.Position(int_0, int_1, int_2)
        message_0 = module_0.Message(text=str_0, end_position=position_0)
        list_0 = [message_0, message_0, message_0]
        base_error_0 = module_0.BaseError(key=str_0, position=set_0, messages=list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        base_error_0 = module_0.BaseError()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\x0bS.GK#y:,S6#'
        int_0 = 1627
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_0, start_position=position_0)
        int_1 = -2544
        position_1 = module_0.Position(int_0, int_1, int_1)
        bool_0 = message_0.__eq__(message_0)
        int_2 = 1
        int_3 = -4351
        int_4 = message_0.__hash__()
        int_5 = None
        position_2 = module_0.Position(int_2, int_3, int_5)
        list_0 = [message_0, message_0]
        base_error_0 = module_0.BaseError(position=position_0, messages=list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        validation_result_0 = module_0.ValidationResult()
        str_0 = validation_result_0.__repr__()
        str_1 = validation_result_0.__repr__()
        iterator_0 = validation_result_0.__iter__()
        int_0 = None
        int_1 = -1456
        int_2 = -2833
        position_0 = module_0.Position(int_0, int_1, int_2)
        list_0 = []
        validation_error_0 = module_0.ValidationError(messages=list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 1
        int_1 = 460
        optional_0 = None
        position_0 = None
        str_0 = 'hejGS!5_GZcktDwZs>nh'
        list_0 = [int_0, int_0, int_0, str_0]
        message_0 = module_0.Message(text=str_0, index=list_0, end_position=position_0)
        list_1 = [message_0, message_0]
        validation_error_0 = module_0.ValidationError(code=optional_0, position=position_0, messages=list_1)
        base_error_0 = module_0.BaseError(key=int_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'union'
        int_0 = -415
        int_1 = 466
        position_0 = module_0.Position(int_0, int_0, int_1)
        message_0 = module_0.Message(text=str_0)
        list_0 = [message_0, message_0, message_0]
        base_error_0 = module_0.BaseError(code=str_0, position=position_0, messages=list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\x0bS.GK#y:,S6#'
        list_0 = [str_0, str_0, str_0]
        int_0 = 1627
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
        bool_0 = message_0.__eq__(list_0)
        int_1 = -823
        message_1 = module_0.Message(text=str_0, key=str_0)
        bool_1 = message_0.__eq__(message_1)
        int_2 = -4351
        position_1 = module_0.Position(int_1, int_0, int_1)
        str_1 = '`kK7'
        message_2 = module_0.Message(text=str_1, code=str_1, end_position=position_0)
        list_1 = [message_1, message_2, message_2, message_1]
        base_error_0 = module_0.BaseError(text=str_0, key=int_2, messages=list_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '\x0bS.GK#y:,S6#'
        int_0 = 1627
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
        message_1 = module_0.Message(text=str_0, key=int_0, end_position=position_0)
        message_2 = module_0.Message(text=str_0, code=str_0)
        bool_0 = message_2.__eq__(message_0)
        int_1 = -823
        int_2 = -3259
        int_3 = 1008
        int_4 = -4206
        position_1 = module_0.Position(int_1, int_3, int_4)
        list_0 = None
        base_error_0 = module_0.BaseError(text=str_0, code=str_0, messages=list_0)
        str_1 = base_error_0.__str__()
        validation_result_0 = module_0.ValidationResult(error=list_0)
        iterator_0 = validation_result_0.__iter__()
        int_5 = -1737
        int_6 = None
        int_7 = -43
        position_2 = module_0.Position(int_6, int_2, int_7)
        bool_1 = position_1.__eq__(int_5)
        base_error_1 = module_0.BaseError(position=position_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '\x0bS.GK#y:,S6#'
        list_0 = [str_0, str_0, str_0]
        int_0 = 1627
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
        bool_0 = message_0.__eq__(list_0)
        int_1 = 1
        int_2 = 1
        position_1 = module_0.Position(int_0, int_0, int_2)
        int_3 = -3286
        base_error_0 = module_0.BaseError(text=str_0)
        str_1 = base_error_0.__str__()
        optional_0 = None
        validation_result_0 = module_0.ValidationResult(value=optional_0)
        validation_error_0 = module_0.ValidationError(text=str_1, code=str_1, key=int_1)
        validation_result_1 = module_0.ValidationResult(value=int_3, error=validation_error_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '\x0bS.GK#y:,S6#'
        list_0 = [str_0, str_0, str_0]
        int_0 = 5
        int_1 = 3
        position_0 = module_0.Position(int_0, int_0, int_1)
        message_0 = module_0.Message(text=str_0, code=str_0, key=str_0, end_position=position_0)
        bool_0 = message_0.__eq__(list_0)
        int_2 = -3259
        int_3 = -4351
        int_4 = -388
        position_1 = module_0.Position(int_0, int_2, int_4)
        list_1 = [message_0, message_0]
        base_error_0 = module_0.BaseError(messages=list_1)
        str_1 = base_error_0.__str__()
        str_2 = ''
        validation_result_0 = module_0.ValidationResult(error=str_2)
        iterator_0 = validation_result_0.__iter__()
        int_5 = 1
        position_2 = module_0.Position(int_1, int_3, int_0)
        bool_1 = position_2.__eq__(message_0)
        base_error_1 = module_0.BaseError(key=int_5, position=position_1, messages=list_1)
    except BaseException:
        pass