# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    int_0 = 116
    position_0 = module_0.Position(int_0, int_0, int_0)
    bool_0 = position_0.__eq__(position_0)

def test_case_1():
    int_0 = -347
    int_1 = 3
    position_0 = module_0.Position(int_0, int_1, int_1)
    str_0 = position_0.__repr__()

def test_case_2():
    str_0 = 'YO*'
    list_0 = [str_0, str_0, str_0, str_0]
    message_0 = module_0.Message(text=str_0, code=str_0, index=list_0, start_position=str_0)
    message_1 = module_0.Message(text=str_0, code=str_0, position=message_0)
    str_1 = message_1.__repr__()

def test_case_3():
    int_0 = 3
    int_1 = -40
    str_0 = 'Must be null.'
    int_2 = -2693
    position_0 = module_0.Position(int_0, int_2, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0)
    int_3 = message_0.__hash__()
    int_4 = 968
    position_1 = module_0.Position(int_0, int_1, int_4)
    int_5 = 6
    int_6 = -3275
    bool_0 = position_1.__eq__(position_0)
    position_2 = module_0.Position(int_5, int_5, int_6)
    bool_1 = position_2.__eq__(position_1)

def test_case_4():
    str_0 = 'DW{.rI}\t'
    int_0 = -1275
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
    str_1 = message_0.__repr__()

def test_case_5():
    str_0 = '3\x0cP*\x0b=_e\\ml'
    int_0 = 6
    int_1 = None
    position_0 = module_0.Position(int_0, int_1, int_0)
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    float_0 = -3822.6582
    int_2 = 143
    int_3 = 1567
    int_4 = -2430
    position_1 = module_0.Position(int_2, int_3, int_4)
    bool_0 = position_1.__eq__(float_0)
    str_1 = message_0.__repr__()

def test_case_6():
    str_0 = 'An error occurred'
    str_1 = 'error_code'
    base_error_0 = module_0.BaseError(text=str_0, code=str_1)
    var_0 = str(base_error_0)
    str_2 = 'First error'
    str_3 = 'first_code'
    str_4 = 'first_key'
    message_0 = module_0.Message(text=str_2, code=str_3, key=str_4)
    str_5 = 'Second error'
    str_6 = 'second_code'
    str_7 = 'second_key'
    message_1 = module_0.Message(text=str_5, code=str_6, key=str_7)
    message_2 = [message_0, message_1]
    base_error_1 = module_0.BaseError(messages=message_2)
    var_1 = str(base_error_1)
    str_8 = 'Nested error'
    str_9 = 'nested_code'
    str_10 = 'parent'
    str_11 = 'child'
    str_12 = [str_10, str_11]
    message_3 = module_0.Message(text=str_8, code=str_9, index=str_12)
    message_4 = [message_3]
    base_error_2 = module_0.BaseError(messages=message_4)
    var_2 = str(base_error_2)

def test_case_7():
    validation_result_0 = module_0.ValidationResult()

def test_case_8():
    str_0 = ' is required.'
    int_0 = -216
    position_0 = module_0.Position(int_0, int_0, int_0)
    str_1 = position_0.__repr__()
    message_0 = module_0.Message(text=str_0, start_position=position_0)
    validation_result_0 = module_0.ValidationResult()
    int_1 = 1846
    str_2 = position_0.__repr__()
    position_1 = module_0.Position(int_0, int_1, int_0)
    bool_0 = validation_result_0.__bool__()
    int_2 = message_0.__hash__()
    bool_1 = position_1.__eq__(str_0)
    str_3 = position_0.__repr__()
    str_4 = position_0.__repr__()
    str_5 = validation_result_0.__repr__()

def test_case_9():
    int_0 = 3
    int_1 = -8
    int_2 = 968
    position_0 = module_0.Position(int_0, int_1, int_2)
    int_3 = 6
    int_4 = -3275
    position_1 = module_0.Position(int_3, int_3, int_4)
    bool_0 = position_1.__eq__(position_0)

def test_case_10():
    float_0 = -2711.0
    int_0 = -3269
    dict_0 = {float_0: int_0}
    base_error_0 = module_0.BaseError(text=dict_0)
    bool_0 = base_error_0.__eq__(float_0)
    position_0 = module_0.Position(int_0, int_0, int_0)
    bool_1 = position_0.__eq__(float_0)

def test_case_11():
    str_0 = '6ZQsOPUk;]q;16bm8<Q'
    optional_0 = None
    message_0 = module_0.Message(text=str_0, end_position=optional_0)
    bool_0 = message_0.__eq__(str_0)

