# Automatically generated by Pynguin.
import sanic.router as module_0

def test_case_0():
    pass

def test_case_1():
    router_0 = module_0.Router()
    str_0 = 'ikb'
    route_0 = None
    var_0 = router_0.add(str_0, route_0, route_0, str_0)

def test_case_2():
    str_0 = '.h)*7W6"yXJSke&'
    iterable_0 = None
    float_0 = 238.66521
    bool_0 = False
    bool_1 = True
    str_1 = ' 7!l<:'
    int_0 = -807
    router_0 = module_0.Router(str_1, int_0, bool_0)
    var_0 = router_0.add(str_0, iterable_0, float_0, bool_0, bool_1, bool_0)

def test_case_3():
    router_0 = module_0.Router()
    str_0 = '^E(Y\n\x0cSu<C!?+=\x0c4LNgT'
    bool_0 = False
    route_0 = None
    var_0 = router_0.add(str_0, bool_0, route_0, str_0, bool_0, bool_0, bool_0, bool_0)
    var_1 = router_0.finalize()

def test_case_4():
    router_0 = module_0.Router()
    str_0 = 'ikb'
    route_0 = None
    var_0 = router_0.add(str_0, route_0, route_0, str_0)
    var_1 = router_0.finalize()

def test_case_5():
    router_0 = module_0.Router()
    var_0 = router_0.routes_all
    var_1 = len(var_0)
    var_2 = router_0.routes_dynamic
    var_3 = len(var_2)
    var_4 = router_0.routes_regex
    var_5 = len(var_4)