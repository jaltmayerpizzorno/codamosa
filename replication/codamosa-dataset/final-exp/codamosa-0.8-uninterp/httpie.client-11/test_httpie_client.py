# Automatically generated by Pynguin.
import httpie.client as module_0
import httpie.cli.dicts as module_1
import argparse as module_2

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    session_0 = module_0.build_requests_session(bool_0)

def test_case_2():
    request_headers_dict_0 = module_1.RequestHeadersDict()
    request_headers_dict_1 = module_0.finalize_headers(request_headers_dict_0)

def test_case_3():
    int_0 = 1228
    str_0 = 'timeout'
    dict_0 = {str_0: int_0, str_0: str_0}
    namespace_0 = module_2.Namespace(**dict_0)
    dict_1 = module_0.make_send_kwargs(namespace_0)

def test_case_4():
    str_0 = 'type'
    str_1 = module_0.ensure_path_as_is(str_0, str_0)

def test_case_5():
    dict_0 = None
    var_0 = module_0.dump_request(dict_0)
    str_0 = '~!'
    dict_1 = {str_0: var_0, str_0: dict_0}
    bool_0 = False
    session_0 = module_0.build_requests_session(bool_0)
    request_headers_dict_0 = module_1.RequestHeadersDict(**dict_1)
    request_headers_dict_1 = module_0.finalize_headers(request_headers_dict_0)
    request_headers_dict_2 = module_0.finalize_headers(request_headers_dict_0)

def test_case_6():
    bool_0 = None
    session_0 = module_0.build_requests_session(bool_0)
    str_0 = 'group_name'
    int_0 = 1228
    str_1 = 'timeout'
    dict_0 = {str_1: str_0, str_0: int_0, str_1: bool_0, str_0: bool_0}
    namespace_0 = module_2.Namespace(**dict_0)
    namespace_1 = module_2.Namespace(**dict_0)
    dict_1 = module_0.make_send_kwargs(namespace_1)