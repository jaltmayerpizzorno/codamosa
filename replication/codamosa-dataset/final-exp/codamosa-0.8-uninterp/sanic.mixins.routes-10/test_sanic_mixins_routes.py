# Automatically generated by Pynguin.
import sanic.mixins.routes as module_0
import pathlib as module_1

def test_case_0():
    pass

def test_case_1():
    route_mixin_0 = module_0.RouteMixin()

def test_case_2():
    str_0 = ''
    route_mixin_0 = module_0.RouteMixin()
    list_0 = [route_mixin_0, route_mixin_0]
    route_mixin_1 = module_0.RouteMixin(*list_0)
    var_0 = route_mixin_1.get(str_0)

def test_case_3():
    str_0 = 't)=\x0b'
    route_mixin_0 = module_0.RouteMixin()
    list_0 = [route_mixin_0, route_mixin_0, route_mixin_0, route_mixin_0]
    route_mixin_1 = module_0.RouteMixin(*list_0)
    var_0 = route_mixin_1.put(str_0)

def test_case_4():
    str_0 = '/-'
    dict_0 = {}
    route_mixin_0 = module_0.RouteMixin(**dict_0)
    var_0 = route_mixin_0.head(str_0)
    str_1 = '\x0c'
    bool_0 = None
    route_mixin_1 = module_0.RouteMixin()
    var_1 = route_mixin_1.websocket(str_1, bool_0)

def test_case_5():
    str_0 = 'f7=h2Hu|diT|W*-x6f'
    list_0 = [str_0]
    pure_path_0 = module_1.PurePath(*list_0)
    int_0 = -2680
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.patch(str_0, pure_path_0, int_0)