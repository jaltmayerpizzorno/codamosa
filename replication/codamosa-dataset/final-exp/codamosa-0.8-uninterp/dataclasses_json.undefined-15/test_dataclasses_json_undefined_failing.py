# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        str_0 = 'NQFF\nY^F'
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_0 = {str_0: str_0}
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_1.handle_from_dict(catch_all_undefined_parameters_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Meta'
        float_0 = -198.366
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, float_0: str_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        int_0 = -1276
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        dict_1 = raise_undefined_parameters_0.handle_from_dict(int_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '>$12w]m}x._Yu8\n\t'
        int_0 = 2409
        set_0 = {str_0, int_0}
        bytes_0 = b'O'
        list_0 = None
        list_1 = None
        dict_0 = {str_0: str_0, list_0: set_0, list_1: bytes_0}
        list_2 = []
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters(*list_2)
        int_1 = 816
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        dict_1 = ignore_undefined_parameters_0.handle_from_dict(int_1, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        undefined_parameter_action_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(undefined_parameter_action_0)
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        callable_1 = ignore_undefined_parameters_0.create_init(int_0)
        float_0 = 2590.73382
        callable_2 = ignore_undefined_parameters_0.create_init(float_0)
        undefined_parameter_action_1 = None
        undefined_parameter_error_0 = module_0.UndefinedParameterError(undefined_parameter_action_1)
    except BaseException:
        pass

def test_case_4():
    try:
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        str_0 = '\tU'
        str_1 = '8Z\t\ts`xv\t\x0bD57do^@'
        bytes_0 = b'\xcf\x1a(V\xed'
        bool_0 = True
        dict_0 = {catch_all_undefined_parameters_0: str_0, str_1: bool_0, str_1: bytes_0, catch_all_undefined_parameters_0: str_1}
        dict_1 = catch_all_undefined_parameters_0.handle_to_dict(bytes_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Nested dataclass field '
        dict_0 = {str_0: str_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(dict_0)
        list_0 = []
        dict_1 = {}
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters(*list_0, **dict_1)
        dict_2 = catch_all_undefined_parameters_1.handle_dump(callable_0)
    except BaseException:
        pass