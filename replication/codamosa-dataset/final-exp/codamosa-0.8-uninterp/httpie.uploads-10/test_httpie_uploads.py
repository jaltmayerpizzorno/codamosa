# Automatically generated by Pynguin.
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

def test_case_0():
    pass

def test_case_1():
    iterable_0 = None
    multipart_request_data_dict_0 = module_0.MultipartRequestDataDict()
    chunked_upload_stream_0 = module_1.ChunkedUploadStream(iterable_0, multipart_request_data_dict_0)

def test_case_2():
    dict_0 = {}
    int_0 = 96
    multipart_encoder_0 = module_2.MultipartEncoder(dict_0, int_0)
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    iterable_0 = chunked_multipart_upload_stream_0.__iter__()

def test_case_3():
    str_0 = 'M60h+AXb\nK'
    bool_0 = False
    var_0 = module_1.prepare_request_body(str_0, bool_0)

def test_case_4():
    dict_0 = {}
    int_0 = 96
    multipart_encoder_0 = module_2.MultipartEncoder(dict_0, int_0)
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    str_0 = 'default_options'
    var_0 = module_1.prepare_request_body(multipart_encoder_0, str_0, int_0)
    iterable_0 = chunked_multipart_upload_stream_0.__iter__()

def test_case_5():
    str_0 = ''
    var_0 = lambda data: str_0
    str_1 = 'test_string'
    bool_0 = True
    bool_1 = True
    var_1 = None
    var_2 = module_1.prepare_request_body(str_1, var_0, var_1, bool_0, bool_1)
    var_3 = lambda data: str_0

def test_case_6():
    multipart_request_data_dict_0 = module_0.MultipartRequestDataDict()
    str_0 = '#E]l"<0]J| u'
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_7():
    dict_0 = {}
    multipart_encoder_0 = module_2.MultipartEncoder(dict_0)
    str_0 = '9_qS2p-zI*'
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    iterable_0 = chunked_multipart_upload_stream_0.__iter__()
    var_0 = multipart_encoder_0.to_string()
    multipart_request_data_dict_0 = module_0.MultipartRequestDataDict(**dict_0)
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0)
    chunked_multipart_upload_stream_1 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    multipart_encoder_1 = module_2.MultipartEncoder(chunked_multipart_upload_stream_1)

def test_case_8():
    str_0 = '\tW'
    str_1 = 'value1'
    str_2 = (str_0, str_1)
    str_3 = 'field2'
    str_4 = 'value2'
    str_5 = (str_3, str_4)
    str_6 = 'field3'
    str_7 = 'value3'
    str_8 = (str_6, str_7)
    str_9 = [str_2, str_5, str_8]
    multipart_encoder_0 = module_2.MultipartEncoder(str_9)
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    iterable_0 = chunked_multipart_upload_stream_0.__iter__()
    var_0 = next(iterable_0)

def test_case_9():
    str_0 = ''
    var_0 = lambda data: str_0
    str_1 = 'test_string'
    bool_0 = True
    bool_1 = True
    var_1 = None
    var_2 = module_1.prepare_request_body(str_1, var_0, var_1, bool_0, bool_1)
    str_2 = 'test_string'
    bool_2 = True
    bool_3 = False
    var_3 = None
    var_4 = module_1.prepare_request_body(str_1, str_2, var_3, bool_2, bool_3)

def test_case_10():
    dict_0 = {}
    multipart_encoder_0 = module_2.MultipartEncoder(dict_0)
    var_0 = multipart_encoder_0.to_string()
    i_o_0 = module_3.IO(**dict_0)
    var_1 = i_o_0.read()
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    iterable_0 = chunked_multipart_upload_stream_0.__iter__()
    bytes_0 = b"\x84\x98\xb3\x8d\xd0:\xd6\x13\xba'[C\xcegu"
    str_0 = None
    list_0 = None
    dict_1 = {str_0: var_1, str_0: multipart_encoder_0, str_0: list_0}
    multipart_request_data_dict_0 = module_0.MultipartRequestDataDict(**dict_1)
    tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0)
    list_1 = []
    optional_0 = None
    chunked_multipart_upload_stream_1 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    multipart_request_data_dict_1 = module_0.MultipartRequestDataDict()
    var_2 = module_1.prepare_request_body(bytes_0, list_1, optional_0, multipart_request_data_dict_1)
    int_0 = 1529
    tuple_1 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_1, str_0, str_0)
    prepared_request_0 = module_4.PreparedRequest()
    prepared_request_1 = module_4.PreparedRequest()
    multipart_encoder_1 = module_2.MultipartEncoder(iterable_0)
    tuple_2 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_1, str_0)
    request_data_dict_0 = module_0.RequestDataDict(**dict_1)
    var_3 = module_1.prepare_request_body(multipart_encoder_1, tuple_0, int_0, request_data_dict_0)

def test_case_11():
    dict_0 = {}
    multipart_encoder_0 = module_2.MultipartEncoder(dict_0)
    str_0 = '9_qS2p-zI*'
    var_0 = multipart_encoder_0.to_string()
    tuple_0 = (multipart_encoder_0, str_0)
    i_o_0 = module_3.IO(**dict_0)
    var_1 = i_o_0.read()
    bool_0 = False
    var_2 = module_1.prepare_request_body(str_0, var_1, bool_0)
    chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    iterable_0 = chunked_multipart_upload_stream_0.__iter__()
    bytes_0 = b"\x84\x98\xb3\x8d\xd0:\xd6\x13\xba'[C\xcegu"
    chunked_multipart_upload_stream_1 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    tuple_1 = (tuple_0, bytes_0, multipart_encoder_0)
    list_0 = [tuple_1, bytes_0]
    str_1 = None
    list_1 = None
    dict_1 = {str_1: var_1, str_1: multipart_encoder_0, str_1: list_1}
    multipart_request_data_dict_0 = module_0.MultipartRequestDataDict(**dict_1)
    tuple_2 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_1)
    chunked_multipart_upload_stream_2 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
    multipart_request_data_dict_1 = module_0.MultipartRequestDataDict(**dict_0)
    callable_0 = None
    float_0 = 1682.0
    var_3 = module_1.prepare_request_body(str_0, callable_0, float_0, chunked_multipart_upload_stream_2)
    var_4 = multipart_encoder_0.to_string()
    tuple_3 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)
    prepared_request_0 = module_4.PreparedRequest()
    prepared_request_1 = module_4.PreparedRequest()
    chunked_upload_stream_0 = module_1.ChunkedUploadStream(chunked_multipart_upload_stream_0, list_0)
    multipart_encoder_1 = module_2.MultipartEncoder(chunked_upload_stream_0, float_0)
    chunked_multipart_upload_stream_3 = module_1.ChunkedMultipartUploadStream(multipart_encoder_1)

def test_case_12():
    str_0 = 'hello=world'
    var_0 = lambda chunk: chunk
    var_1 = None
    bool_0 = True
    bool_1 = False
    var_2 = module_1.prepare_request_body(str_0, var_0, var_1, bool_0, bool_1)
    var_3 = type(var_2)
    int_0 = 0
    var_4 = var_2.stream
    var_5 = list(var_4)[int_0]
    var_6 = lambda chunk: chunk