# Automatically generated by Pynguin.
import sanic.mixins.middleware as module_0
import functools as module_1

def test_case_0():
    try:
        middleware_mixin_0 = module_0.MiddlewareMixin()
        var_0 = lambda request, response: (request, response)
        var_1 = middleware_mixin_0.on_response(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '9lINEow'
        dict_0 = {str_0: str_0}
        middleware_mixin_0 = module_0.MiddlewareMixin(**dict_0)
        middleware_mixin_1 = module_0.MiddlewareMixin()
        var_0 = lambda request, response: (request, response)
        list_0 = [var_0]
        partial_0 = module_1.partial(*list_0, **dict_0)
        var_1 = middleware_mixin_0.on_request(partial_0)
    except BaseException:
        pass