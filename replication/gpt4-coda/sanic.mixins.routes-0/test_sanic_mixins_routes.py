# Automatically generated by Pynguin.
import sanic.mixins.routes as module_0

def test_case_0():
    pass

def test_case_1():
    route_mixin_0 = module_0.RouteMixin()

def test_case_2():
    str_0 = '\n        Decorate a function to be registered as a websocket route\n\n        :param uri: path of the URL\n        :param host: Host IP or FQDN details\n        :param strict_slashes: If the API endpoint needs to terminate\n                               with a "/" or not\n        :param subprotocols: optional list of str with supported subprotocols\n        :param name: A unique name assigned to the URL so that it can\n                     be used with :func:`url_for`\n        :return: tuple of routes, decorated function\n        '
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.post(str_0)

def test_case_3():
    str_0 = ''
    bool_0 = None
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.head(str_0, bool_0, str_0, bool_0)

def test_case_4():
    str_0 = '/P\x0c3DEiJ[b:^1'
    set_0 = set()
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.options(str_0, set_0)

def test_case_5():
    str_0 = '<LWI&S;Q;'
    bool_0 = True
    dict_0 = {}
    list_0 = [dict_0]
    str_1 = ''
    dict_1 = {str_1: dict_0}
    route_mixin_0 = module_0.RouteMixin(*list_0, **dict_1)
    var_0 = route_mixin_0.patch(str_0, bool_0)

def test_case_6():
    str_0 = 'n&+cSFXwt1rtlN\r($O'
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.delete(str_0)

def test_case_7():
    str_0 = '9HAtQ5j.6loD'
    bool_0 = False
    route_mixin_0 = module_0.RouteMixin()
    var_0 = route_mixin_0.websocket(str_0, str_0, bool_0)