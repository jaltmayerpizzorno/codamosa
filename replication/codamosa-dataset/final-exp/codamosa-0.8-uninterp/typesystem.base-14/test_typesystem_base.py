# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()

def test_case_1():
    str_0 = '/sOJLXF1xVi'
    int_0 = 2658
    int_1 = -1704
    int_2 = -2546
    position_0 = module_0.Position(int_0, int_1, int_2)
    message_0 = module_0.Message(text=str_0, key=str_0, start_position=position_0)
    str_1 = message_0.__repr__()

def test_case_2():
    str_0 = 'kPNgn>UaC>7!ZT:u'
    base_error_0 = module_0.BaseError(text=str_0, key=str_0)
    iterator_0 = base_error_0.__iter__()

def test_case_3():
    str_0 = '\x0bS.GK#y:,S6#'
    int_0 = -1613
    base_error_0 = module_0.BaseError(text=str_0, code=str_0, position=int_0)
    str_1 = None
    bool_0 = base_error_0.__eq__(str_1)

def test_case_4():
    int_0 = 12
    base_error_0 = module_0.BaseError(text=int_0)
    iterator_0 = base_error_0.__iter__()

def test_case_5():
    str_0 = '\x0bS.K#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
    bool_0 = message_0.__eq__(list_0)
    base_error_0 = module_0.BaseError(text=str_0, key=str_0)
    iterator_0 = base_error_0.__iter__()
    list_1 = [message_0, message_0]
    base_error_1 = module_0.BaseError(messages=list_1)
    int_1 = base_error_1.__hash__()

def test_case_6():
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()
    list_0 = []
    int_0 = 1474
    int_1 = -5296
    int_2 = -1646
    position_0 = module_0.Position(int_0, int_1, int_2)
    base_error_0 = module_0.BaseError(text=list_0, position=position_0)
    list_1 = base_error_0.messages()
    bool_0 = validation_result_0.__bool__()

def test_case_7():
    int_0 = 1
    float_0 = -596.9
    base_error_0 = module_0.BaseError(text=float_0)
    bool_0 = base_error_0.__eq__(int_0)
    iterator_0 = base_error_0.__iter__()
    int_1 = -2361
    list_0 = base_error_0.messages(add_prefix=int_1)
    int_2 = -3354
    int_3 = -602
    position_0 = module_0.Position(int_1, int_2, int_3)
    bool_1 = position_0.__eq__(position_0)
    str_0 = base_error_0.__repr__()

def test_case_8():
    str_0 = '\n    Raised by `typesystem.tokenize_json()` and `typesystem.tokenize_yaml()`.\n    '
    base_error_0 = module_0.BaseError(text=str_0, code=str_0)
    int_0 = base_error_0.__len__()
    int_1 = 12
    base_error_1 = module_0.BaseError(text=int_1)
    iterator_0 = base_error_1.__iter__()

def test_case_9():
    str_0 = '\x0bS.GK#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    parse_error_0 = module_0.ParseError(text=str_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
    bool_0 = message_0.__eq__(list_0)
    int_1 = -823
    position_1 = module_0.Position(int_0, int_1, int_1)
    int_2 = -3286
    base_error_0 = module_0.BaseError(text=str_0, key=int_2, position=position_0)
    str_1 = base_error_0.__str__()
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()
    bool_1 = base_error_0.__eq__(parse_error_0)

def test_case_10():
    float_0 = -596.9
    base_error_0 = module_0.BaseError(text=float_0)
    bool_0 = base_error_0.__eq__(float_0)

def test_case_11():
    int_0 = -15
    position_0 = module_0.Position(int_0, int_0, int_0)
    str_0 = position_0.__repr__()
    validation_result_0 = module_0.ValidationResult(value=int_0)
    bool_0 = validation_result_0.__bool__()
    var_0 = iter(validation_result_0)
    var_1 = next(var_0)
    var_2 = next(var_0)

def test_case_12():
    validation_result_0 = module_0.ValidationResult()
    str_0 = validation_result_0.__repr__()
    str_1 = validation_result_0.__repr__()
    iterator_0 = validation_result_0.__iter__()
    int_0 = None
    int_1 = -1456
    int_2 = -2833
    position_0 = module_0.Position(int_0, int_1, int_2)
    bool_0 = validation_result_0.__bool__()

