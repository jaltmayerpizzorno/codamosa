# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    int_0 = 502
    position_0 = module_0.Position(int_0, int_0, int_0)

def test_case_1():
    str_0 = 'no_match'
    int_0 = 0
    int_1 = 1205
    position_0 = module_0.Position(int_0, int_0, int_1)
    message_0 = module_0.Message(text=str_0, code=str_0, position=position_0)
    str_1 = message_0.__repr__()
    bool_0 = message_0.__eq__(int_0)

def test_case_2():
    str_0 = 'K!q}J.T%aA_LVxd\rxq9'
    message_0 = module_0.Message(text=str_0, key=str_0)
    int_0 = message_0.__hash__()

def test_case_3():
    float_0 = -2640.0
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    base_error_0 = module_0.BaseError(text=dict_0, position=dict_0)
    int_0 = base_error_0.__hash__()

def test_case_4():
    str_0 = 'yis~\x0bFDNPs6\\'
    message_0 = module_0.Message(text=str_0)
    bool_0 = message_0.__eq__(message_0)

def test_case_5():
    str_0 = 'userrkname'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(message_0)

def test_case_6():
    str_0 = 'hello'
    str_1 = 'max_length'
    str_2 = 'username'
    base_error_0 = module_0.BaseError(text=str_0, code=str_1, key=str_2)
    str_3 = [str_0]
    message_0 = module_0.Message(text=str_0, index=str_3)
    message_1 = [message_0, message_0]
    base_error_1 = module_0.BaseError(messages=message_1)
    var_0 = repr(base_error_1)

def test_case_7():
    str_0 = None
    int_0 = 1
    int_1 = None
    message_0 = module_0.Message(text=str_0, code=str_0, key=int_0)
    bool_0 = message_0.__eq__(int_1)
    list_0 = [message_0]
    validation_error_0 = module_0.ValidationError(text=str_0, key=int_1, messages=list_0)
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()

def test_case_8():
    str_0 = 'hello'
    str_1 = 'max_length'
    str_2 = 'username'
    base_error_0 = module_0.BaseError(text=str_0, code=str_1, key=str_2)
    var_0 = repr(base_error_0)
    str_3 = [str_0]
    message_0 = module_0.Message(text=str_0, index=str_3)
    list_0 = base_error_0.messages()
    str_4 = 'goodbye'
    message_1 = module_0.Message(text=str_4)
    message_2 = [message_0, message_1]
    base_error_1 = module_0.BaseError(messages=message_2)
    var_1 = repr(base_error_1)

def test_case_9():
    str_0 = 'ura"T-iTEe'
    base_error_0 = module_0.BaseError(text=str_0)
    int_0 = base_error_0.__hash__()
    str_1 = 'no7_m\t&ch'
    int_1 = 0
    int_2 = 1205
    position_0 = module_0.Position(int_1, int_1, int_2)
    message_0 = module_0.Message(text=str_1, code=str_1, position=position_0)
    str_2 = message_0.__repr__()
    bool_0 = base_error_0.__eq__(int_1)
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()
    int_3 = base_error_0.__hash__()

def test_case_10():
    str_0 = 'ura"T-iTEe'
    base_error_0 = module_0.BaseError(text=str_0)
    int_0 = base_error_0.__hash__()
    str_1 = 'no7_m\t&ch'
    int_1 = 0
    str_2 = base_error_0.__repr__()
    int_2 = 1205
    position_0 = module_0.Position(int_1, int_1, int_2)
    message_0 = module_0.Message(text=str_1, code=str_1, position=position_0)
    str_3 = message_0.__repr__()
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()
    int_3 = base_error_0.__hash__()

def test_case_11():
    float_0 = -1263.0
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    base_error_0 = module_0.BaseError(text=dict_0, position=dict_0)
    int_0 = 4
    int_1 = 1
    int_2 = None
    position_0 = module_0.Position(int_1, int_0, int_2)
    validation_result_0 = module_0.ValidationResult()
    str_0 = base_error_0.__str__()
    validation_result_1 = module_0.ValidationResult()
    iterator_0 = validation_result_1.__iter__()
    validation_result_2 = module_0.ValidationResult()
    str_1 = validation_result_2.__repr__()

def test_case_12():
    validation_result_0 = module_0.ValidationResult()
    bool_0 = validation_result_0.__bool__()

def test_case_13():
    str_0 = 'ura"T-iTEe'
    base_error_0 = module_0.BaseError(text=str_0)
    int_0 = base_error_0.__hash__()
    validation_error_0 = module_0.ValidationError(text=str_0, key=str_0)
    validation_result_0 = module_0.ValidationResult(error=validation_error_0)
    str_1 = validation_result_0.__repr__()

