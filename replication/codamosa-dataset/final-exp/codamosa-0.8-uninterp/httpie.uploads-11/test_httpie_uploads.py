# Automatically generated by Pynguin.
import requests_toolbelt.multipart.encoder as module_0
import httpie.uploads as module_1
import typing as module_2
import httpie.cli.dicts as module_3
import requests.models as module_4

def test_case_0():
    pass

def test_case_1():
    str_0 = 'test'
    str_1 = 'case'
    str_2 = (str_0, str_1)
    str_3 = (str_2,)
    multipart_encoder_0 = module_0.MultipartEncoder(str_3)
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    var_0 = list(chunked_multipart_upload_stream_0)

def test_case_2():
    bytes_0 = b'e\x08\x9a\xba\xd8V\x82\x85\xc5\x0c,'
    i_o_0 = module_2.IO()
    var_0 = i_o_0.__enter__()
    list_0 = []
    dict_0 = None
    var_1 = module_1.prepare_request_body(bytes_0, var_0, list_0, dict_0)

def test_case_3():
    request_data_dict_0 = module_3.RequestDataDict()
    multipart_encoder_0 = module_0.MultipartEncoder(request_data_dict_0)
    prepared_request_0 = module_4.PreparedRequest()
    iterable_0 = None
    list_0 = [prepared_request_0, iterable_0, multipart_encoder_0]
    var_0 = module_1.prepare_request_body(multipart_encoder_0, prepared_request_0, list_0)

def test_case_4():
    request_data_dict_0 = module_3.RequestDataDict()
    callable_0 = None
    prepared_request_0 = module_4.PreparedRequest()
    float_0 = 3809.74
    chunked_upload_stream_0 = module_1.ChunkedUploadStream(float_0, callable_0)
    iterable_0 = chunked_upload_stream_0.__iter__()
    multipart_request_data_dict_0 = module_3.MultipartRequestDataDict()
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)
    var_0 = module_1.prepare_request_body(request_data_dict_0, chunked_upload_stream_0)

def test_case_5():
    multipart_request_data_dict_0 = module_3.MultipartRequestDataDict()
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)
    prepared_request_0 = module_4.PreparedRequest()

def test_case_6():
    str_0 = 'wuo/6$\n77LOSs'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    multipart_request_data_dict_0 = module_3.MultipartRequestDataDict(**dict_0)
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_7():
    str_0 = '|N_\t/,>5H'
    str_1 = 'wuo/6$\n77LOSs'
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
    multipart_request_data_dict_0 = module_3.MultipartRequestDataDict(**dict_0)
    request_data_dict_0 = module_3.RequestDataDict()
    callable_0 = None
    int_0 = 30
    set_0 = set()
    var_0 = module_1.prepare_request_body(str_0, callable_0, int_0, set_0, str_0)

def test_case_8():
    str_0 = 'wuo/6$\n77LOSs'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    multipart_request_data_dict_0 = module_3.MultipartRequestDataDict(**dict_0)
    request_data_dict_0 = module_3.RequestDataDict()
    prepared_request_0 = module_4.PreparedRequest()
    int_0 = 1338
    callable_0 = None
    set_0 = set()
    int_1 = None
    multipart_encoder_0 = module_0.MultipartEncoder(set_0, int_1)
    var_0 = module_1.prepare_request_body(str_0, callable_0, int_0, prepared_request_0)
    var_1 = module_1.prepare_request_body(multipart_encoder_0, callable_0, prepared_request_0, multipart_request_data_dict_0)
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)