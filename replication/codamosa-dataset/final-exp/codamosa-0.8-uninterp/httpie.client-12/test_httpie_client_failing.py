# Automatically generated by Pynguin.
import argparse as module_0
import httpie.client as module_1
import httpie.cli.dicts as module_2
import pathlib as module_3

def test_case_0():
    try:
        namespace_0 = module_0.Namespace()
        request_headers_dict_0 = module_1.make_default_headers(namespace_0)
    except BaseException:
        pass

def test_case_1():
    try:
        namespace_0 = module_0.Namespace()
        dict_0 = module_1.make_send_kwargs(namespace_0)
    except BaseException:
        pass

def test_case_2():
    try:
        namespace_0 = module_0.Namespace()
        dict_0 = module_1.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass

def test_case_3():
    try:
        namespace_0 = module_0.Namespace()
        dict_0 = module_1.make_request_kwargs(namespace_0, namespace_0)
    except BaseException:
        pass

def test_case_4():
    try:
        request_headers_dict_0 = module_2.RequestHeadersDict()
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        bool_0 = True
        str_0 = 'action'
        session_0 = module_1.build_requests_session(bool_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        request_headers_dict_0 = module_2.RequestHeadersDict()
        namespace_0 = module_0.Namespace()
        str_0 = 'J.6RK;'
        list_0 = [request_headers_dict_0]
        dict_0 = {str_0: list_0}
        path_0 = module_3.Path(**dict_0)
        callable_0 = None
        iterable_0 = module_1.collect_messages(namespace_0, path_0, callable_0)
        request_headers_dict_1 = module_2.RequestHeadersDict(iterable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = -3208.0
        var_0 = module_1.max_headers(float_0)
        str_0 = 'm_\n\typ&)'
        bool_0 = True
        session_0 = module_1.build_requests_session(bool_0)
        dict_0 = {str_0: bool_0, str_0: var_0, str_0: str_0, str_0: var_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'mP\n\typ&)'
        str_1 = module_1.ensure_path_as_is(str_0, str_0)
        bool_0 = False
        request_headers_dict_0 = module_2.RequestHeadersDict()
        session_0 = module_1.build_requests_session(bool_0)
        var_0 = module_1.max_headers(request_headers_dict_0)
        dict_0 = {str_0: bool_0, str_0: str_1, str_0: str_0, str_0: str_1}
        request_headers_dict_1 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_2 = module_1.finalize_headers(request_headers_dict_1)
        request_headers_dict_3 = module_1.finalize_headers(request_headers_dict_1)
        namespace_0 = module_0.Namespace(**dict_0)
        dict_1 = module_1.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '88\\&5J Bp'
        str_1 = 'cert'
        bytes_0 = b'\xd8\x98\x9b\xb4\xd6\\@\xe2,'
        dict_0 = {str_0: str_0, str_1: bytes_0, str_0: str_0, str_0: str_0, str_1: bytes_0}
        namespace_0 = module_0.Namespace(**dict_0)
        dict_1 = module_1.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass