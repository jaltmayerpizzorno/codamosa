# Automatically generated by Pynguin.
import httpie.cli.dicts as module_0
import requests_toolbelt.multipart.encoder as module_1
import httpie.uploads as module_2
import requests.models as module_3
import typing as module_4

def test_case_0():
    try:
        request_data_dict_0 = module_0.RequestDataDict()
        multipart_encoder_0 = module_1.MultipartEncoder(request_data_dict_0)
        chunked_multipart_upload_stream_0 = module_2.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        multipart_encoder_1 = module_1.MultipartEncoder(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        prepared_request_0 = module_3.PreparedRequest()
        i_o_0 = module_4.IO()
        var_0 = module_2.prepare_request_body(i_o_0, i_o_0, i_o_0)
    except BaseException:
        pass

def test_case_2():
    try:
        prepared_request_0 = module_3.PreparedRequest()
        bool_0 = False
        var_0 = module_2.compress_request(prepared_request_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'gJ77[PGhtI'
        dict_0 = None
        bool_0 = False
        float_0 = -1458.0
        var_0 = module_2.prepare_request_body(str_0, dict_0, bool_0, float_0)
        str_1 = 'Like `write`, but colorized chunks are written as text\n    directly to `outfile` to ensure it gets processed by colorama.\n    Applies only to Windows with Python 3 and colorized terminal output.\n\n    '
        dict_1 = {str_1: str_1}
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict(**dict_1)
        tuple_0 = module_2.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_1, str_1)
        str_2 = 'headers'
        var_1 = module_2.prepare_request_body(str_1, str_2)
        prepared_request_0 = module_3.PreparedRequest()
        bool_1 = True
        var_2 = module_2.compress_request(prepared_request_0, bool_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Like `write`, but colorized chunks are written as text\n    directly to `outfile` to ensure it gets processed by colorama.\n    Applies only to Windows with Python 3 and colorized terminal output.\n\n    '
        dict_0 = {str_0: str_0}
        list_0 = []
        list_1 = [str_0]
        multipart_encoder_0 = module_1.MultipartEncoder(list_0, list_1)
        str_1 = '{0}:{1:0>2}:{2:0>2}'
        var_0 = module_2.prepare_request_body(multipart_encoder_0, str_1, dict_0)
        var_1 = multipart_encoder_0.to_string()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Like `write`, but colorized chunks are written as text\n    directly to `outfile` to ensure it gets processed by colorama.\n    Applies only to Windows with Python 3 and colorized terminal output.\n\n    '
        dict_0 = {str_0: str_0}
        list_0 = []
        list_1 = [str_0]
        multipart_encoder_0 = module_1.MultipartEncoder(list_0, list_1)
        str_1 = '{0}:{1:0>2}:{2:0>2}'
        var_0 = module_2.prepare_request_body(multipart_encoder_0, str_1, dict_0)
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict(**dict_0)
        chunked_multipart_upload_stream_0 = module_2.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        str_2 = None
        tuple_0 = module_2.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_2, str_0)
        str_3 = ';'
        var_1 = module_2.prepare_request_body(str_0, str_3)
        callable_0 = None
        str_4 = ' NNOGAI?.V\t.i\\:bC'
        tuple_1 = module_2.get_multipart_data_and_content_type(multipart_request_data_dict_0)
        prepared_request_0 = module_3.PreparedRequest()
        int_0 = -2553
        multipart_encoder_1 = None
        var_2 = module_2.prepare_request_body(str_4, callable_0, int_0, multipart_encoder_1, prepared_request_0)
        i_o_0 = module_4.IO()
        var_3 = i_o_0.read()
        list_2 = [var_3, var_3, var_3]
        var_4 = module_2.prepare_request_body(str_0, callable_0, list_2)
        chunked_multipart_upload_stream_1 = module_2.ChunkedMultipartUploadStream(multipart_encoder_1)
        iterable_1 = chunked_multipart_upload_stream_1.__iter__()
        prepared_request_1 = module_3.PreparedRequest()
        chunked_multipart_upload_stream_2 = module_2.ChunkedMultipartUploadStream(multipart_encoder_1)
        iterable_2 = chunked_multipart_upload_stream_2.__iter__()
        chunked_multipart_upload_stream_3 = module_2.ChunkedMultipartUploadStream(multipart_encoder_0)
        int_1 = 20
        callable_1 = None
        chunked_upload_stream_0 = module_2.ChunkedUploadStream(multipart_encoder_1, callable_1)
        var_5 = module_2.prepare_request_body(multipart_encoder_0, callable_0, int_1, iterable_1, chunked_upload_stream_0)
    except BaseException:
        pass