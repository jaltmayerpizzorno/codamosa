# Automatically generated by Pynguin.
import typing as module_0
import httpie.uploads as module_1
import httpie.cli.dicts as module_2
import requests_toolbelt.multipart.encoder as module_3

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    i_o_0 = module_0.IO(*list_0)
    var_0 = i_o_0.__enter__()
    var_1 = i_o_0.readline()
    list_1 = [var_1, var_1, var_1]
    chunked_upload_stream_0 = module_1.ChunkedUploadStream(var_0, list_1)

def test_case_2():
    multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
    multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0)
    callable_0 = None
    var_0 = module_1.prepare_request_body(multipart_encoder_0, callable_0)
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    iterable_0 = chunked_multipart_upload_stream_0.__iter__()

def test_case_3():
    bytes_0 = b'\x8f\x88#'
    list_0 = []
    var_0 = module_1.prepare_request_body(bytes_0, list_0)

def test_case_4():
    multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
    multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0)
    callable_0 = None
    var_0 = module_1.prepare_request_body(multipart_encoder_0, callable_0)

def test_case_5():
    multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
    str_0 = '--no-sorted'
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_6():
    str_0 = 's\t`=CVhGETFOp\x0b<aZIL\x0b'
    callable_0 = None
    int_0 = None
    list_0 = []
    multipart_encoder_0 = module_3.MultipartEncoder(list_0)
    tuple_0 = (multipart_encoder_0,)
    var_0 = module_1.prepare_request_body(str_0, callable_0, int_0, str_0, tuple_0)

def test_case_7():
    str_0 = 'field0'
    str_1 = 'field1'
    str_2 = 'field2'
    str_3 = 'field3'
    str_4 = 'field4'
    str_5 = 'field5'
    str_6 = 'field6'
    str_7 = 'field7'
    str_8 = 'field8'
    str_9 = 'field9'
    str_10 = 'value'
    str_11 = {str_0: str_10, str_1: str_10, str_2: str_10, str_3: str_10, str_4: str_10, str_5: str_10, str_6: str_10, str_7: str_10, str_8: str_10, str_9: str_10}
    multipart_encoder_0 = module_3.MultipartEncoder(str_11)
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    var_0 = iter(chunked_multipart_upload_stream_0)
    var_1 = list(var_0)
    var_2 = len(var_1)

def test_case_8():
    multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
    i_o_0 = module_0.IO()
    bool_0 = i_o_0.writable()
    multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0)
    callable_0 = None
    int_0 = -1923
    list_0 = [i_o_0]
    var_0 = module_1.prepare_request_body(multipart_encoder_0, callable_0, int_0, list_0)