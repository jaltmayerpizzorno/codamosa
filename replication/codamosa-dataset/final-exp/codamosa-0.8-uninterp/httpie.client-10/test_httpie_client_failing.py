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
        str_0 = 'VCE'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        str_1 = 'NVM{aS2Gd1:3H#?Em\\'
        request_headers_dict_2 = module_2.RequestHeadersDict()
        str_2 = 't'
        str_3 = module_1.ensure_path_as_is(str_1, str_2)
        namespace_0 = None
        dict_1 = module_1.make_send_kwargs(namespace_0)
    except BaseException:
        pass

def test_case_2():
    try:
        namespace_0 = None
        dict_0 = module_1.make_send_kwargs_mergeable_from_env(namespace_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '#h\\\nB\x0b0^\x0c:O&]Yn'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        namespace_0 = module_0.Namespace()
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        dict_1 = module_1.make_request_kwargs(namespace_0, request_headers_dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'A^S\t"S2\rP'
        bool_0 = False
        session_0 = module_1.build_requests_session(bool_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        str_0 = 'l\tX9|s\\CK6|EmxfabH#'
        session_0 = module_1.build_requests_session(bool_0)
        str_1 = 'B'
        str_2 = '--follow'
        str_3 = 'VCE'
        dict_0 = {str_1: str_0, str_2: str_1, str_2: str_2, str_3: str_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        request_headers_dict_2 = module_2.RequestHeadersDict()
        str_4 = 't'
        str_5 = module_1.ensure_path_as_is(str_0, str_4)
        str_6 = 'Vp$0'
        str_7 = module_1.ensure_path_as_is(str_2, str_6)
        namespace_0 = module_0.Namespace()
        list_0 = [str_7]
        path_0 = module_3.Path(*list_0)
        iterable_0 = module_1.collect_messages(namespace_0, path_0)
        str_8 = 'Nl74reIj&{+P=C'
        dict_1 = {str_8: str_6}
        request_headers_dict_3 = module_2.RequestHeadersDict(iterable_0, **dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        namespace_0 = None
        str_0 = 'W#_4b@'
        str_1 = '@^*'
        str_2 = '$u9^1NnTRp)-'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: namespace_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        request_headers_dict_2 = module_1.finalize_headers(request_headers_dict_1)
        dict_1 = module_1.make_request_kwargs(namespace_0)
    except BaseException:
        pass