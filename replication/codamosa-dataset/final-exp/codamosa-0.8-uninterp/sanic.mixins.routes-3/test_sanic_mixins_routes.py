# Automatically generated by Pynguin.
import sanic.mixins.routes as module_0
import pathlib as module_1

def test_case_0():
    pass

def test_case_1():
    route_mixin_0 = module_0.RouteMixin()

def test_case_2():
    str_0 = 'domain'
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.websocket(str_0)

def test_case_3():
    str_0 = 'module'
    bytes_0 = b'P\xddg\xbeg\xcf\xc6\x97\x81\x8e\xd0\x87\x1b\xa1#^\xe0\xbe\xbf'
    bool_0 = True
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.get(str_0, bool_0)
    set_0 = {str_0}
    optional_0 = None
    list_0 = []
    str_1 = ':rU'
    str_2 = 'QmrROA=XjRFPySy|\n'
    dict_0 = {str_1: str_1, str_2: str_1}
    route_mixin_1 = module_0.RouteMixin(*list_0, **dict_0)
    var_1 = route_mixin_1.route(str_0, bytes_0, set_0, optional_0)

def test_case_4():
    str_0 = ''
    set_0 = {str_0, str_0}
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.put(str_0, str_0, set_0, str_0)

def test_case_5():
    str_0 = ''
    pure_path_0 = module_1.PurePath()
    float_0 = 1992.109398
    var_0 = pure_path_0.__ge__(float_0)
    route_mixin_0 = module_0.RouteMixin()
    var_1 = route_mixin_0.patch(str_0, pure_path_0)

def test_case_6():
    str_0 = '/t,q&}w; _/~'
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.delete(str_0)
    route_mixin_1 = module_0.RouteMixin()