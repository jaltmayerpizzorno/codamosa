# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        str_0 = 'default'
        dict_0 = {catch_all_undefined_parameters_0: catch_all_undefined_parameters_0, catch_all_undefined_parameters_0: str_0}
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        dict_1 = raise_undefined_parameters_0.handle_from_dict(str_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "s$'aC3Y{Z7Q60m.t*\tg"
        dict_0 = {}
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        dict_1 = ignore_undefined_parameters_0.handle_from_dict(str_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x01\xc7)\xd6\xe6\xf9\x1b\xef\x85'
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        str_0 = 'CatchAllVar'
        str_1 = '\n            Raises exception because this class should not be inherited.\n            This class is helper only.\n            '
        dict_0 = {str_0: str_0, str_1: bytes_0}
        int_0 = 2347
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(int_0)
        float_0 = -709.8791
        undefined_parameter_error_0 = module_0.UndefinedParameterError(float_0, callable_0)
        undefined_parameter_error_1 = module_0.UndefinedParameterError(undefined_parameter_error_0, **dict_0)
        callable_1 = catch_all_undefined_parameters_0.create_init(undefined_parameter_error_1)
        dict_1 = {}
        callable_2 = ignore_undefined_parameters_0.create_init(dict_1)
        undefined_parameter_action_0 = module_0._UndefinedParameterAction()
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = None
        str_0 = '((\n\t<2'
        float_0 = -2352.9225
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        dict_1 = {dict_0: ignore_undefined_parameters_0, ignore_undefined_parameters_0: str_0, str_0: float_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_2 = catch_all_undefined_parameters_0.handle_from_dict(float_0, dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        undefined_0 = module_0.Undefined.INCLUDE
        bool_0 = False
        dict_0 = {bool_0: bool_0}
        str_0 = 'T'
        dict_1 = {}
        dict_2 = {bool_0: dict_0, undefined_0: str_0}
        list_0 = []
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters(*list_0)
        dict_3 = catch_all_undefined_parameters_0.handle_to_dict(dict_1, dict_2)
    except BaseException:
        pass

def test_case_5():
    try:
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_0 = catch_all_undefined_parameters_0.handle_dump(ignore_undefined_parameters_0)
    except BaseException:
        pass