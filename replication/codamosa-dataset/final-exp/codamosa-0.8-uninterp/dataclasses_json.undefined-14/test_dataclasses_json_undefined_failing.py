# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        dict_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(dict_0)
        str_0 = 'x'
        float_0 = 1341.799
        dict_1 = {str_0: float_0, str_0: str_0, str_0: float_0}
        dict_2 = {float_0: catch_all_undefined_parameters_0, dict_0: catch_all_undefined_parameters_0, callable_0: catch_all_undefined_parameters_0, catch_all_undefined_parameters_0: dict_1}
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        dict_3 = raise_undefined_parameters_0.handle_from_dict(dict_1, dict_2)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '?\r\ngi{`)w\x0c;'
        str_1 = 'J2_3,'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
        dict_1 = {}
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters(**dict_1)
        callable_0 = ignore_undefined_parameters_0.create_init(dict_0)
        float_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_2 = catch_all_undefined_parameters_0.handle_dump(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_0 = catch_all_undefined_parameters_0.handle_dump(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(dict_0)
        list_0 = []
        dict_1 = None
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters(*list_0)
        dict_2 = ignore_undefined_parameters_0.handle_from_dict(list_0, dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'H\nTM}I%\x0bT>I/{4\n{R8'
        float_0 = -148.8439
        dict_0 = {str_0: float_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_from_dict(float_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        dict_0 = {}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_to_dict(bool_0, dict_0)
    except BaseException:
        pass