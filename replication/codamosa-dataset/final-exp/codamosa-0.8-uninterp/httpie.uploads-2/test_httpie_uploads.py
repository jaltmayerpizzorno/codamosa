# Automatically generated by Pynguin.
import httpie.uploads as module_0
import requests_toolbelt.multipart.encoder as module_1
import httpie.cli.dicts as module_2
import requests.models as module_3

def test_case_0():
    pass

def test_case_1():
    int_0 = -19
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(int_0, int_0)

def test_case_2():
    str_0 = 'k'
    str_1 = 'v'
    str_2 = {str_0: str_1}
    multipart_encoder_0 = module_1.MultipartEncoder(str_2)
    chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
    var_0 = list(chunked_multipart_upload_stream_0)

def test_case_3():
    i_o_0 = None
    list_0 = [i_o_0, i_o_0, i_o_0, i_o_0]
    var_0 = module_0.prepare_request_body(i_o_0, list_0)

def test_case_4():
    bytes_0 = None
    tuple_0 = ()
    request_data_dict_0 = module_2.RequestDataDict()
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(tuple_0, request_data_dict_0)
    prepared_request_0 = module_3.PreparedRequest()
    multipart_encoder_0 = module_1.MultipartEncoder(chunked_upload_stream_0, bytes_0)
    bool_0 = False
    var_0 = module_0.prepare_request_body(multipart_encoder_0, bool_0)

def test_case_5():
    multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0)

def test_case_6():
    dict_0 = {}
    multipart_request_data_dict_0 = module_2.MultipartRequestDataDict(**dict_0)
    bytes_0 = b'\xffBQX\xd8\xb5\xf1\xc0\xd5\x83\x88\xde\xa4{\xe0'
    str_0 = "40gE\\'!"
    int_0 = 5
    tuple_0 = None
    tuple_1 = (int_0, tuple_0)
    var_0 = module_0.prepare_request_body(bytes_0, str_0, dict_0, tuple_1)

def test_case_7():
    str_0 = '\r{oV'
    prepared_request_0 = module_3.PreparedRequest()
    multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_8():
    str_0 = 'title'
    str_1 = 'b*?'
    bool_0 = False
    bool_1 = True
    var_0 = module_0.prepare_request_body(str_0, bool_0, bool_0, bool_0, bool_1)
    var_1 = module_0.prepare_request_body(str_0, str_1, str_1, bool_0, bool_0)

def test_case_9():
    tuple_0 = ()
    multipart_encoder_0 = module_1.MultipartEncoder(tuple_0)
    chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
    float_0 = -2316.1
    dict_0 = {float_0: float_0, float_0: float_0}
    list_0 = [float_0]
    int_0 = -1394
    bool_0 = False
    str_0 = '\n'
    tuple_1 = (multipart_encoder_0, str_0)
    var_0 = module_0.prepare_request_body(multipart_encoder_0, list_0, int_0, bool_0, tuple_1)
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(dict_0, list_0)
    iterable_0 = chunked_upload_stream_0.__iter__()
    iterable_1 = chunked_upload_stream_0.__iter__()