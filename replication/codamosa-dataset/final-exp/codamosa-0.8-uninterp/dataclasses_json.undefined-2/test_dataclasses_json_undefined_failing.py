# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        dict_0 = {raise_undefined_parameters_0: raise_undefined_parameters_0, raise_undefined_parameters_0: raise_undefined_parameters_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_from_dict(raise_undefined_parameters_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        raise_undefined_parameters_0 = None
        dict_0 = {}
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        dict_1 = ignore_undefined_parameters_0.handle_from_dict(raise_undefined_parameters_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        str_0 = '">'
        str_1 = '). Value cannot be deserialized properly.'
        dict_0 = {}
        callable_0 = ignore_undefined_parameters_0.create_init(dict_0)
        str_2 = "'xH^_"
        dict_1 = {str_0: str_0, str_1: ignore_undefined_parameters_0, str_1: ignore_undefined_parameters_0, str_2: ignore_undefined_parameters_0}
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters(**dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = None
        dict_1 = {dict_0: dict_0, dict_0: dict_0, dict_0: dict_0, dict_0: dict_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_2 = catch_all_undefined_parameters_0.handle_to_dict(dict_0, dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'x\x0cgVFn,u\\2BCX2v G,'
        str_1 = '-.6^6@agI/rA'
        dict_0 = {str_0: str_0, str_1: str_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_dump(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '_r'
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        str_1 = '\n    This action does nothing when it encounters undefined parameters.\n    The undefined parameters can not be retrieved after the class has been\n    created.\n    '
        dict_0 = {str_0: catch_all_undefined_parameters_0, str_1: str_1, str_1: str_1}
        list_0 = [dict_0, dict_0, dict_0]
        list_1 = [list_0, str_0, str_0]
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        undefined_0 = module_0.Undefined.INCLUDE
        dict_1 = {str_0: dict_0, str_1: undefined_0}
        dict_2 = raise_undefined_parameters_0.handle_from_dict(list_1, dict_1)
    except BaseException:
        pass