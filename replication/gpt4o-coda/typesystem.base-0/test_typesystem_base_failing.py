# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    try:
        base_error_0 = module_0.BaseError()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'G5+An'
        int_0 = 3
        int_1 = 1
        position_0 = module_0.Position(int_0, int_1, int_0)
        message_0 = module_0.Message(text=str_0, code=str_0, key=str_0, position=position_0, end_position=position_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "'pyyaml' must be installed."
        str_1 = '[XJ\ris\\|$YdF0'
        parse_error_0 = module_0.ParseError(text=str_0, code=str_1)
        base_error_0 = module_0.BaseError(key=parse_error_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 3670
        int_1 = -3203
        int_2 = 1852
        int_3 = 905
        position_0 = module_0.Position(int_1, int_2, int_3)
        base_error_0 = module_0.BaseError(messages=int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 787
        int_1 = -1164
        str_0 = ''
        base_error_0 = module_0.BaseError(text=str_0)
        str_1 = base_error_0.__str__()
        str_2 = base_error_0.__str__()
        str_3 = base_error_0.__repr__()
        validation_result_0 = module_0.ValidationResult()
        bool_0 = validation_result_0.__bool__()
        position_0 = module_0.Position(int_0, int_1, int_0)
        str_4 = '2U <r8j\n\x0cq@SKg'
        optional_0 = None
        message_0 = module_0.Message(text=str_4, code=str_0, index=optional_0, start_position=position_0)
        iterator_0 = base_error_0.__iter__()
        message_1 = module_0.Message(text=str_0, key=str_0, index=validation_result_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        bool_1 = True
        any_0 = None
        validation_result_0 = module_0.ValidationResult(value=any_0)
        base_error_0 = module_0.BaseError(text=bool_1)
        validation_result_1 = module_0.ValidationResult()
        int_0 = base_error_0.__len__()
        iterator_0 = base_error_0.__iter__()
        str_0 = validation_result_1.__repr__()
        base_error_1 = module_0.BaseError(position=bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        int_0 = -2197
        int_1 = 1891
        position_0 = module_0.Position(int_0, int_1, int_1)
        base_error_0 = module_0.BaseError(text=str_0)
        str_1 = base_error_0.__repr__()
        base_error_1 = module_0.BaseError(code=str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'(6H\xa1\x06\xdd\x14.\x9a_M\xf7'
        str_0 = 'Nv)'
        validation_error_0 = module_0.ValidationError(text=bytes_0, key=str_0)
        validation_result_0 = module_0.ValidationResult(error=validation_error_0)
        str_1 = validation_result_0.__repr__()
        validation_error_1 = module_0.ValidationError()
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        validation_result_0 = module_0.ValidationResult(error=dict_0)
        bool_0 = validation_result_0.__bool__()
        bool_1 = validation_result_0.__bool__()
        validation_error_0 = module_0.ValidationError()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '&e!'
        message_0 = module_0.Message(text=str_0)
        list_0 = [message_0, message_0, message_0]
        int_0 = 2307
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_1 = module_0.Message(text=str_0, key=str_0, index=list_0, position=position_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ':8'
        str_1 = 'additionalItems'
        list_0 = [str_1, str_1, str_0]
        message_0 = module_0.Message(text=str_1, code=str_1, index=list_0)
        list_1 = [message_0, message_0]
        validation_error_0 = module_0.ValidationError(code=str_0, messages=list_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '5<$},E<y'
        int_0 = 1956
        set_0 = {str_0}
        validation_result_0 = module_0.ValidationResult(value=set_0)
        validation_result_1 = module_0.ValidationResult(value=validation_result_0)
        bool_0 = validation_result_1.__bool__()
        int_1 = 2209
        position_0 = module_0.Position(int_1, int_0, int_1)
        message_0 = module_0.Message(text=str_0, code=str_0, end_position=position_0)
        list_0 = [message_0]
        base_error_0 = module_0.BaseError(key=str_0, messages=list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "Q/@S9. e'0$2"
        str_1 = 'j,g'
        bool_0 = True
        base_error_0 = module_0.BaseError(text=str_0, key=str_1, messages=bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        list_0 = []
        base_error_0 = module_0.BaseError(messages=list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        optional_0 = None
        bool_0 = True
        optional_1 = None
        str_0 = 'Must be a real datetime.'
        int_0 = 0
        int_1 = -2820
        int_2 = -2286
        position_0 = module_0.Position(int_0, int_1, int_2)
        position_1 = module_0.Position(int_0, int_2, int_2)
        message_0 = module_0.Message(text=str_0, start_position=position_0, end_position=position_1)
        list_0 = [message_0, message_0]
        parse_error_0 = module_0.ParseError(code=optional_1, messages=list_0)
        base_error_0 = module_0.BaseError(text=optional_0, position=bool_0, messages=parse_error_0)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = 787
        int_1 = -1164
        str_0 = ''
        base_error_0 = module_0.BaseError(text=str_0)
        str_1 = base_error_0.__str__()
        str_2 = base_error_0.__str__()
        str_3 = base_error_0.__repr__()
        validation_result_0 = module_0.ValidationResult()
        bool_0 = validation_result_0.__bool__()
        position_0 = module_0.Position(int_0, int_1, int_0)
        str_4 = '2U <r8j\n\x0cq@SKg'
        int_2 = base_error_0.__hash__()
        optional_0 = None
        message_0 = module_0.Message(text=str_4, code=str_0, index=optional_0, start_position=position_0)
        iterator_0 = base_error_0.__iter__()
        message_1 = module_0.Message(text=str_0, key=str_0, index=validation_result_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '=V=T{'
        int_0 = -2934
        int_1 = -2070
        int_2 = 1205
        position_0 = module_0.Position(int_0, int_1, int_2)
        bool_0 = position_0.__eq__(str_0)
        str_1 = ''
        validation_result_0 = module_0.ValidationResult(error=str_1)
        str_2 = validation_result_0.__repr__()
        int_3 = 1938
        str_3 = 'o\\9er\\dS<,js*5b\r(0g9'
        str_4 = None
        list_0 = [int_3, str_0, str_4]
        message_0 = module_0.Message(text=str_3, code=str_3, index=list_0)
        str_5 = message_0.__repr__()
        parse_error_0 = module_0.ParseError(text=str_5)
        bool_1 = message_0.__eq__(parse_error_0)
        validation_error_0 = module_0.ValidationError(text=str_0)
        int_4 = -910
        int_5 = 604
        position_1 = module_0.Position(int_4, int_4, int_5)
        message_1 = module_0.Message(text=str_3, index=list_0, position=position_1, start_position=position_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '.\\f%)3reeaYx_V,9rjE'
        set_0 = {str_0, str_0, str_0}
        bool_0 = True
        validation_result_0 = module_0.ValidationResult(value=set_0, error=bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 1938
        str_0 = 'o\\9er\\dS<,js*5b\r(0g9'
        str_1 = ' rfaccC\tJeO\\?8\ty'
        message_0 = module_0.Message(text=str_1, key=int_0)
        list_0 = [message_0, message_0]
        validation_error_0 = module_0.ValidationError(messages=list_0)
        message_1 = module_0.Message(text=str_1, position=validation_error_0)
        str_2 = message_1.__repr__()
        int_1 = 3002
        position_0 = module_0.Position(int_0, int_0, int_1)
        bool_0 = position_0.__eq__(int_0)
        validation_error_1 = module_0.ValidationError(text=str_0, key=str_1, position=position_0)
        validation_result_0 = module_0.ValidationResult(error=validation_error_1)
        validation_error_2 = module_0.ValidationError(text=str_1)
        message_2 = module_0.Message(text=str_1, code=str_1)
        bool_1 = message_2.__eq__(message_2)
        str_3 = message_0.__repr__()
        bool_2 = position_0.__eq__(position_0)
        parse_error_0 = module_0.ParseError(text=str_2)
        validation_error_3 = module_0.ValidationError()
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'j'
        message_0 = module_0.Message(text=str_0)
        int_0 = 1864
        validation_result_0 = module_0.ValidationResult()
        str_1 = validation_result_0.__repr__()
        position_0 = module_0.Position(int_0, int_0, int_0)
        bool_0 = validation_result_0.__bool__()
        int_1 = message_0.__hash__()
        list_0 = [str_0, str_0]
        message_1 = module_0.Message(text=str_0, index=list_0, position=position_0)
        str_2 = '~4].1M\\(~eRlGa/bp%'
        message_2 = module_0.Message(text=str_2)
        bool_1 = message_0.__eq__(message_1)
        list_1 = [message_1, message_0, message_2, message_1]
        base_error_0 = module_0.BaseError(text=str_0, code=str_0, position=position_0, messages=list_1)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 1938
        str_0 = 'o\\9er\\dS<,js*5b\r(0g9'
        str_1 = ' rfaccC\tJeO\\?8\ty'
        message_0 = module_0.Message(text=str_1, key=int_0)
        list_0 = [message_0, message_0]
        validation_error_0 = module_0.ValidationError(messages=list_0)
        message_1 = module_0.Message(text=str_1, position=validation_error_0)
        str_2 = message_1.__repr__()
        int_1 = 3002
        position_0 = module_0.Position(int_0, int_0, int_1)
        bool_0 = position_0.__eq__(int_0)
        validation_error_1 = module_0.ValidationError(text=str_0, key=str_1, position=position_0)
        validation_result_0 = module_0.ValidationResult(error=validation_error_1)
        validation_error_2 = module_0.ValidationError(text=str_1)
        message_2 = module_0.Message(text=str_1, code=str_1)
        bool_1 = message_0.__eq__(message_2)
        bool_2 = message_2.__eq__(message_2)
        str_3 = message_0.__repr__()
        bool_3 = message_1.__eq__(validation_error_2)
        str_4 = message_0.__repr__()
        bool_4 = position_0.__eq__(position_0)
        parse_error_0 = module_0.ParseError(text=str_3)
        validation_error_3 = module_0.ValidationError()
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = ' rfa\tJ,O\\?8\ty'
        validation_result_0 = module_0.ValidationResult()
        message_0 = module_0.Message(text=str_0, index=validation_result_0)
        int_0 = message_0.__hash__()
        validation_result_1 = module_0.ValidationResult()
        int_1 = -301
        int_2 = -822
        int_3 = 1528
        position_0 = module_0.Position(int_1, int_2, int_3)
        bool_0 = position_0.__eq__(validation_result_1)
        bool_1 = validation_result_1.__bool__()
        iterator_0 = validation_result_1.__iter__()
        str_1 = 'T4)-gW@\tSJ('
        set_0 = None
        float_0 = 1089.183883
        base_error_0 = module_0.BaseError(text=str_1, key=str_1)
        str_2 = validation_result_1.__repr__()
        int_4 = base_error_0.__hash__()
        set_1 = {float_0, int_4, set_0, base_error_0}
        validation_error_0 = module_0.ValidationError(messages=set_1)
    except BaseException:
        pass