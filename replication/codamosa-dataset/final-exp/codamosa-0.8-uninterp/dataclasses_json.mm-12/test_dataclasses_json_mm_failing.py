# Automatically generated by Pynguin.
import dataclasses_json.mm as module_0

def test_case_0():
    try:
        schema_f_0 = module_0.SchemaF()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        str_0 = ''
        str_1 = ' and was defaulted to None by infer_missing=True. Set infer_missing=False (the default) to prevent this behavior.'
        dict_1 = {dict_0: str_0, str_0: dict_0, str_1: str_1, dict_0: str_1}
        var_0 = module_0.schema(dict_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_2():
    try:
        type_0 = None
        bytes_0 = b'BV\x97G\xae\x9e\xcc'
        var_0 = None
        int_0 = None
        type_1 = module_0.build_schema(type_0, bytes_0, var_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        list_1 = [list_0]
        dict_0 = None
        var_0 = module_0.build_type(dict_0, list_0, list_1, dict_0, list_0)
    except BaseException:
        pass