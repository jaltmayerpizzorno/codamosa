# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        dict_0 = {}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        list_0 = [dict_0]
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        callable_0 = ignore_undefined_parameters_0.create_init(list_0)
        ignore_undefined_parameters_1 = module_0._IgnoreUndefinedParameters()
        float_0 = -747.8675
        dict_1 = {}
        dict_2 = catch_all_undefined_parameters_0.handle_from_dict(float_0, dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        bool_0 = True
        dict_0 = {raise_undefined_parameters_0: raise_undefined_parameters_0, bool_0: raise_undefined_parameters_0}
        dict_1 = {}
        dict_2 = raise_undefined_parameters_0.handle_from_dict(dict_1, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 828.02
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        callable_0 = ignore_undefined_parameters_0.create_init(float_0)
        undefined_parameter_action_0 = module_0._UndefinedParameterAction()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_to_dict(bool_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_0 = catch_all_undefined_parameters_0.handle_dump(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\tw9u R>b`YQH-'
        int_0 = 1417
        str_1 = 'De'
        dict_0 = {str_0: int_0, str_1: str_0}
        undefined_parameter_error_0 = module_0.UndefinedParameterError(int_0, dict_0, **dict_0)
        dict_1 = None
        list_0 = []
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters(*list_0)
        dict_2 = ignore_undefined_parameters_0.handle_from_dict(undefined_parameter_error_0, dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(catch_all_undefined_parameters_0)
        str_0 = 'pvCI\x0bZJ5Wc0bl+f,SoY'
        str_1 = '|A3h?eACtncYJIk0'
        str_2 = '(pRR\tp=]d=\r\nJs'
        undefined_parameter_error_0 = None
        tuple_0 = (undefined_parameter_error_0, ignore_undefined_parameters_0)
        dict_0 = {tuple_0: ignore_undefined_parameters_0, str_1: str_0}
        dict_1 = catch_all_undefined_parameters_0.handle_to_dict(str_2, dict_0)
    except BaseException:
        pass