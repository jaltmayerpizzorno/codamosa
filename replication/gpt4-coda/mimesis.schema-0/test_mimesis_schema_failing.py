# Automatically generated by Pynguin.
import mimesis.schema as module_0

def test_case_0():
    try:
        str_0 = ',NQ'
        abstract_field_0 = module_0.AbstractField()
        any_0 = abstract_field_0.__call__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        abstract_field_0 = module_0.AbstractField()
        any_0 = abstract_field_0.__call__()
    except BaseException:
        pass

def test_case_2():
    try:
        abstract_field_0 = module_0.AbstractField()
        any_0 = abstract_field_0.__call__(abstract_field_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callable_0 = None
        schema_0 = module_0.Schema(callable_0)
    except BaseException:
        pass

def test_case_4():
    try:
        abstract_field_0 = module_0.AbstractField()
        schema_0 = module_0.Schema(abstract_field_0)
        list_0 = schema_0.create()
    except BaseException:
        pass

def test_case_5():
    try:
        abstract_field_0 = module_0.AbstractField()
        str_0 = '"G"8;XFb.\rx%E^j\x0c14{$'
        any_0 = abstract_field_0.__call__(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '"3G";XFb.x%E^j\x0c14{$'
        str_1 = None
        str_2 = '[AYj9'
        dict_0 = {str_2: str_0, str_2: str_2, str_0: str_2}
        abstract_field_0 = module_0.AbstractField(str_1, str_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '"G;X..$c^"\x0c14$'
        abstract_field_0 = module_0.AbstractField()
        any_0 = abstract_field_0.__call__(str_0)
    except BaseException:
        pass