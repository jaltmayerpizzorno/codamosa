# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    validation_result_0 = module_0.ValidationResult()
    str_0 = validation_result_0.__repr__()

def test_case_1():
    str_0 = '0'
    int_0 = 1389
    int_1 = -2380
    position_0 = module_0.Position(int_0, int_0, int_1)
    parse_error_0 = module_0.ParseError(text=str_0, position=position_0)

def test_case_2():
    int_0 = 42
    position_0 = module_0.Position(int_0, int_0, int_0)
    position_1 = module_0.Position(int_0, int_0, int_0)
    bool_0 = position_0.__eq__(position_1)

def test_case_3():
    str_0 = 'L8'
    int_0 = -3327
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
    int_1 = message_0.__hash__()
    str_1 = message_0.__repr__()
    str_2 = '"doAm/}.dcI#S7'
    message_1 = module_0.Message(text=str_2, code=str_2, key=str_2)
    bool_0 = message_1.__eq__(str_2)
    str_3 = 'j2i@F'
    none_type_0 = None
    message_2 = module_0.Message(text=str_3, code=str_2, key=str_3, start_position=none_type_0)
    str_4 = message_2.__repr__()

def test_case_4():
    str_0 = 'username'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(message_0)

def test_case_5():
    str_0 = '9i&s'
    base_error_0 = module_0.BaseError(text=str_0, code=str_0)
    bool_0 = base_error_0.__eq__(str_0)

def test_case_6():
    str_0 = '"doAm/}.dcI#S7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=message_0)
    int_0 = base_error_0.__hash__()

def test_case_7():
    str_0 = ''
    message_0 = module_0.Message(text=str_0)
    str_1 = message_0.__repr__()

def test_case_8():
    str_0 = '\n    A set-like class that tests for uniqueness of primitive types.\n    Ensures the `True` and `False` are treated as distinct from `1` and `0`,\n    and coerces non-hashable instances that cannot be added to sets,\n    into hashable representations that can.\n    '
    str_1 = '_target_string'
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1, str_1: str_1}
    base_error_0 = module_0.BaseError(text=dict_0, key=str_1)
    list_0 = base_error_0.messages(add_prefix=str_0)

def test_case_9():
    str_0 = '"doAm/}.dcI#S7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=message_0)
    iterator_0 = base_error_0.__iter__()
    str_1 = '|j2k/F'
    none_type_0 = None
    message_1 = module_0.Message(text=str_1, code=str_0, key=str_1, start_position=none_type_0)
    str_2 = message_1.__repr__()

def test_case_10():
    str_0 = '"coAm/}.HcI#q7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=str_0)
    str_1 = base_error_0.__repr__()

def test_case_11():
    validation_result_0 = module_0.ValidationResult()
    bool_0 = validation_result_0.__bool__()

def test_case_12():
    str_0 = '9iqP'
    base_error_0 = module_0.BaseError(text=str_0, code=str_0)
    int_0 = -1998
    position_0 = module_0.Position(int_0, int_0, int_0)
    validation_error_0 = module_0.ValidationError(text=str_0, code=str_0, position=position_0)
    bool_0 = base_error_0.__eq__(validation_error_0)

def test_case_13():
    str_0 = 'useJornam'
    message_0 = module_0.Message(text=str_0)
    bool_0 = message_0.__eq__(message_0)

def test_case_14():
    str_0 = '"coAm/}.HcI#q7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=str_0)

def test_case_15():
    str_0 = ''
    base_error_0 = module_0.BaseError(text=str_0, key=str_0)
    bool_0 = base_error_0.__eq__(base_error_0)

def test_case_16():
    str_0 = '"doAm/}.dcI#S7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=message_0)
    bool_1 = base_error_0.__eq__(bool_0)
    int_0 = base_error_0.__len__()