def test_case_13():
    str_0 = '\x0bS.K#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    str_1 = 'kPNgn>UaC>7!ZT:u'
    int_0 = 1604
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_1, start_position=position_0, end_position=position_0)
    bool_0 = message_0.__eq__(list_0)
    base_error_0 = module_0.BaseError(text=str_0, key=str_0)
    bool_1 = position_0.__eq__(str_1)
    validation_result_0 = module_0.ValidationResult(value=message_0)
    iterator_0 = validation_result_0.__iter__()
    int_1 = -87
    str_2 = validation_result_0.__repr__()
    int_2 = 1594
    int_3 = 1
    position_1 = module_0.Position(int_2, int_1, int_3)

def test_case_14():
    str_0 = '\x0bS.GK#y:,S6#'
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0)
    int_1 = -2544
    position_1 = module_0.Position(int_0, int_1, int_1)
    bool_0 = message_0.__eq__(message_0)
    base_error_0 = module_0.BaseError(text=str_0, key=int_1)
    bool_1 = base_error_0.__eq__(base_error_0)

def test_case_15():
    str_0 = '\x0bS.GK#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
    bool_0 = message_0.__eq__(list_0)
    int_1 = -4351
    position_1 = module_0.Position(int_0, int_1, int_1)
    int_2 = -3286
    base_error_0 = module_0.BaseError(text=str_0, key=int_2, position=position_0)
    str_1 = base_error_0.__str__()
    int_3 = -1737
    int_4 = -2700
    position_2 = module_0.Position(int_3, int_0, int_4)
    iterator_0 = base_error_0.__iter__()
    bool_1 = position_2.__eq__(int_3)
    str_2 = base_error_0.__repr__()

def test_case_16():
    str_0 = '\x0bS.GK#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    parse_error_0 = module_0.ParseError(text=str_0)
    int_1 = -4351
    position_0 = module_0.Position(int_0, int_1, int_1)
    int_2 = -3286
    base_error_0 = module_0.BaseError(text=str_0, key=int_2, position=position_0)
    str_1 = base_error_0.__str__()
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()
    int_3 = -1737
    bool_0 = base_error_0.__eq__(list_0)
    bool_1 = position_0.__eq__(validation_result_0)
    iterator_1 = base_error_0.__iter__()
    int_4 = -2361
    position_1 = module_0.Position(int_3, int_2, int_4)
    bool_2 = position_1.__eq__(position_0)
    str_2 = base_error_0.__repr__()

def test_case_17():
    float_0 = 242.2
    str_0 = '0\\Z'
    validation_error_0 = module_0.ValidationError(text=float_0, code=str_0)
    validation_result_0 = module_0.ValidationResult(error=validation_error_0)
    iterator_0 = validation_result_0.__iter__()
    str_1 = validation_result_0.__repr__()
    str_2 = ':.v=s5)< G.9 }Fv2'
    parse_error_0 = None
    tuple_0 = None
    int_0 = -1645
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_2, index=parse_error_0, start_position=tuple_0)
    list_0 = [message_0]
    base_error_0 = module_0.BaseError(messages=list_0)

def test_case_18():
    str_0 = '\x0bS.GK#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
    bool_0 = message_0.__eq__(list_0)
    int_1 = -4351
    position_1 = module_0.Position(int_0, int_1, int_1)
    int_2 = -3286
    base_error_0 = module_0.BaseError(text=str_0, key=int_2, position=position_0)
    str_1 = base_error_0.__str__()
    validation_result_0 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()
    int_3 = -1737
    int_4 = -2700
    position_2 = module_0.Position(int_3, int_0, int_4)
    bool_1 = position_1.__eq__(validation_result_0)
    iterator_1 = base_error_0.__iter__()
    bool_2 = position_1.__eq__(position_0)
    str_2 = base_error_0.__repr__()

def test_case_19():
    str_0 = '\x0bS.GK#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_0)
    bool_0 = message_0.__eq__(list_0)
    int_1 = -823
    int_2 = 1
    int_3 = -4351
    int_4 = -1443
    position_1 = module_0.Position(int_4, int_0, int_4)
    optional_0 = None
    base_error_0 = module_0.BaseError(text=str_0, key=int_3, position=position_0, messages=optional_0)
    str_1 = base_error_0.__str__()
    str_2 = ''
    validation_error_0 = module_0.ValidationError(text=str_2, code=str_2)
    validation_result_0 = module_0.ValidationResult(error=validation_error_0)
    validation_result_1 = module_0.ValidationResult()
    iterator_0 = validation_result_0.__iter__()
    int_5 = -2936
    int_6 = 758
    position_2 = module_0.Position(int_1, int_5, int_6)
    position_3 = module_0.Position(int_6, int_5, int_1)
    bool_1 = position_3.__eq__(int_2)
    iterator_1 = base_error_0.__iter__()
    bool_2 = position_2.__eq__(iterator_0)
    list_1 = [message_0, message_0, message_0, message_0]
    base_error_1 = module_0.BaseError(messages=list_1)
    str_3 = base_error_1.__repr__()

