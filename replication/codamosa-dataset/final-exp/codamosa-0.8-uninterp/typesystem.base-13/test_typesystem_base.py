# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    validation_result_0 = module_0.ValidationResult()

def test_case_1():
    str_0 = 'ax_length'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    bool_0 = message_0.__eq__(message_0)

def test_case_2():
    str_0 = 'h6mrL1(v'
    parse_error_0 = module_0.ParseError(text=str_0)
    message_0 = module_0.Message(text=str_0, key=str_0, position=parse_error_0)
    bool_0 = message_0.__eq__(message_0)

def test_case_3():
    str_0 = 'tag:yaml.org,2002:null'
    base_error_0 = module_0.BaseError(text=str_0, code=str_0)
    str_1 = base_error_0.__repr__()

def test_case_4():
    str_0 = 'ax_length'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    message_1 = module_0.Message(text=str_0, code=str_0, key=str_0)

def test_case_5():
    str_0 = 'foo'
    str_1 = 'custom'
    message_0 = module_0.Message(text=str_0, code=str_1)
    message_1 = [message_0]
    validation_error_0 = module_0.ValidationError(messages=message_1)
    var_0 = repr(validation_error_0)
    var_1 = str(validation_error_0)
    message_2 = module_0.Message(text=str_0, code=str_1, key=str_0)
    message_3 = [message_2]
    validation_error_1 = module_0.ValidationError(messages=message_3)
    var_2 = repr(validation_error_1)
    var_3 = str(validation_error_1)
    int_0 = 3
    var_4 = [str_0, int_0]
    message_4 = module_0.Message(text=str_0, code=str_1, index=var_4)
    message_5 = [message_4]
    validation_error_2 = module_0.ValidationError(messages=message_5)
    var_5 = repr(validation_error_2)

def test_case_6():
    str_0 = 'text'
    str_1 = 'code'
    str_2 = 'key'
    var_0 = None
    message_0 = module_0.Message(text=str_0, code=str_1, key=str_2, position=var_0)
    base_error_0 = module_0.BaseError(text=str_0, code=str_1, key=str_2, position=var_0)
    var_1 = repr(base_error_0)
    message_1 = [message_0, message_0]
    base_error_1 = module_0.BaseError(messages=message_1)
    var_2 = repr(base_error_1)

def test_case_7():
    validation_result_0 = module_0.ValidationResult()
    bool_0 = validation_result_0.__bool__()

def test_case_8():
    str_0 = 'field_id'
    bool_0 = True
    validation_result_0 = module_0.ValidationResult(value=bool_0)
    iterator_0 = validation_result_0.__iter__()
    bool_1 = validation_result_0.__bool__()
    base_error_0 = module_0.BaseError(text=str_0, key=str_0)
    str_1 = base_error_0.__str__()
    validation_error_0 = module_0.ValidationError(text=str_0)
    bool_2 = base_error_0.__eq__(base_error_0)
    validation_result_1 = module_0.ValidationResult()
    int_0 = base_error_0.__len__()
    int_1 = base_error_0.__hash__()
    iterator_1 = base_error_0.__iter__()
    int_2 = -5248
    int_3 = 1467
    str_2 = validation_result_0.__repr__()
    bool_3 = validation_result_0.__bool__()
    int_4 = None
    iterator_2 = validation_result_1.__iter__()
    position_0 = module_0.Position(int_3, int_0, int_4)
    str_3 = base_error_0.__repr__()
    validation_result_2 = module_0.ValidationResult(error=validation_error_0)
    position_1 = module_0.Position(int_2, int_2, int_3)

def test_case_9():
    str_0 = 'May not have more than 100 characters'
    str_1 = 'max_length'
    str_2 = 'username'
    message_0 = module_0.Message(text=str_0, code=str_1, key=str_2)
    message_1 = module_0.Message(text=str_0, code=str_1, key=str_2)
    dict_0 = {message_1: message_0, message_0: message_1, str_1: str_2, message_1: message_1}
    message_2 = module_0.Message(text=str_1, index=dict_0)
    none_type_0 = None
    message_3 = module_0.Message(text=str_2, index=none_type_0)

def test_case_10():
    str_0 = "/uO\n'~cm,RBIXa"
    str_1 = "F(v!\rn9S'"
    message_0 = module_0.Message(text=str_0, end_position=str_1)

def test_case_11():
    str_0 = ',t\nY8C>U.$ZLD '
    message_0 = module_0.Message(text=str_0)
    str_1 = message_0.__repr__()
    int_0 = message_0.__hash__()
    bool_0 = message_0.__eq__(str_1)
    base_error_0 = module_0.BaseError(text=str_1)
    int_1 = message_0.__hash__()
    str_2 = message_0.__repr__()
    validation_result_0 = module_0.ValidationResult()
    bool_1 = validation_result_0.__bool__()
    bool_2 = message_0.__eq__(base_error_0)
    str_3 = validation_result_0.__repr__()
    int_2 = None
    position_0 = module_0.Position(int_1, int_2, int_2)
    str_4 = base_error_0.__repr__()
    validation_result_1 = module_0.ValidationResult()
    base_error_1 = module_0.BaseError(text=str_3, position=position_0)
    int_3 = -557
    position_1 = module_0.Position(int_3, int_3, int_3)
    str_5 = position_1.__repr__()
    bool_3 = position_1.__eq__(str_2)

def test_case_12():
    str_0 = 'ax_length'
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0)
    validation_error_0 = module_0.ValidationError(text=str_0, key=str_0)
    bool_0 = message_0.__eq__(message_0)

def test_case_13():
    int_0 = 42
    validation_result_0 = module_0.ValidationResult(value=int_0)
    var_0 = list(validation_result_0)
    bool_0 = validation_result_0.__bool__()

def test_case_14():
    str_0 = 'P*xzkDs#ZYn\tyyv'
    int_0 = -1260
    base_error_0 = module_0.BaseError(text=str_0)
    iterator_0 = base_error_0.__iter__()
    position_0 = module_0.Position(int_0, int_0, int_0)
    bool_0 = position_0.__eq__(position_0)
    str_1 = "aPa@6\\IqI\\5Z'r?m*h<^"
    int_1 = base_error_0.__len__()
    int_2 = base_error_0.__hash__()
    iterator_1 = base_error_0.__iter__()
    message_0 = module_0.Message(text=str_1, start_position=position_0)
    list_0 = [message_0, message_0]
    validation_result_0 = module_0.ValidationResult(value=list_0)
    str_2 = validation_result_0.__repr__()
    validation_result_1 = module_0.ValidationResult()
    bool_1 = validation_result_0.__bool__()
    iterator_2 = validation_result_0.__iter__()
    int_3 = -644
    int_4 = -565
    position_1 = module_0.Position(int_3, int_4, int_0)
    str_3 = base_error_0.__repr__()
    str_4 = '8,<m k\tc4Q.aT'
    validation_error_0 = module_0.ValidationError(text=str_4, position=position_0)
    validation_result_2 = module_0.ValidationResult(error=validation_error_0)
    int_5 = 3181
    position_2 = module_0.Position(int_5, int_5, int_3)
    str_5 = position_2.__repr__()
    bool_2 = position_0.__eq__(iterator_0)

def test_case_15():
    str_0 = 'LewYVB'
    int_0 = 2858
    int_1 = 3215
    position_0 = module_0.Position(int_0, int_1, int_1)
    message_0 = module_0.Message(text=str_0, code=str_0, key=str_0, end_position=position_0)
    list_0 = [message_0, message_0]
    base_error_0 = module_0.BaseError(messages=list_0)
    str_1 = base_error_0.__str__()
    int_2 = 272
    validation_result_0 = module_0.ValidationResult(error=int_2)
    bool_0 = validation_result_0.__bool__()
    str_2 = base_error_0.__str__()
    message_1 = module_0.Message(text=str_0, key=str_0)
    str_3 = message_1.__repr__()
    str_4 = message_1.__repr__()
    int_3 = message_1.__hash__()
    int_4 = message_1.__hash__()
    bool_1 = message_1.__eq__(message_1)
    int_5 = message_1.__hash__()
    iterator_0 = validation_result_0.__iter__()
    int_6 = -1484
    position_1 = module_0.Position(int_5, int_4, int_6)
    int_7 = message_1.__hash__()
    str_5 = base_error_0.__str__()
    str_6 = validation_result_0.__repr__()

