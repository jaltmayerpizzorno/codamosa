# Automatically generated by Pynguin.
import argparse as module_0
import httpie.client as module_1
import httpie.cli.dicts as module_2
import pathlib as module_3

def test_case_0():
    try:
        namespace_0 = module_0.Namespace()
        list_0 = [namespace_0, namespace_0, namespace_0]
        bytes_0 = b'?v\xc7\x8d'
        dict_0 = None
        var_0 = module_1.dump_request(dict_0)
        var_1 = namespace_0.__contains__(bytes_0)
        var_2 = namespace_0.__contains__(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        request_headers_dict_0 = module_2.RequestHeadersDict()
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        bool_0 = True
        var_0 = module_1.max_headers(bool_0)
        namespace_0 = module_0.Namespace()
        path_0 = module_3.Path()
        iterable_0 = module_1.collect_messages(namespace_0, path_0)
        dict_0 = {}
        namespace_1 = module_0.Namespace(**dict_0)
        list_0 = []
        session_0 = module_1.build_requests_session(bool_0, list_0)
        var_1 = namespace_1.__eq__(session_0)
        request_headers_dict_2 = module_1.make_default_headers(namespace_1)
    except BaseException:
        pass

def test_case_2():
    try:
        namespace_0 = None
        dict_0 = module_1.make_send_kwargs(namespace_0)
    except BaseException:
        pass

def test_case_3():
    try:
        namespace_0 = None
        dict_0 = module_1.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'no'
        namespace_0 = module_0.Namespace()
        str_1 = '\\nW^'
        str_2 = ']Dw)&EBMycZ3qp@'
        dict_0 = {str_1: namespace_0, str_0: str_1, str_2: namespace_0, str_2: namespace_0}
        path_0 = module_3.Path(**dict_0)
        iterable_0 = module_1.collect_messages(namespace_0, path_0)
        dict_1 = module_1.make_request_kwargs(namespace_0, iterable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        bytes_0 = b's<\xa0iXwD\x86'
        none_type_0 = None
        session_0 = module_1.build_requests_session(bool_0, bytes_0, none_type_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ':=@'
        dict_0 = {str_0: str_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        request_headers_dict_2 = module_1.finalize_headers(request_headers_dict_1)
        str_1 = 'q7+SWbVqc~kk&6G~WX}L'
        str_2 = '48g~\'"w)!'
        dict_1 = {str_2: str_2, str_2: str_2, str_1: str_1, str_1: str_2}
        request_headers_dict_3 = module_2.RequestHeadersDict()
        request_headers_dict_4 = module_1.finalize_headers(request_headers_dict_3)
        namespace_0 = module_0.Namespace(**dict_1)
        request_headers_dict_5 = module_1.make_default_headers(namespace_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ':=@'
        dict_0 = {str_0: str_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        request_headers_dict_2 = module_1.finalize_headers(request_headers_dict_1)
        request_headers_dict_3 = module_1.finalize_headers(request_headers_dict_2)
        bool_0 = False
        session_0 = module_1.build_requests_session(bool_0)
        bool_1 = False
        var_0 = module_1.max_headers(bool_1)
        dict_1 = {}
        namespace_0 = module_0.Namespace(**dict_1)
        list_0 = []
        path_0 = module_3.Path(*list_0)
        iterable_0 = module_1.collect_messages(namespace_0, path_0)
        request_headers_dict_4 = module_2.RequestHeadersDict(iterable_0)
    except BaseException:
        pass

def test_case_8():
    try:
        namespace_0 = module_0.Namespace()
        bool_0 = None
        str_0 = 'G;|lQZ{4&60<0Xg#!nm9'
        str_1 = '(2>r>"!E17'
        str_2 = module_1.ensure_path_as_is(str_0, str_1)
        dict_0 = {str_2: bool_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        complex_0 = None
        set_0 = {str_0, complex_0, str_0}
        var_0 = module_1.max_headers(set_0)
        session_0 = module_1.build_requests_session(bool_0)
        var_1 = namespace_0.__eq__(session_0)
        var_2 = namespace_0.__eq__(session_0)
        request_headers_dict_2 = module_1.make_default_headers(namespace_0)
    except BaseException:
        pass