def test_case_20():
    str_0 = '\x0bS.GK#y:,S6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0)
    str_1 = '>"QO'
    int_1 = -2544
    position_1 = module_0.Position(int_0, int_1, int_1)
    message_1 = module_0.Message(text=str_1, code=str_0, start_position=position_0, end_position=position_1)
    bool_0 = message_1.__eq__(message_0)
    int_2 = message_1.__hash__()
    int_3 = 1940
    str_2 = message_1.__repr__()
    str_3 = position_1.__repr__()
    int_4 = 3
    int_5 = 1038
    position_2 = module_0.Position(int_3, int_4, int_5)
    base_error_0 = module_0.BaseError(text=str_1)
    str_4 = base_error_0.__str__()
    validation_result_0 = module_0.ValidationResult()
    bool_1 = base_error_0.__eq__(list_0)
    int_6 = -248
    position_3 = module_0.Position(int_4, int_4, int_6)
    bool_2 = position_3.__eq__(validation_result_0)
    iterator_0 = base_error_0.__iter__()

def test_case_21():
    str_0 = 'cannot be greater than 20'
    validation_error_0 = module_0.ValidationError(text=str_0)
    validation_result_0 = module_0.ValidationResult(error=validation_error_0)
    var_0 = iter(validation_result_0)
    var_1 = next(var_0)
    var_2 = next(var_0)

def test_case_22():
    str_0 = 'oZ-kquq'
    validation_result_0 = module_0.ValidationResult()
    bool_0 = validation_result_0.__bool__()
    message_0 = module_0.Message(text=str_0)
    base_error_0 = module_0.BaseError(text=str_0)
    bool_1 = base_error_0.__eq__(bool_0)
    bool_2 = message_0.__eq__(base_error_0)
    int_0 = message_0.__hash__()
    str_1 = '\r0]"W{'
    message_1 = module_0.Message(text=str_0, start_position=str_1)
    str_2 = message_0.__repr__()
    str_3 = validation_result_0.__repr__()
    str_4 = 'cs%/<zB`C^#\n-% Ji!'
    base_error_1 = module_0.BaseError(text=str_4, key=str_4)
    list_0 = base_error_1.messages(add_prefix=str_0)
    bool_3 = message_1.__eq__(message_0)
    bool_4 = message_0.__eq__(message_0)
    int_1 = 625
    int_2 = 2
    position_0 = module_0.Position(int_1, int_1, int_2)
    str_5 = position_0.__repr__()

def test_case_23():
    str_0 = '\x0bSGK#y:,6#'
    list_0 = [str_0, str_0, str_0]
    int_0 = 1627
    position_0 = module_0.Position(int_0, int_0, int_0)
    message_0 = module_0.Message(text=str_0, start_position=position_0)
    str_1 = '>"QO'
    int_1 = -2544
    position_1 = module_0.Position(int_0, int_1, int_1)
    bool_0 = message_0.__eq__(message_0)
    int_2 = -4300
    int_3 = message_0.__hash__()
    int_4 = 1940
    str_2 = message_0.__repr__()
    str_3 = position_1.__repr__()
    int_5 = 3
    str_4 = position_0.__repr__()
    int_6 = 1038
    position_2 = module_0.Position(int_4, int_5, int_6)
    base_error_0 = module_0.BaseError(text=str_1)
    str_5 = base_error_0.__str__()
    validation_result_0 = module_0.ValidationResult()
    bool_1 = base_error_0.__eq__(list_0)
    int_7 = 1580
    str_6 = position_0.__repr__()
    int_8 = -5593
    position_3 = module_0.Position(int_5, int_7, int_8)
    bool_2 = position_0.__eq__(str_1)
    set_0 = {int_2, int_6}
    bool_3 = base_error_0.__eq__(set_0)
    float_0 = 2211.159549
    bool_4 = position_1.__eq__(float_0)
    str_7 = 'N4x]#7AkCHL'
    base_error_1 = module_0.BaseError(text=str_1, code=str_2, key=str_7, position=position_2)
    validation_error_0 = module_0.ValidationError(text=str_5)
    bool_5 = base_error_0.__eq__(validation_error_0)