def test_case_16():
    str_0 = 'field_id'
    bool_0 = True
    validation_result_0 = module_0.ValidationResult(value=bool_0)
    iterator_0 = validation_result_0.__iter__()
    bool_1 = validation_result_0.__bool__()
    base_error_0 = module_0.BaseError(text=str_0, key=str_0)
    str_1 = base_error_0.__str__()
    validation_error_0 = module_0.ValidationError(text=str_0)
    float_0 = -1971.827
    message_0 = module_0.Message(text=str_0, code=str_1, index=float_0)
    bool_2 = base_error_0.__eq__(base_error_0)
    validation_result_1 = module_0.ValidationResult()
    bool_3 = validation_result_1.__bool__()
    int_0 = -16
    int_1 = 2709
    position_0 = module_0.Position(int_0, int_1, int_0)
    validation_result_2 = module_0.ValidationResult(error=validation_error_0)
    bool_4 = position_0.__eq__(validation_result_2)
    message_1 = module_0.Message(text=str_1, code=str_1, key=str_0)
    str_2 = validation_result_2.__repr__()
    int_2 = None
    int_3 = 1
    int_4 = -1629
    position_1 = module_0.Position(int_1, int_3, int_4)
    str_3 = base_error_0.__repr__()
    validation_result_3 = module_0.ValidationResult()
    base_error_1 = module_0.BaseError(text=str_1)
    position_2 = module_0.Position(int_0, int_2, int_0)
    str_4 = position_2.__repr__()
    bool_5 = position_0.__eq__(position_2)

def test_case_17():
    str_0 = 'field_id'
    bool_0 = True
    validation_result_0 = module_0.ValidationResult(value=bool_0)
    iterator_0 = validation_result_0.__iter__()
    bool_1 = validation_result_0.__bool__()
    base_error_0 = module_0.BaseError(text=str_0, key=str_0)
    str_1 = base_error_0.__str__()
    validation_error_0 = module_0.ValidationError(text=str_0)
    bool_2 = base_error_0.__eq__(base_error_0)
    validation_result_1 = module_0.ValidationResult()
    int_0 = base_error_0.__len__()
    int_1 = base_error_0.__hash__()
    iterator_1 = base_error_0.__iter__()
    int_2 = -5248
    int_3 = 1467
    int_4 = 446
    str_2 = validation_result_0.__repr__()
    validation_result_2 = module_0.ValidationResult()
    bool_3 = validation_result_2.__bool__()
    int_5 = None
    iterator_2 = validation_result_2.__iter__()
    position_0 = module_0.Position(int_3, int_4, int_5)
    str_3 = base_error_0.__repr__()
    validation_result_3 = module_0.ValidationResult(error=validation_error_0)
    validation_result_4 = module_0.ValidationResult()
    int_6 = None
    int_7 = -2398
    position_1 = module_0.Position(int_6, int_7, int_2)
    str_4 = position_1.__repr__()
    bool_4 = position_1.__eq__(position_0)

def test_case_18():
    str_0 = 'abc'
    message_0 = module_0.Message(text=str_0, code=str_0)
    message_1 = module_0.Message(text=str_0, code=str_0)
    var_0 = message_0 == message_1
    message_2 = module_0.Message(text=str_0, code=str_0)
    str_1 = 'abx'
    message_3 = module_0.Message(text=str_1, code=str_0)
    var_1 = message_2 == message_3
    message_4 = module_0.Message(text=str_0, code=str_0)
    var_2 = message_4 == message_4
    var_3 = None
    message_5 = module_0.Message(text=str_0, code=var_3)
    message_6 = module_0.Message(text=str_0, code=var_3)
    var_4 = message_5 == message_6
    message_7 = module_0.Message(text=str_0, code=var_3)
    message_8 = module_0.Message(text=str_0, code=str_0)
    var_5 = message_7 == message_8
    message_9 = module_0.Message(text=str_0, code=str_0)
    message_10 = module_0.Message(text=str_0, code=var_3)
    var_6 = message_9 == message_10
    str_2 = ''
    message_11 = module_0.Message(text=str_0, key=str_2)
    var_7 = message_11 == message_10