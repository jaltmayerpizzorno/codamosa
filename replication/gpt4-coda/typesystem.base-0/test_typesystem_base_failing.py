# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    try:
        int_0 = 2
        int_1 = 924
        position_0 = module_0.Position(int_0, int_1, int_0)
        str_0 = position_0.__repr__()
        base_error_0 = module_0.BaseError()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '/'
        str_1 = 'true'
        message_0 = module_0.Message(text=str_0, key=str_0, position=str_1)
        str_2 = '_Z?nex^x9Q.mCx'
        validation_error_0 = module_0.ValidationError(code=str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 0
        int_1 = -2112
        position_0 = module_0.Position(int_0, int_0, int_1)
        str_0 = 'um(YZ\nn=9+a\x0b\\X \re?j'
        list_0 = []
        message_0 = module_0.Message(text=str_0, index=list_0)
        str_1 = message_0.__repr__()
        str_2 = None
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()
        base_error_0 = module_0.BaseError(text=str_2, key=int_1, messages=iterator_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -354
        int_1 = 1
        position_0 = module_0.Position(int_0, int_0, int_1)
        message_0 = None
        str_0 = '('
        message_1 = module_0.Message(text=str_0, key=str_0)
        list_0 = [message_0, message_0, message_0, message_1]
        base_error_0 = module_0.BaseError(code=position_0, key=int_0, messages=list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'allOf'
        list_0 = [str_0, str_0, str_0]
        str_1 = 'L\x0b{'
        parse_error_0 = module_0.ParseError(text=str_0, position=str_1)
        message_0 = module_0.Message(text=str_0, index=list_0, start_position=parse_error_0)
        list_1 = [message_0, message_0]
        str_2 = 'f7f1V\nm 80%_ip6lH_g'
        int_0 = None
        int_1 = -4306
        position_0 = module_0.Position(int_0, int_1, int_0)
        message_1 = module_0.Message(text=str_2, start_position=position_0)
        list_2 = [message_1, message_1, message_1, message_1]
        base_error_0 = module_0.BaseError(text=list_2)
        var_0 = base_error_0.__getitem__(list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -1050
        int_1 = -2393
        position_0 = module_0.Position(int_1, int_1, int_1)
        str_0 = position_0.__repr__()
        bool_0 = position_0.__eq__(int_0)
        str_1 = '*Z;nrq.__a_u'
        base_error_0 = module_0.BaseError(key=str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '#/definitions/'
        float_0 = -3000.26746
        message_0 = module_0.Message(text=str_0, position=float_0)
        list_0 = [str_0, str_0, str_0, str_0]
        float_1 = 1868.073187
        message_1 = module_0.Message(text=str_0, key=str_0, index=list_0, start_position=float_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'fAy{\\_ty?\x0c'
        base_error_0 = module_0.BaseError(text=str_0)
        bool_0 = base_error_0.__eq__(str_0)
        bool_1 = base_error_0.__eq__(str_0)
        int_0 = 1180
        position_0 = module_0.Position(int_0, int_0, int_0)
        message_0 = module_0.Message(text=str_0, key=str_0, position=position_0, start_position=position_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ''
        validation_result_0 = module_0.ValidationResult()
        message_0 = module_0.Message(text=str_0)
        bool_0 = message_0.__eq__(str_0)
        str_1 = validation_result_0.__repr__()
        validation_result_1 = module_0.ValidationResult(value=str_0)
        iterator_0 = validation_result_1.__iter__()
        validation_result_2 = module_0.ValidationResult(value=str_0, error=iterator_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'lcw'
        int_0 = 1
        position_0 = module_0.Position(int_0, int_0, int_0)
        bool_0 = position_0.__eq__(position_0)
        list_0 = [str_0, str_0, position_0, position_0]
        list_1 = [position_0, str_0, list_0, list_0]
        base_error_0 = module_0.BaseError(key=str_0, position=position_0, messages=list_1)
    except BaseException:
        pass

def test_case_10():
    try:
        validation_result_0 = module_0.ValidationResult()
        str_0 = validation_result_0.__repr__()
        str_1 = validation_result_0.__repr__()
        bool_0 = validation_result_0.__bool__()
        int_0 = 6
        int_1 = 609
        position_0 = module_0.Position(int_0, int_1, int_0)
        message_0 = module_0.Message(text=str_1, key=str_1)
        base_error_0 = module_0.BaseError(position=position_0, messages=message_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = True
        str_0 = '0!A/*.+%WA7'
        list_0 = []
        int_0 = 1057
        int_1 = -2822
        str_1 = 'ZfoEK"\'K*^4TO'
        int_2 = -270
        int_3 = 1157
        int_4 = 3387
        position_0 = module_0.Position(int_2, int_3, int_4)
        base_error_0 = module_0.BaseError(text=str_0, key=str_1, position=position_0)
        bool_1 = base_error_0.__eq__(bool_0)
        position_1 = module_0.Position(int_0, int_1, int_0)
        message_0 = module_0.Message(text=str_0, code=str_0, index=list_0, start_position=position_1, end_position=position_1)
        base_error_1 = module_0.BaseError(text=bool_0, messages=message_0)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        int_0 = 5
        int_1 = 1338
        position_0 = module_0.Position(int_0, int_1, int_1)
        bool_0 = position_0.__eq__(list_0)
        base_error_0 = module_0.BaseError(messages=list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '||jJ/}gR#\x0cbR6'
        list_0 = []
        dict_0 = {str_0: list_0}
        base_error_0 = module_0.BaseError(text=str_0, key=str_0, position=dict_0)
        str_1 = base_error_0.__repr__()
        validation_error_0 = module_0.ValidationError(text=str_0)
        validation_error_1 = module_0.ValidationError(text=str_1)
        base_error_1 = module_0.BaseError(position=str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'>\xf7\xae\xc4'
        validation_result_0 = module_0.ValidationResult(error=bytes_0)
        str_0 = validation_result_0.__repr__()
        str_1 = 'ynX@3R-X(*YZI"?6E'
        int_0 = 3711
        int_1 = 1597
        position_0 = module_0.Position(int_0, int_0, int_1)
        base_error_0 = module_0.BaseError(code=str_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = "'Xo37whH>k\tX\r"
        int_0 = -3434
        int_1 = -1473
        position_0 = module_0.Position(int_0, int_1, int_0)
        message_0 = module_0.Message(text=str_0, code=str_0, position=position_0, end_position=position_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "'1%tHh>#"
        none_type_0 = None
        int_0 = -976
        int_1 = 308
        int_2 = -27
        position_0 = module_0.Position(int_0, int_1, int_2)
        validation_error_0 = module_0.ValidationError(text=str_0, key=str_0, position=position_0)
        base_error_0 = module_0.BaseError(text=str_0)
        str_1 = base_error_0.__repr__()
        list_0 = base_error_0.messages()
        validation_result_0 = module_0.ValidationResult(value=none_type_0)
        int_3 = -8
        int_4 = base_error_0.__len__()
        int_5 = base_error_0.__hash__()
        str_2 = base_error_0.__str__()
        int_6 = -742
        bool_0 = validation_result_0.__bool__()
        str_3 = validation_result_0.__repr__()
        position_1 = module_0.Position(int_3, int_6, int_1)
        message_0 = module_0.Message(text=str_0, key=str_0, start_position=position_1)
        base_error_1 = module_0.BaseError(text=str_0)
        int_7 = message_0.__hash__()
        iterator_0 = base_error_1.__iter__()
        iterator_1 = validation_result_0.__iter__()
        str_4 = message_0.__repr__()
        list_1 = base_error_0.messages(add_prefix=int_3)
        str_5 = message_0.__repr__()
        bool_1 = base_error_1.__eq__(str_5)
        int_8 = None
        base_error_2 = module_0.BaseError(key=int_8, messages=list_0)
        bool_2 = message_0.__eq__(message_0)
        message_1 = module_0.Message(text=str_0, code=str_4, key=int_7)
        str_6 = base_error_1.__repr__()
        bool_3 = base_error_0.__eq__(validation_error_0)
        var_0 = base_error_0.__getitem__(bool_1)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 350
        int_1 = -879
        position_0 = module_0.Position(int_0, int_0, int_1)
        int_2 = -440
        int_3 = -957
        bool_0 = position_0.__eq__(int_2)
        bool_1 = position_0.__eq__(int_1)
        position_1 = module_0.Position(int_2, int_3, int_2)
        bool_2 = position_1.__eq__(position_0)
        validation_result_0 = module_0.ValidationResult()
        int_4 = 175
        str_0 = 'properties'
        list_0 = [str_0, int_4]
        float_0 = 636.6646
        bool_3 = position_1.__eq__(int_2)
        message_0 = module_0.Message(text=str_0, index=list_0, start_position=float_0)
        iterator_0 = validation_result_0.__iter__()
        str_1 = position_0.__repr__()
        int_5 = -1955
        str_2 = validation_result_0.__repr__()
        iterator_1 = validation_result_0.__iter__()
        position_2 = module_0.Position(int_4, int_4, int_5)
        bytes_0 = b'O'
        base_error_0 = module_0.BaseError(code=str_0, messages=bytes_0)
    except BaseException:
        pass