# Automatically generated by Pynguin.
import httpie.client as module_0
import argparse as module_1
import httpie.cli.dicts as module_2
import pathlib as module_3

def test_case_0():
    try:
        request_headers_dict_0 = None
        request_headers_dict_1 = module_0.finalize_headers(request_headers_dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        namespace_0 = module_1.Namespace()
        request_headers_dict_0 = module_0.make_default_headers(namespace_0)
    except BaseException:
        pass

def test_case_2():
    try:
        namespace_0 = module_1.Namespace()
        dict_0 = module_0.make_send_kwargs(namespace_0)
    except BaseException:
        pass

def test_case_3():
    try:
        namespace_0 = module_1.Namespace()
        dict_0 = module_0.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        session_0 = module_0.build_requests_session(bool_0)
        namespace_0 = module_1.Namespace()
        dict_0 = module_0.make_request_kwargs(namespace_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        str_0 = "kM;G'u\x0ci>"
        session_0 = module_0.build_requests_session(bool_0, str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "*qba'c{?S+L&S^JkXXf:"
        dict_0 = None
        var_0 = module_0.dump_request(dict_0)
        str_1 = '}'
        dict_1 = {str_0: str_0, str_1: str_0, str_0: str_1, str_1: str_1, str_0: str_0, str_0: var_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_1)
        request_headers_dict_1 = module_0.finalize_headers(request_headers_dict_0)
        request_headers_dict_2 = module_2.RequestHeadersDict()
        bool_0 = True
        session_0 = module_0.build_requests_session(bool_0)
        namespace_0 = module_1.Namespace(**dict_1)
        dict_2 = module_0.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        session_0 = module_0.build_requests_session(bool_0)
        namespace_0 = module_1.Namespace()
        path_0 = module_3.Path()
        iterable_0 = module_0.collect_messages(namespace_0, path_0)
        request_headers_dict_0 = module_2.RequestHeadersDict(iterable_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'data'
        int_0 = 3182
        dict_0 = {str_0: int_0, str_0: str_0}
        namespace_0 = module_1.Namespace(**dict_0)
        request_headers_dict_0 = module_0.make_default_headers(namespace_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'timeout'
        var_0 = None
        dict_0 = {str_0: str_0, str_0: str_0, str_0: var_0, str_0: var_0}
        namespace_0 = module_1.Namespace(**dict_0)
        namespace_1 = module_1.Namespace(**dict_0)
        bool_0 = False
        session_0 = module_0.build_requests_session(bool_0)
        dict_1 = module_0.make_send_kwargs(namespace_1)
        dict_2 = module_0.make_send_kwargs_mergeable_from_env(namespace_1)
    except BaseException:
        pass