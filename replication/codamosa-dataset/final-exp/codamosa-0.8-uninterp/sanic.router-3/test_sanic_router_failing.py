# Automatically generated by Pynguin.
import sanic.router as module_0

def test_case_0():
    try:
        str_0 = '\\;3rhU'
        str_1 = 'ud\nA74utY'
        bool_0 = True
        router_0 = module_0.Router(str_0, str_1, bool_0)
        var_0 = router_0.finalize()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        str_0 = '.^G*@m[eb4rL'
        iterable_0 = None
        str_1 = 'JGiVgH>stc",1|s4pY'
        int_0 = 488
        router_0 = module_0.Router(int_0)
        var_0 = router_0.add(str_0, iterable_0, str_1, bool_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        router_0 = module_0.Router()
        var_0 = router_0.routes_all
        var_1 = len(var_0)
        var_2 = router_0.routes_static
        var_3 = len(var_1)
    except BaseException:
        pass