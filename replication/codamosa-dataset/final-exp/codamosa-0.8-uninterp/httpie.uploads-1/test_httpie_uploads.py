# Automatically generated by Pynguin.
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

def test_case_0():
    pass

def test_case_1():
    iterable_0 = None
    var_0 = None
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(iterable_0, var_0)

def test_case_2():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    float_0 = -1427.3859446401852
    callable_0 = None
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(float_0, callable_0)
    multipart_encoder_0 = module_2.MultipartEncoder(multipart_request_data_dict_0)
    i_o_0 = module_3.IO()
    var_0 = i_o_0.readline()
    bool_0 = True
    var_1 = module_0.prepare_request_body(multipart_encoder_0, i_o_0, var_0, bool_0)

def test_case_3():
    request_data_dict_0 = module_1.RequestDataDict()
    bytes_0 = b'\xd3s\x11d\xf3\xae\xff0\x91'
    var_0 = module_0.prepare_request_body(request_data_dict_0, bytes_0)

def test_case_4():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0)

def test_case_5():
    str_0 = 'body'
    bool_0 = True
    var_0 = module_0.prepare_request_body(str_0, str_0, bool_0)

def test_case_6():
    var_0 = lambda x: x
    str_0 = 'aaa'
    str_1 = 'bbb'
    str_2 = 'ccc'
    str_3 = [str_0, str_1, str_2]
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(str_3, var_0)
    var_1 = [x for x in chunked_upload_stream_0]

def test_case_7():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    str_0 = '\n    The same as --print, -p but applies only to intermediary requests/responses\n    (such as redirects) when their inclusion is enabled with --all. If this\n    options is not specified, then they are formatted the same way as the final\n    response.\n\n    '
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_8():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    i_o_0 = module_3.IO()
    var_0 = i_o_0.__enter__()
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(var_0, i_o_0)
    iterable_0 = chunked_upload_stream_0.__iter__()
    multipart_encoder_0 = module_2.MultipartEncoder(multipart_request_data_dict_0, iterable_0)
    var_1 = module_0.prepare_request_body(multipart_encoder_0, chunked_upload_stream_0, i_o_0)

def test_case_9():
    str_0 = '(EafO'
    dict_0 = {str_0: str_0}
    multipart_encoder_0 = module_2.MultipartEncoder(dict_0)
    chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
    int_0 = -2807
    prepared_request_0 = module_4.PreparedRequest()
    request_data_dict_0 = module_1.RequestDataDict()
    var_0 = prepared_request_0.prepare_headers(request_data_dict_0)
    var_1 = module_0.prepare_request_body(str_0, multipart_encoder_0)
    var_2 = module_0.prepare_request_body(request_data_dict_0, chunked_multipart_upload_stream_0, int_0, str_0, dict_0)
    prepared_request_1 = module_4.PreparedRequest()
    prepared_request_2 = module_4.PreparedRequest()