def test_case_17():
    str_0 = '"doAm/}.dcI#S7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=message_0)
    list_0 = base_error_0.messages(add_prefix=str_0)
    int_0 = 1
    int_1 = -864
    str_1 = base_error_0.__repr__()
    int_2 = -4383
    position_0 = module_0.Position(int_1, int_2, int_2)
    str_2 = position_0.__repr__()
    validation_result_0 = module_0.ValidationResult()
    str_3 = validation_result_0.__repr__()
    bool_1 = position_0.__eq__(validation_result_0)
    base_error_1 = module_0.BaseError(messages=list_0)
    str_4 = base_error_1.__repr__()
    int_3 = base_error_0.__len__()
    str_5 = base_error_1.__repr__()
    int_4 = base_error_1.__len__()
    bool_2 = base_error_1.__eq__(int_0)
    str_6 = base_error_0.__str__()

def test_case_18():
    str_0 = '\rQZ'
    int_0 = 2
    int_1 = -14
    position_0 = module_0.Position(int_0, int_1, int_1)
    message_0 = module_0.Message(text=str_0, key=str_0, start_position=position_0)
    bool_0 = message_0.__eq__(str_0)
    int_2 = -255
    str_1 = position_0.__repr__()
    int_3 = 0
    position_1 = module_0.Position(int_2, int_2, int_3)
    str_2 = position_1.__repr__()
    message_1 = module_0.Message(text=str_0, key=str_0, end_position=position_1)
    list_0 = [message_1, message_1]
    base_error_0 = module_0.BaseError(messages=list_0)
    str_3 = base_error_0.__repr__()
    base_error_1 = module_0.BaseError(messages=list_0)
    validation_result_0 = module_0.ValidationResult(value=message_1)
    iterator_0 = validation_result_0.__iter__()
    int_4 = base_error_1.__len__()
    str_4 = base_error_1.__str__()
    list_1 = base_error_1.messages()

def test_case_19():
    str_0 = 'test'
    int_0 = 1
    int_1 = 2
    int_2 = 3
    position_0 = module_0.Position(int_0, int_1, int_2)
    int_3 = 4
    position_1 = module_0.Position(int_1, int_2, int_3)
    message_0 = module_0.Message(text=str_0, index=position_1, start_position=position_0, end_position=position_1)
    position_2 = module_0.Position(int_0, int_1, int_2)
    position_3 = module_0.Position(int_1, int_2, int_3)
    message_1 = module_0.Message(text=str_0, index=int_2, start_position=position_2, end_position=position_3)
    bool_0 = message_0.__eq__(message_1)
    position_4 = module_0.Position(int_0, int_1, int_2)
    int_4 = 5
    position_5 = module_0.Position(int_1, int_2, int_4)
    message_2 = module_0.Message(text=str_0, index=position_2, start_position=position_4, end_position=position_5)
    bool_1 = message_0.__eq__(message_2)
    position_6 = module_0.Position(int_1, int_3, int_3)
    message_3 = module_0.Message(text=str_0, index=bool_0, start_position=position_1, end_position=position_6)
    bool_2 = message_0.__eq__(message_3)

def test_case_20():
    str_0 = '"doAm/}.dcI#S7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=message_0)
    validation_result_0 = module_0.ValidationResult()
    list_0 = base_error_0.messages(add_prefix=str_0)
    int_0 = 1
    int_1 = -864
    str_1 = base_error_0.__repr__()
    int_2 = -4383
    position_0 = module_0.Position(int_1, int_2, int_2)
    str_2 = position_0.__repr__()
    validation_result_1 = module_0.ValidationResult()
    str_3 = validation_result_0.__repr__()
    bool_1 = position_0.__eq__(validation_result_0)
    parse_error_0 = module_0.ParseError(text=str_2)
    base_error_1 = module_0.BaseError(messages=list_0)
    str_4 = base_error_1.__repr__()
    int_3 = base_error_0.__len__()
    str_5 = base_error_1.__repr__()
    int_4 = base_error_1.__len__()
    bool_2 = base_error_1.__eq__(int_0)
    list_1 = base_error_0.messages()
    str_6 = "MY'P["
    message_1 = module_0.Message(text=str_6, code=str_0, start_position=position_0)
    str_7 = message_1.__repr__()

