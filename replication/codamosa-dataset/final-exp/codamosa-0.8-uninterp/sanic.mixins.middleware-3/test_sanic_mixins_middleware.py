# Automatically generated by Pynguin.
import sanic.mixins.middleware as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    middleware_mixin_0 = module_0.MiddlewareMixin(*list_0)

def test_case_2():
    middleware_mixin_0 = module_0.MiddlewareMixin()
    str_0 = ')%'
    var_0 = middleware_mixin_0.middleware(str_0, str_0)

def test_case_3():
    middleware_mixin_0 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_0.on_request()

def test_case_4():
    middleware_mixin_0 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_0.on_response()