# Automatically generated by Pynguin.
import dataclasses_json.undefined as module_0

def test_case_0():
    try:
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        float_0 = 1834.38248
        dict_0 = {ignore_undefined_parameters_0: ignore_undefined_parameters_0, ignore_undefined_parameters_0: ignore_undefined_parameters_0, ignore_undefined_parameters_0: ignore_undefined_parameters_0, float_0: float_0}
        callable_0 = ignore_undefined_parameters_0.create_init(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        undefined_0 = module_0.Undefined.INCLUDE
        dict_0 = None
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_1 = catch_all_undefined_parameters_0.handle_to_dict(undefined_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "s'FlWXffj}\x0b"
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        dict_0 = {}
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters()
        catch_all_undefined_parameters_2 = module_0._CatchAllUndefinedParameters(**dict_0)
        dict_1 = catch_all_undefined_parameters_2.handle_dump(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        str_0 = 'B?:i2k$=4S'
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        float_0 = 1687.1
        tuple_0 = (float_0,)
        callable_0 = catch_all_undefined_parameters_0.create_init(tuple_0)
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters(*list_0)
        callable_1 = ignore_undefined_parameters_0.create_init(catch_all_undefined_parameters_0)
        dict_0 = {str_0: str_0}
        catch_all_undefined_parameters_1 = module_0._CatchAllUndefinedParameters(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'g\xb5\x06\xaal\xb1W71s\x14m\x91'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        list_0 = None
        callable_0 = catch_all_undefined_parameters_0.create_init(list_0)
        list_1 = []
        dict_1 = {}
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters(**dict_1)
        callable_1 = ignore_undefined_parameters_0.create_init(list_1)
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        ignore_undefined_parameters_1 = module_0._IgnoreUndefinedParameters()
        dict_2 = ignore_undefined_parameters_1.handle_from_dict(raise_undefined_parameters_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
        int_0 = 637
        callable_0 = ignore_undefined_parameters_0.create_init(int_0)
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        callable_1 = ignore_undefined_parameters_0.create_init(raise_undefined_parameters_0)
        dict_0 = {}
        dict_1 = None
        dict_2 = raise_undefined_parameters_0.handle_from_dict(dict_0, dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'g\xb5\x06\xaal\xb1W71s\x14m\x91'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
        list_0 = None
        callable_0 = catch_all_undefined_parameters_0.create_init(list_0)
        list_1 = []
        dict_1 = {}
        ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters(**dict_1)
        callable_1 = ignore_undefined_parameters_0.create_init(list_1)
        raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
        ignore_undefined_parameters_1 = module_0._IgnoreUndefinedParameters()
        str_0 = ''
        dict_2 = catch_all_undefined_parameters_0.handle_from_dict(str_0, dict_0)
    except BaseException:
        pass