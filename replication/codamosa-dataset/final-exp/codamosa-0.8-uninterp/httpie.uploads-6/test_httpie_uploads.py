# Automatically generated by Pynguin.
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests_toolbelt.multipart.encoder as module_2
import requests.models as module_3

def test_case_0():
    pass

def test_case_1():
    iterable_0 = None
    dict_0 = None
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(iterable_0, dict_0)

def test_case_2():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    callable_0 = None
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(multipart_request_data_dict_0, callable_0)
    multipart_encoder_0 = module_2.MultipartEncoder(chunked_upload_stream_0)
    chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)

def test_case_3():
    tuple_0 = ()
    multipart_encoder_0 = module_2.MultipartEncoder(tuple_0)
    tuple_1 = None
    var_0 = module_0.prepare_request_body(multipart_encoder_0, tuple_1)

def test_case_4():
    request_data_dict_0 = module_1.RequestDataDict()
    callable_0 = None
    str_0 = None
    float_0 = 0.1
    list_0 = []
    chunked_upload_stream_0 = module_0.ChunkedUploadStream(float_0, list_0)
    iterable_0 = chunked_upload_stream_0.__iter__()
    var_0 = module_0.prepare_request_body(request_data_dict_0, callable_0, str_0, iterable_0)
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    str_1 = '\tU!G{]Uk6bYx.]]/g3HZ'
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_1, str_1)

def test_case_5():
    request_data_dict_0 = module_1.RequestDataDict()
    list_0 = []
    request_data_dict_1 = module_1.RequestDataDict()
    callable_0 = None
    dict_0 = {}
    var_0 = module_0.prepare_request_body(request_data_dict_1, callable_0, dict_0, list_0)
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    str_0 = '\tU!G{]Uk6bYx.]]/g3HZ'
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_6():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    str_0 = '\tU!G{]Uk6bYx.]]/gHHZ'
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)

def test_case_7():
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    str_0 = "The main entry point. Invoke as `http' or `python -m httpie'.\n\n"
    tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0)

def test_case_8():
    request_data_dict_0 = module_1.RequestDataDict()
    callable_0 = None
    multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
    multipart_request_data_dict_1 = module_1.MultipartRequestDataDict()
    int_0 = -446
    list_0 = [multipart_request_data_dict_1, callable_0, int_0]
    var_0 = module_0.prepare_request_body(request_data_dict_0, callable_0, int_0, request_data_dict_0, list_0)
    prepared_request_0 = module_3.PreparedRequest()

def test_case_9():
    str_0 = "J'}"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    request_data_dict_0 = module_1.RequestDataDict(**dict_0)
    multipart_encoder_0 = module_2.MultipartEncoder(request_data_dict_0, dict_0)
    int_0 = None
    float_0 = -145.8763857718563
    var_0 = module_0.prepare_request_body(multipart_encoder_0, str_0, int_0, float_0)