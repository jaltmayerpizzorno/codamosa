# Automatically generated by Pynguin.
import httpie.uploads as module_0
import requests_toolbelt.multipart.encoder as module_1
import requests.models as module_2
import httpie.cli.dicts as module_3
import typing as module_4

def test_case_0():
    try:
        str_0 = ' file: '
        str_1 = ")'^5D@\x0c))`zu\rd\\U"
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_1}
        list_0 = [dict_0, str_1, str_1]
        chunked_upload_stream_0 = module_0.ChunkedUploadStream(dict_0, list_0)
        iterable_0 = chunked_upload_stream_0.__iter__()
        multipart_encoder_0 = module_1.MultipartEncoder(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        prepared_request_0 = module_2.PreparedRequest()
        bool_0 = True
        var_0 = module_0.compress_request(prepared_request_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'JR7V-2$\tSnqM.IzI>T\tZ'
        list_0 = []
        dict_0 = {str_0: list_0}
        int_0 = 267
        bool_0 = True
        bytes_0 = b'\xfcR\xc9\x9e\x04\xc0\x05\xc3\xc3\xa7\n\xdb\xc1\x9c\x8fy\x96\xa0\xf7\xa2'
        var_0 = module_0.prepare_request_body(str_0, dict_0, int_0, bool_0, bytes_0)
        prepared_request_0 = module_2.PreparedRequest()
        bool_1 = False
        var_1 = module_0.compress_request(prepared_request_0, bool_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'b'
        bytes_1 = [bytes_0]
        var_0 = lambda chunk: print(chunk)
        chunked_upload_stream_0 = module_0.ChunkedUploadStream(bytes_1, var_0)
        iterable_0 = chunked_upload_stream_0.__iter__()
        iterable_1 = chunked_upload_stream_0.__iter__()
        var_1 = next(iterable_0)
        iterable_2 = chunked_upload_stream_0.__iter__()
        var_2 = next(iterable_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '8/BdXJx\x0c9eQ~T4OB ['
        str_1 = '--auth'
        dict_0 = {str_0: str_0, str_1: str_0, str_1: str_0}
        multipart_encoder_0 = module_1.MultipartEncoder(dict_0)
        chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        multipart_encoder_1 = module_1.MultipartEncoder(iterable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'JR7V-2$\tSnqM.IzI>T\tZ'
        list_0 = []
        dict_0 = {str_0: list_0}
        int_0 = 255
        list_1 = [dict_0]
        str_1 = 'l|w'
        request_data_dict_0 = module_3.RequestDataDict()
        prepared_request_0 = module_2.PreparedRequest()
        chunked_upload_stream_0 = module_0.ChunkedUploadStream(request_data_dict_0, prepared_request_0)
        list_2 = [str_1, str_1, chunked_upload_stream_0, list_1]
        chunked_upload_stream_1 = module_0.ChunkedUploadStream(list_1, list_2)
        bool_0 = True
        bytes_0 = b'\xfcR\xc9\x9e\x04\xc0\x05\xc3\xc3\xa7\n\xdb\xc1\x9c\x8fy\x96\xa0\xf7\xa2'
        var_0 = module_0.prepare_request_body(str_0, dict_0, int_0, bool_0, bytes_0)
        multipart_request_data_dict_0 = module_3.MultipartRequestDataDict()
        float_0 = 1889.118011749312
        chunked_upload_stream_2 = module_0.ChunkedUploadStream(float_0, str_0)
        list_3 = []
        chunked_upload_stream_3 = module_0.ChunkedUploadStream(chunked_upload_stream_2, list_3)
        tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)
        tuple_1 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0)
        i_o_0 = module_4.IO()
        bool_1 = i_o_0.writable()
        var_1 = i_o_0.__enter__()
        var_2 = module_0.prepare_request_body(str_0, list_0, var_1, int_0)
        i_o_1 = module_4.IO(*list_0)
        str_2 = ">elC#kr17l]'"
        str_3 = '..X\x0bOvbK@\x0cP/H#]\t9'
        var_3 = module_0.prepare_request_body(i_o_1, chunked_upload_stream_3, int_0, str_2, str_3)
        bool_2 = False
        var_4 = module_0.compress_request(prepared_request_0, bool_2)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        multipart_encoder_0 = module_1.MultipartEncoder(dict_0)
        chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
        chunked_upload_stream_0 = module_0.ChunkedUploadStream(multipart_encoder_0, chunked_multipart_upload_stream_0)
        chunked_multipart_upload_stream_1 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
        tuple_0 = (chunked_multipart_upload_stream_1,)
        multipart_encoder_1 = module_1.MultipartEncoder(tuple_0, multipart_encoder_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ';-s>pD/f\r5h'
        dict_0 = {str_0: str_0}
        multipart_encoder_0 = module_1.MultipartEncoder(dict_0)
        list_0 = [multipart_encoder_0, str_0, str_0]
        var_0 = module_0.prepare_request_body(multipart_encoder_0, list_0)
        multipart_request_data_dict_0 = module_3.MultipartRequestDataDict()
        chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)
        var_1 = multipart_encoder_0.to_string()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Missing Content-Range'
        int_0 = None
        int_1 = -1924
        var_0 = module_0.prepare_request_body(str_0, str_0, int_0, int_1)
        multipart_encoder_0 = module_1.MultipartEncoder(var_0)
    except BaseException:
        pass