# Automatically generated by Pynguin.
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests_toolbelt.multipart.encoder as module_2

def test_case_0():
    pass

def test_case_1():
    iterable_0 = None
    request_data_dict_0 = None
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(iterable_0, request_data_dict_0)

def test_case_2():
    request_data_dict_0 = module_1.RequestDataDict()
    multipart_encoder_0 = module_2.MultipartEncoder(request_data_dict_0)
    set_0 = None
    list_0 = [set_0]
    var_0 = module_0.prepare_request_body(multipart_encoder_0, request_data_dict_0, set_0, list_0)

def test_case_3():
    bytes_0 = b''
    str_0 = '1Y2jQy)@'
    int_0 = 1992
    list_0 = None
    var_0 = module_0.prepare_request_body(bytes_0, str_0, int_0, list_0)

def test_case_4():
    request_data_dict_0 = module_1.RequestDataDict()
    multipart_encoder_0 = module_2.MultipartEncoder(request_data_dict_0)
    str_0 = 'rb'
    tuple_0 = (multipart_encoder_0, str_0)
    var_0 = module_0.prepare_request_body(multipart_encoder_0, tuple_0)

def test_case_5():
    str_0 = 'auto'
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_6():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0)

def test_case_7():
    multipart_encoder_0 = None
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0)
    tuple_1 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0)
    int_0 = 1992
    callable_0 = None
    str_0 = None
    float_0 = 0.1
    var_0 = module_0.prepare_request_body(str_0, callable_0, int_0, float_0)