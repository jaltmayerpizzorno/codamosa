# Automatically generated by Pynguin.
import sanic.mixins.middleware as module_0

def test_case_0():
    pass

def test_case_1():
    middleware_mixin_0 = module_0.MiddlewareMixin()

def test_case_2():
    bytes_0 = b'?\xc1\xd2\xf0D3\x80\x13\x18C\x85-\xd9\xb4o@\xf4('
    middleware_mixin_0 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_0.middleware(bytes_0)

def test_case_3():
    middleware_mixin_0 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_0.on_request()

def test_case_4():
    middleware_mixin_0 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_0.on_response()