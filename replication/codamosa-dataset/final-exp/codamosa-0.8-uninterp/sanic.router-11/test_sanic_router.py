# Automatically generated by Pynguin.
import sanic.router as module_0

def test_case_0():
    pass

def test_case_1():
    router_0 = module_0.Router()
    str_0 = ''
    var_0 = router_0.add(str_0, str_0, str_0, str_0)

def test_case_2():
    router_0 = module_0.Router()
    str_0 = '/<__file_uri__>'
    bool_0 = False
    var_0 = router_0.add(str_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0)

def test_case_3():
    router_0 = module_0.Router()
    bool_0 = False
    str_0 = "]'Rd;@i'm("
    iterable_0 = None
    list_0 = []
    var_0 = router_0.add(str_0, iterable_0, list_0, str_0, bool_0, str_0)

def test_case_4():
    router_0 = module_0.Router()
    str_0 = '/<__file_uri__>'
    bool_0 = False
    var_0 = router_0.add(str_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0)
    var_1 = router_0.finalize()

def test_case_5():
    router_0 = module_0.Router()
    str_0 = '/<D1fxile_uri__>'
    var_0 = None
    bool_0 = False
    var_1 = router_0.add(str_0, var_0, var_0, bool_0, bool_0, bool_0, var_0, var_0, bool_0)
    var_2 = router_0.finalize()

def test_case_6():
    router_0 = module_0.Router()
    var_0 = router_0.routes_dynamic
    var_1 = len(var_0)
    var_2 = router_0.routes_static
    var_3 = len(var_2)
    var_4 = router_0.routes_regex
    var_5 = len(var_4)
    var_6 = router_0.routes_all
    var_7 = len(var_6)