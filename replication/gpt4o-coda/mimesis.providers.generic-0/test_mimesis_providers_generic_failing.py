# Automatically generated by Pynguin.
import mimesis.providers.generic as module_0

def test_case_0():
    try:
        generic_0 = module_0.Generic()
        list_0 = generic_0.__dir__()
        dict_0 = None
        list_1 = [dict_0]
        generic_0.add_providers(*list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        generic_0 = module_0.Generic()
        generic_0.add_provider(generic_0)
    except BaseException:
        pass