def test_case_12():
    str_0 = ''
    int_0 = -2197
    int_1 = -803
    int_2 = 1891
    position_0 = module_0.Position(int_0, int_1, int_2)
    message_0 = module_0.Message(text=str_0, key=str_0, start_position=position_0, end_position=position_0)
    list_0 = [message_0, message_0]
    parse_error_0 = module_0.ParseError(messages=list_0)

def test_case_13():
    tuple_0 = None
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    str_0 = None
    list_0 = []
    message_0 = module_0.Message(text=str_0, index=list_0)
    list_1 = [message_0, message_0, message_0]
    validation_error_0 = module_0.ValidationError(text=str_0, code=str_0, messages=list_1)
    tuple_1 = (dict_0, validation_error_0)
    validation_result_0 = module_0.ValidationResult(value=tuple_1)
    iterator_0 = validation_result_0.__iter__()
    int_0 = 1
    position_0 = module_0.Position(int_0, int_0, int_0)

def test_case_14():
    int_0 = 1938
    str_0 = 'o\\9er\\dS<,js*5b\r(0g9'
    str_1 = ' rfaccC\tJeO\\?8\ty'
    message_0 = module_0.Message(text=str_1, key=int_0)
    int_1 = 3002
    position_0 = module_0.Position(int_0, int_0, int_1)
    bool_0 = position_0.__eq__(int_0)
    validation_error_0 = module_0.ValidationError(text=str_0, key=str_1, position=position_0)
    bool_1 = position_0.__eq__(position_0)
    validation_error_1 = module_0.ValidationError(text=str_1)
    str_2 = None
    message_1 = module_0.Message(text=str_2, code=str_2)
    bool_2 = message_1.__eq__(message_1)
    str_3 = message_0.__repr__()
    str_4 = message_0.__repr__()
    parse_error_0 = module_0.ParseError(text=str_3)
    bool_3 = message_1.__eq__(parse_error_0)
    list_0 = validation_error_0.messages(add_prefix=int_1)

def test_case_15():
    str_0 = '=V=T{'
    str_1 = 'o\\9er\\dS<,js*5b\r(0g9'
    str_2 = ' rfaccC\tJeO\\?8\ty'
    int_0 = 3002
    position_0 = module_0.Position(int_0, int_0, int_0)
    bool_0 = position_0.__eq__(int_0)
    validation_error_0 = module_0.ValidationError(text=str_1, key=str_0, position=position_0)
    validation_result_0 = module_0.ValidationResult(error=validation_error_0)
    validation_error_1 = module_0.ValidationError(text=str_2)
    str_3 = None
    list_0 = [int_0, str_0, str_3]
    message_0 = module_0.Message(text=str_1, code=str_1, index=list_0)
    message_1 = module_0.Message(text=str_0, code=str_0)
    bool_1 = message_1.__eq__(message_0)
    list_1 = validation_error_0.messages()
    str_4 = message_0.__repr__()
    bool_2 = message_0.__eq__(validation_error_1)
    str_5 = message_0.__repr__()
    bool_3 = position_0.__eq__(position_0)
    parse_error_0 = module_0.ParseError(text=str_4)
    bool_4 = message_0.__eq__(parse_error_0)
    validation_error_2 = module_0.ValidationError(text=str_0)

def test_case_16():
    int_0 = 1938
    str_0 = 'o\\9er\\dS<,js*5b\r(0g9'
    str_1 = ' rfaccC\tJeO\\?8\ty'
    message_0 = module_0.Message(text=str_1, key=int_0)
    list_0 = [message_0, message_0]
    validation_error_0 = module_0.ValidationError(messages=list_0)
    str_2 = message_0.__repr__()
    int_1 = 3002
    position_0 = module_0.Position(int_0, int_0, int_1)
    bool_0 = position_0.__eq__(int_0)
    validation_error_1 = module_0.ValidationError(text=str_0, key=str_1, position=position_0)
    validation_result_0 = module_0.ValidationResult(error=validation_error_1)
    list_1 = [int_0, str_0, str_2]
    message_1 = module_0.Message(text=str_0, code=str_0, index=list_1)
    message_2 = module_0.Message(text=str_2, code=str_2)
    bool_1 = message_2.__eq__(message_1)
    str_3 = message_1.__repr__()
    bool_2 = position_0.__eq__(position_0)
    parse_error_0 = module_0.ParseError(text=str_3)
    bool_3 = message_1.__eq__(parse_error_0)
    validation_error_2 = module_0.ValidationError(text=str_2)