# Automatically generated by Pynguin.
import requests.models as module_0
import httpie.uploads as module_1
import httpie.cli.dicts as module_2
import requests_toolbelt.multipart.encoder as module_3
import typing as module_4

def test_case_0():
    try:
        prepared_request_0 = module_0.PreparedRequest()
        bool_0 = True
        var_0 = module_1.compress_request(prepared_request_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x8a\xdcv\x0c\xed\x8f.\xee4\xc9s"S\x10\x0e\x885'
        multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
        multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        list_0 = [bytes_0]
        chunked_upload_stream_0 = module_1.ChunkedUploadStream(chunked_multipart_upload_stream_0, list_0)
        multipart_encoder_1 = module_3.MultipartEncoder(chunked_upload_stream_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        str_1 = 'invalid option '
        var_0 = module_1.prepare_request_body(str_0, str_1)
        multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
        request_data_dict_0 = module_2.RequestDataDict()
        chunked_upload_stream_0 = module_1.ChunkedUploadStream(multipart_request_data_dict_0, request_data_dict_0)
        tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)
        tuple_1 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)
        list_0 = [chunked_upload_stream_0]
        multipart_encoder_0 = module_3.MultipartEncoder(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
        list_0 = []
        multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0, list_0)
        callable_0 = None
        var_0 = module_1.prepare_request_body(multipart_encoder_0, callable_0)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        dict_0 = {}
        multipart_request_data_dict_1 = module_2.MultipartRequestDataDict(**dict_0)
        str_0 = ';:jb#y"0"\nvKNc\\or(Uh'
        tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0)
        prepared_request_0 = module_0.PreparedRequest()
        var_1 = module_1.prepare_request_body(multipart_encoder_0, callable_0, tuple_0, prepared_request_0)
        request_data_dict_0 = module_2.RequestDataDict(**dict_0)
        prepared_request_1 = module_0.PreparedRequest()
        set_0 = None
        var_2 = module_1.prepare_request_body(str_0, callable_0, set_0, str_0)
        request_data_dict_1 = module_2.RequestDataDict()
        bool_0 = False
        var_3 = module_1.compress_request(prepared_request_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
        multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        multipart_encoder_1 = module_3.MultipartEncoder(chunked_multipart_upload_stream_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
        list_0 = [bool_0, bool_0]
        multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0, list_0)
        callable_0 = None
        var_0 = module_1.prepare_request_body(multipart_encoder_0, callable_0)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        multipart_request_data_dict_1 = module_2.MultipartRequestDataDict()
        str_0 = ';:jb#y"0"\nvKNc\\or(Uh'
        tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_1, str_0, str_0)
        prepared_request_0 = module_0.PreparedRequest()
        multipart_encoder_1 = module_3.MultipartEncoder(chunked_multipart_upload_stream_0, prepared_request_0)
    except BaseException:
        pass

def test_case_6():
    try:
        multipart_request_data_dict_0 = module_2.MultipartRequestDataDict()
        list_0 = []
        multipart_encoder_0 = module_3.MultipartEncoder(multipart_request_data_dict_0, list_0)
        callable_0 = None
        request_data_dict_0 = module_2.RequestDataDict()
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        var_0 = module_1.prepare_request_body(multipart_encoder_0, callable_0, request_data_dict_0, request_data_dict_0, iterable_0)
        callable_1 = None
        var_1 = module_1.prepare_request_body(multipart_encoder_0, callable_1)
        chunked_multipart_upload_stream_1 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        dict_0 = {}
        multipart_request_data_dict_1 = module_2.MultipartRequestDataDict(**dict_0)
        str_0 = ';:jb#y"0"\nvKNc\\or(Uh'
        tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0)
        prepared_request_0 = module_0.PreparedRequest()
        var_2 = module_1.prepare_request_body(multipart_encoder_0, callable_1, tuple_0, prepared_request_0)
        request_data_dict_1 = module_2.RequestDataDict(**dict_0)
        prepared_request_1 = module_0.PreparedRequest()
        str_1 = None
        none_type_0 = None
        float_0 = None
        var_3 = module_1.prepare_request_body(str_1, callable_1, none_type_0, float_0)
        prepared_request_2 = module_0.PreparedRequest()
        int_0 = 968
        var_4 = module_1.prepare_request_body(str_0, callable_1, int_0, chunked_multipart_upload_stream_1, multipart_encoder_0)
        prepared_request_3 = module_0.PreparedRequest()
        bool_0 = False
        var_5 = module_1.compress_request(prepared_request_2, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        list_0 = []
        multipart_encoder_0 = module_3.MultipartEncoder(list_0)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        dict_0 = {bool_0: list_0}
        tuple_0 = (dict_0,)
        tuple_1 = (chunked_multipart_upload_stream_0, tuple_0)
        var_0 = None
        list_1 = [var_0, var_0, var_0, var_0]
        multipart_encoder_1 = module_3.MultipartEncoder(tuple_1, list_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'kB'
        int_0 = 130
        var_0 = module_1.prepare_request_body(str_0, int_0)
        bytes_0 = b'n\xae\xab\x9bO-\xb0w|$\xf1\x84\xc91F&\xda\xe7F'
        dict_0 = {}
        callable_0 = None
        int_1 = -1229
        float_0 = 1407.049776
        var_1 = module_1.prepare_request_body(bytes_0, callable_0, int_1, float_0)
        i_o_0 = module_4.IO(**dict_0)
        var_2 = i_o_0.readline()
        set_0 = {var_1, var_1, int_1}
        request_data_dict_0 = None
        multipart_encoder_0 = module_3.MultipartEncoder(set_0, request_data_dict_0)
    except BaseException:
        pass