def test_case_14():
    str_0 = 'hello'
    base_error_0 = module_0.BaseError(text=str_0, code=str_0, key=str_0)
    var_0 = repr(base_error_0)
    str_1 = [str_0]
    message_0 = module_0.Message(text=str_0, index=str_1)
    str_2 = 'goodbye'
    message_1 = module_0.Message(text=str_2)
    message_2 = [message_0, message_1]
    base_error_1 = module_0.BaseError(messages=message_2)
    var_1 = repr(base_error_1)

def test_case_15():
    int_0 = -9
    validation_result_0 = module_0.ValidationResult(value=int_0)
    var_0 = tuple(validation_result_0)

def test_case_16():
    int_0 = 0
    position_0 = module_0.Position(int_0, int_0, int_0)
    str_0 = " >@'88\ngk $j"
    message_0 = module_0.Message(text=str_0, key=str_0, position=position_0)
    str_1 = message_0.__repr__()
    str_2 = position_0.__repr__()

def test_case_17():
    str_0 = 'ura"T-iTEe'
    base_error_0 = module_0.BaseError(text=str_0)
    int_0 = base_error_0.__hash__()
    int_1 = 0
    int_2 = 1205
    position_0 = module_0.Position(int_1, int_0, int_2)
    message_0 = module_0.Message(text=str_0, start_position=position_0)
    str_1 = message_0.__repr__()
    bool_0 = message_0.__eq__(int_0)
    validation_result_0 = module_0.ValidationResult()

def test_case_18():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    position_0 = module_0.Position(int_0, int_1, int_2)
    position_1 = module_0.Position(int_0, int_1, int_2)
    bool_0 = position_0.__eq__(position_1)
    int_3 = 0
    position_2 = module_0.Position(int_3, int_1, int_2)
    bool_1 = position_0.__eq__(position_2)
    position_3 = module_0.Position(int_0, int_3, int_2)
    bool_2 = position_0.__eq__(position_3)
    position_4 = module_0.Position(int_0, int_1, int_3)
    bool_3 = position_0.__eq__(position_4)

def test_case_19():
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
    validation_error_1 = module_0.ValidationError(messages=list_0)
    bool_2 = base_error_0.__eq__(validation_error_1)
    validation_result_1 = module_0.ValidationResult()
    str_1 = validation_result_0.__repr__()

def test_case_20():
    int_0 = 1
    int_1 = 2
    position_0 = module_0.Position(int_0, int_1, int_1)
    position_1 = module_0.Position(int_0, int_1, int_1)
    bool_0 = position_0.__eq__(position_1)
    int_2 = 0
    position_2 = module_0.Position(int_2, int_1, int_0)
    position_3 = module_0.Position(int_0, int_2, int_2)
    bool_1 = position_0.__eq__(position_3)
    position_4 = module_0.Position(int_0, int_1, int_2)
    bool_2 = position_0.__eq__(position_4)

def test_case_21():
    str_0 = 'B\x0b'
    int_0 = 5958
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
    bool_1 = position_0.__eq__(list_0)
    int_4 = None
    bool_2 = message_0.__eq__(message_0)
    list_1 = [int_4]
    bool_3 = position_1.__eq__(bool_0)
    int_5 = -385
    bool_4 = position_1.__eq__(list_0)
    int_6 = 0
    str_4 = ''
    message_1 = module_0.Message(text=str_4)
    int_7 = 2291
    list_2 = base_error_0.messages()
    position_2 = module_0.Position(int_5, int_6, int_7)
    message_2 = module_0.Message(text=str_3, index=list_1, position=position_2)
    message_3 = module_0.Message(text=str_3, code=str_0)
    bool_5 = message_3.__eq__(message_2)
    int_8 = base_error_0.__len__()
    bool_6 = base_error_0.__eq__(message_0)
    validation_error_0 = module_0.ValidationError(text=str_0, position=position_1)
    validation_result_0 = module_0.ValidationResult()
    str_5 = validation_result_0.__repr__()

def test_case_22():
    str_0 = 'May not have more than 100 characters'
    str_1 = 'max_length'
    var_0 = []
    int_0 = 1
    position_0 = module_0.Position(int_0, int_0, int_0)
    int_1 = 2
    position_1 = module_0.Position(int_0, int_0, int_1)
    message_0 = module_0.Message(text=str_0, code=str_1, index=var_0, start_position=position_0, end_position=position_1)
    var_1 = []
    position_2 = module_0.Position(int_1, int_1, int_0)
    position_3 = module_0.Position(int_1, int_1, int_1)
    message_1 = module_0.Message(text=str_0, code=str_1, index=var_1, start_position=position_2, end_position=position_3)
    var_2 = message_0 == message_1