def test_case_21():
    str_0 = '"doAm/}.dcI#S7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    validation_result_0 = module_0.ValidationResult()
    int_0 = 1
    int_1 = 2852
    int_2 = -2490
    position_0 = module_0.Position(int_1, int_0, int_2)
    str_1 = position_0.__repr__()
    bool_1 = position_0.__eq__(str_0)
    list_0 = [message_0]
    parse_error_0 = module_0.ParseError(messages=list_0)
    str_2 = position_0.__repr__()
    base_error_0 = module_0.BaseError(messages=list_0)
    str_3 = base_error_0.__repr__()
    int_3 = base_error_0.__len__()
    int_4 = message_0.__hash__()

def test_case_22():
    str_0 = '"doAm/}.dcI#S7'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(str_0)
    base_error_0 = module_0.BaseError(text=message_0)
    list_0 = base_error_0.messages(add_prefix=str_0)
    int_0 = 1
    int_1 = -864
    str_1 = base_error_0.__repr__()
    int_2 = -4383
    position_0 = module_0.Position(int_1, int_2, int_2)
    str_2 = position_0.__repr__()
    validation_result_0 = module_0.ValidationResult()
    str_3 = validation_result_0.__repr__()
    bool_1 = position_0.__eq__(validation_result_0)
    parse_error_0 = module_0.ParseError(text=str_2)
    base_error_1 = module_0.BaseError(messages=list_0)
    str_4 = base_error_1.__repr__()
    int_3 = base_error_0.__len__()
    str_5 = base_error_1.__repr__()
    int_4 = base_error_1.__len__()
    bool_2 = base_error_1.__eq__(int_0)
    str_6 = base_error_1.__str__()
    message_1 = module_0.Message(text=str_5, code=str_1, end_position=position_0)
    str_7 = message_0.__repr__()

def test_case_23():
    int_0 = 1
    var_0 = None
    validation_result_0 = module_0.ValidationResult(value=int_0, error=var_0)
    var_1 = iter(validation_result_0)
    var_2 = next(var_1)

def test_case_24():
    int_0 = 3
    validation_result_0 = module_0.ValidationResult(value=int_0)
    var_0 = list(validation_result_0)
    str_0 = 'error'
    validation_error_0 = module_0.ValidationError(text=str_0)

def test_case_25():
    str_0 = 'username'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    str_1 = 'Jp,n0z_b\x0b[n#25\x0b,'
    message_1 = module_0.Message(text=str_1, code=str_1, key=str_0)
    bool_0 = message_1.__eq__(message_0)

def test_case_26():
    int_0 = 123
    str_0 = 'foo'
    str_1 = 'bar'
    var_0 = [int_0, str_0, str_1]
    str_2 = 'test'
    int_1 = 1
    int_2 = 2
    int_3 = 3
    position_0 = module_0.Position(int_1, int_2, int_3)
    int_4 = 4
    position_1 = module_0.Position(int_2, int_3, int_4)
    message_0 = module_0.Message(text=str_2, index=var_0, start_position=position_0, end_position=position_1)
    position_2 = module_0.Position(int_1, int_2, int_3)
    position_3 = module_0.Position(int_2, int_3, int_4)
    message_1 = module_0.Message(text=str_2, index=var_0, start_position=position_2, end_position=position_3)
    bool_0 = message_0.__eq__(message_1)
    position_4 = module_0.Position(int_1, int_2, int_3)
    int_5 = 5
    position_5 = module_0.Position(int_2, int_3, int_5)
    message_2 = module_0.Message(text=str_2, index=var_0, start_position=position_4, end_position=position_5)
    bool_1 = message_0.__eq__(message_2)
    position_6 = module_0.Position(int_1, int_2, int_3)
    position_7 = module_0.Position(int_2, int_4, int_4)
    message_3 = module_0.Message(text=str_2, index=var_0, start_position=position_6, end_position=position_7)
    bool_2 = message_0.__eq__(message_3)

def test_case_27():
    str_0 = 'username'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    int_0 = 2
    int_1 = -767
    position_0 = module_0.Position(int_0, int_0, int_1)
    message_1 = module_0.Message(text=str_0)
    bool_0 = message_0.__eq__(message_1)