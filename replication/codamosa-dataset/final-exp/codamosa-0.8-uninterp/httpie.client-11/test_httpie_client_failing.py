# Automatically generated by Pynguin.
import httpie.client as module_0
import argparse as module_1
import pathlib as module_2
import httpie.cli.dicts as module_3

def test_case_0():
    try:
        dict_0 = None
        var_0 = module_0.dump_request(dict_0)
        str_0 = '7D1q!\t\rKB(`SUX0m|>'
        str_1 = ';6_7d)MGG?t_\\L#oe/ g'
        str_2 = module_0.ensure_path_as_is(str_0, str_1)
        namespace_0 = module_1.Namespace()
        request_headers_dict_0 = module_0.make_default_headers(namespace_0)
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
        str_0 = ',}bE'
        dict_0 = {str_0: str_0}
        namespace_0 = module_1.Namespace(**dict_0)
        dict_1 = module_0.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass

def test_case_3():
    try:
        namespace_0 = module_1.Namespace()
        str_0 = 'rj;/bn\x0b?'
        str_1 = module_0.ensure_path_as_is(str_0, str_0)
        bool_0 = False
        session_0 = module_0.build_requests_session(bool_0)
        dict_0 = module_0.make_request_kwargs(namespace_0, namespace_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        str_0 = 'aUd-\\\\1'
        session_0 = module_0.build_requests_session(bool_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        namespace_0 = module_1.Namespace()
        path_0 = module_2.Path()
        iterable_0 = module_0.collect_messages(namespace_0, path_0)
        request_headers_dict_0 = module_3.RequestHeadersDict(iterable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = None
        var_0 = module_0.dump_request(dict_0)
        namespace_0 = None
        str_0 = '\x0ca\x0c6*b'
        dict_1 = {str_0: str_0, str_0: str_0}
        request_headers_dict_0 = module_3.RequestHeadersDict(namespace_0, **dict_1)
        request_headers_dict_1 = module_0.finalize_headers(request_headers_dict_0)
        request_headers_dict_2 = module_0.finalize_headers(request_headers_dict_1)
        request_headers_dict_3 = module_0.finalize_headers(request_headers_dict_0)
        str_1 = '\n    Ignore credentials from .netrc.\n\n    '
        str_2 = module_0.ensure_path_as_is(str_1, str_1)
        namespace_1 = module_1.Namespace(**dict_1)
        request_headers_dict_4 = module_0.make_default_headers(namespace_1)
    except BaseException:
        pass