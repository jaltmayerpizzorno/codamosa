# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        str_0 = 'iu\t'
        dict_0 = None
        dict_1 = ignore_undefined_parameters_0.handle_from_dict(str_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        str_0 = 'JBtn}6\n.\\3b!r'
        dict_0 = {str_0: str_0}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        undefined_parameter_error_0 = module_0.UndefinedParameterError(raise_undefined_parameters_0, list_0, **dict_0)
        dict_1 = None
        dict_2 = raise_undefined_parameters_0.handle_from_dict(undefined_parameter_error_0, dict_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '$]".\\J)-}kr9vRcN.'
        str_1 = 'z<{'
        bytes_0 = b'\xd5\xe0$y\xf5B\x96^\xf4&\x18K'
        dict_0 = {str_0: str_0, str_1: str_0, str_0: bytes_0}
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        callable_0 = ignore_undefined_parameters_0.create_init(dict_0)
        undefined_parameter_action_0 = module_0._UndefinedParameterAction()
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = None
        str_0 = ' and was defaulted to None by infer_missing=True. Set infer_missing=False (the default) to prevent this behavior.'
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        set_1 = {catch_all_undefined_parameters_0}
        var_0 = None
        var_1 = None
        undefined_parameter_error_0 = module_0.UndefinedParameterError(var_0, str_0, var_1)
        list_0 = [set_1, set_0, undefined_parameter_error_0]
        dict_0 = {catch_all_undefined_parameters_0: str_0}
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_1.handle_to_dict(list_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        undefined_parameter_action_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_0 = catch_all_undefined_parameters_0.handle_dump(undefined_parameter_action_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ' and was defaulted to None by infer_missing=True. Set infer_missing=False (the default) to prevent this behavior.'
        dict_0 = {}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        var_0 = None
        var_1 = None
        undefined_parameter_error_0 = module_0.UndefinedParameterError(var_1, str_0, var_0)
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_from_dict(str_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        str_0 = ' with either the `dataclass_json` decorator or mixin.'
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        callable_0 = catch_all_undefined_parameters_0.create_init(str_0)
        str_1 = None
        tuple_0 = (callable_0, str_1)
        str_2 = '$\x0b508}\rohh>II&Kch>'
        dict_0 = {str_2: callable_0}
        undefined_parameter_error_0 = module_0.UndefinedParameterError(var_0, tuple_0, **dict_0)
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_1.handle_dump(undefined_parameter_error_0)
    except BaseException:
        pass