# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        str_0 = ',B=g05x~&8'
        dict_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_from_dict(str_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        dict_0 = {raise_undefined_parameters_0: raise_undefined_parameters_0, raise_undefined_parameters_0: raise_undefined_parameters_0}
        list_0 = None
        dict_1 = raise_undefined_parameters_0.handle_from_dict(list_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        str_0 = "2)!. &\n'^\x0cwm"
        undefined_0 = None
        dict_0 = {undefined_0: str_0}
        dict_1 = ignore_undefined_parameters_0.handle_from_dict(undefined_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        undefined_0 = module_0.Undefined.RAISE
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        callable_0 = ignore_undefined_parameters_0.create_init(undefined_0)
        ignore_undefined_parameters_1 = module_0._IgnoreUndefinedParameters()
    except BaseException:
        pass

def test_case_4():
    try:
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        list_0 = [catch_all_undefined_parameters_0, catch_all_undefined_parameters_0, catch_all_undefined_parameters_0, catch_all_undefined_parameters_0]
        dict_0 = {catch_all_undefined_parameters_0: list_0}
        undefined_0 = module_0.Undefined.EXCLUDE
        dict_1 = catch_all_undefined_parameters_0.handle_to_dict(undefined_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        bytes_0 = b'\xc6\xdd\x19\x82'
        str_0 = 'init'
        str_1 = "i83zS\rkPI+9xN8LnK'7\x0c"
        str_2 = "\x0bU4,V%D0YLJ'#db!"
        dict_0 = {str_1: catch_all_undefined_parameters_0, str_2: str_1}
        undefined_parameter_error_0 = module_0.UndefinedParameterError(bytes_0, str_0, dict_0, **dict_0)
        dict_1 = catch_all_undefined_parameters_0.handle_dump(undefined_parameter_error_0)
    except BaseException:
        pass

def test_case_6():
    try:
        undefined_parameter_error_0 = None
        float_0 = -1149.526
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(float_0)
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        callable_1 = ignore_undefined_parameters_0.create_init(callable_0)
        dict_0 = {float_0: float_0, catch_all_undefined_parameters_0: ignore_undefined_parameters_0, undefined_parameter_error_0: callable_0, callable_0: catch_all_undefined_parameters_0}
        list_0 = []
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters(*list_0)
        dict_1 = catch_all_undefined_parameters_1.handle_from_dict(callable_1, dict_0)
    except BaseException:
        pass