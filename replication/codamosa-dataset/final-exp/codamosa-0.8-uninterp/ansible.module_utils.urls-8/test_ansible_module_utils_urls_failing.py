# Automatically generated by Pynguin.
import ansible.module_utils.urls as module_0

def test_case_0():
    try:
        str_0 = 'Upv'
        connection_error_0 = module_0.ConnectionError()
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()
        no_s_s_l_error_0 = None
        int_0 = 52
        bool_0 = True
        request_0 = module_0.Request(no_s_s_l_error_0, int_0, connection_error_0, int_0, bool_0, str_0)
        missing_module_error_0 = module_0.MissingModuleError(request_0, no_s_s_l_error_0)
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(missing_module_error_0)
        var_0 = request_0.options(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(str_0)
        dict_0 = {str_0: str_0, h_t_t_p_s_client_auth_handler_0: h_t_t_p_s_client_auth_handler_0, h_t_t_p_s_client_auth_handler_0: str_0}
        var_0 = h_t_t_p_s_client_auth_handler_0.https_open(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(bool_0)
        var_0 = unix_h_t_t_p_s_connection_0.connect()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '~z3'
        int_0 = 1688
        tuple_0 = ()
        list_0 = [tuple_0, str_0]
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(list_0, list_0)
        var_0 = s_s_l_validation_handler_0.detect_no_proxy(int_0)
        dict_0 = {}
        s_s_l_validation_error_0 = module_0.SSLValidationError(**dict_0)
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(s_s_l_validation_error_0)
        var_1 = unix_h_t_t_p_s_connection_0.__call__()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'E}Dz485sF>J,X '
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(str_0)
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(unix_h_t_t_p_connection_0)
        var_0 = unix_h_t_t_p_s_connection_0.connect()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'http://pypi.pyhon.org/pp/'
        var_0 = module_0.open_url(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Depsolve Error occurred attempting to install group: {0}'
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(str_0)
        var_0 = unix_h_t_t_p_connection_0.connect()
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        str_0 = 'Remove strings in ``no_log_strings`` from value.\n\n    If value is a container type, then remove a lot more.\n\n    Use of ``deferred_removals`` exists, rather than a pure recursive solution,\n    because of the potential to hit the maximum recursion depth when dealing with\n    large amounts of data (see `issue #24560 <https://github.com/ansible/ansible/issues/24560>`_).\n    '
        list_1 = [str_0, str_0, str_0]
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(list_1)
        unix_h_t_t_p_s_connection_0 = None
        no_s_s_l_error_0 = module_0.NoSSLError()
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(s_s_l_validation_error_0, no_s_s_l_error_0)
        var_0 = s_s_l_validation_handler_0.detect_no_proxy(unix_h_t_t_p_s_connection_0)
        var_1 = unix_h_t_t_p_handler_0.http_open(s_s_l_validation_error_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'h\ntps://pypi.python.org/pypi/'
        var_0 = module_0.open_url(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        no_s_s_l_error_0 = module_0.NoSSLError()
        var_0 = module_0.generic_urlparse(no_s_s_l_error_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'Test Error'
        set_0 = {str_0, str_0, str_0, str_0}
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        list_0 = [set_0, s_s_l_validation_error_0, set_0, str_0]
        var_0 = module_0.build_ssl_validation_error(set_0, s_s_l_validation_error_0, list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -1290
        int_1 = 9
        int_2 = 1
        int_3 = 8
        int_4 = 4
        int_5 = (int_1, int_0, int_1, int_2, int_3, int_0, int_4)
        str_0 = '-0000'
        var_0 = module_0.rfc2822_date_string(int_5, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'LLMAb[`'
        connection_error_0 = module_0.ConnectionError()
        var_0 = module_0.generic_urlparse(str_0)
        float_0 = 4112.453019
        bool_0 = False
        list_0 = [connection_error_0, var_0, var_0]
        request_0 = module_0.Request(float_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        custom_h_t_t_p_s_handler_0 = None
        var_0 = module_0.prepare_multipart(custom_h_t_t_p_s_handler_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'Upv'
        connection_error_0 = module_0.ConnectionError()
        no_s_s_l_error_0 = None
        int_0 = 37
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        float_0 = 826.566226
        var_0 = module_0.basic_auth_header(parse_result_dotted_dict_0, float_0)
        bool_0 = False
        str_1 = '/4'
        request_0 = module_0.Request(no_s_s_l_error_0, int_0, connection_error_0, int_0, bool_0, str_1)
        var_1 = request_0.options(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        var_0 = module_0.url_argument_spec()
        str_0 = ''
        bytes_0 = b'\xe8\t\xbeN\xfft8\xdarE\xf1\xa0\xe9){'
        float_0 = -1663.0
        int_0 = 705
        bool_0 = False
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(bool_0)
        int_1 = 301
        var_1 = module_0.fetch_url(str_0, bytes_0, float_0, float_0, int_0, unix_h_t_t_p_s_connection_0, int_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "&'`"
        var_0 = module_0.open_url(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        proxy_error_0 = module_0.ProxyError()
        str_0 = None
        no_s_s_l_error_0 = module_0.NoSSLError()
        tuple_0 = ()
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(proxy_error_0)
        var_0 = module_0.maybe_add_ssl_handler(tuple_0, unix_h_t_t_p_s_connection_0)
        str_1 = 'boom'
        list_0 = [proxy_error_0, proxy_error_0, str_1]
        dict_0 = {str_0: list_0}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        float_0 = 933.31475
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        request_with_method_0 = module_0.RequestWithMethod(dict_0, parse_result_dotted_dict_0, float_0, dict_0, s_s_l_validation_error_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ';Bs30\x0b%v0P'
        var_0 = module_0.generic_urlparse(str_0)
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        set_0 = set()
        var_1 = module_0.get_channel_binding_cert_hash(set_0)
        str_1 = 'https'
        str_2 = 'IJUVhg'
        dict_0 = {str_2: var_1, str_2: var_1, str_0: var_0, str_2: var_1}
        bytes_0 = b'\x1a\x8b\x04\x90\x96o?XiG\xe1\xc3\xc7\xe7'
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(dict_0, bytes_0)
        var_2 = s_s_l_validation_handler_0.http_request(str_1)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '0ZkeXT}@DgO.:~xMpz1T'
        list_0 = [str_0, str_0]
        complex_0 = None
        list_1 = [complex_0, complex_0, complex_0]
        list_2 = [list_1]
        proxy_error_0 = module_0.ProxyError(*list_2)
        list_3 = [proxy_error_0]
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(list_3)
        var_0 = unix_h_t_t_p_connection_0.__call__(*list_0)
        var_1 = module_0.url_argument_spec()
        float_0 = 451.46
        var_2 = module_0.rfc2822_date_string(float_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 37
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(int_0)
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(h_t_t_p_s_client_auth_handler_0, parse_result_dotted_dict_0)
        var_0 = parse_result_dotted_dict_0.as_list()
        bool_0 = False
        var_1 = s_s_l_validation_handler_0.validate_proxy_response(bool_0)
    except BaseException:
        pass

def test_case_21():
    try:
        dict_0 = {}
        bytes_0 = b'>\xa4 4Z>'
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        no_s_s_l_error_0 = module_0.NoSSLError()
        dict_1 = {bytes_0: no_s_s_l_error_0}
        bool_0 = False
        list_0 = []
        str_0 = '{X\te47<*1KC~J?rA`Z'
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(list_0, str_0)
        var_0 = module_0.fetch_url(dict_0, bytes_0, dict_1, bool_0, s_s_l_validation_handler_0, dict_0, dict_1)
    except BaseException:
        pass

def test_case_22():
    try:
        custom_h_t_t_p_s_handler_0 = None
        str_0 = 'AY-,40I s\\'
        list_0 = None
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(s_s_l_validation_error_0, custom_h_t_t_p_s_handler_0)
        var_0 = s_s_l_validation_handler_0.make_context(list_0, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        custom_h_t_t_p_s_handler_0 = None
        str_0 = 'G'
        dict_0 = {str_0: custom_h_t_t_p_s_handler_0, str_0: custom_h_t_t_p_s_handler_0, str_0: custom_h_t_t_p_s_handler_0, str_0: str_0, str_0: custom_h_t_t_p_s_handler_0, str_0: custom_h_t_t_p_s_handler_0}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
        var_0 = module_0.prepare_multipart(parse_result_dotted_dict_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'A/proc/cpuinfo'
        var_0 = module_0.open_url(str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_25():
    try:
        bool_0 = False
        request_0 = module_0.Request(bool_0)
        connection_error_0 = module_0.ConnectionError()
        dict_0 = {}
        var_0 = request_0.options(dict_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = '~sl@i~sMu\r@Q?='
        int_0 = 36
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(int_0)
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(h_t_t_p_s_client_auth_handler_0, parse_result_dotted_dict_0)
        var_0 = s_s_l_validation_handler_0.get_ca_certs()
        str_1 = 'yKKv-['
        dict_0 = {str_0: str_0, str_1: str_1}
        str_2 = '2$T\\z'
        int_1 = 117
        dict_1 = {str_2: dict_0, str_2: int_1}
        var_1 = module_0.fetch_file(str_2, dict_1)
    except BaseException:
        pass

def test_case_27():
    try:
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        var_0 = module_0.getpeercert(s_s_l_validation_error_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = 'Yv]P==k)kYi?WPf7+=o['
        int_0 = 36
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(int_0)
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(h_t_t_p_s_client_auth_handler_0, parse_result_dotted_dict_0)
        var_0 = s_s_l_validation_handler_0.get_ca_certs()
        str_1 = 'yKv-'
        str_2 = '#95l}\x0b5\x0brlq\\>AXmtN@'
        dict_0 = {str_0: str_0, str_2: str_1}
        var_1 = module_0.get_channel_binding_cert_hash(dict_0)
        bool_0 = False
        request_0 = module_0.Request(bool_0)
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(request_0)
        connection_error_0 = module_0.ConnectionError()
        var_2 = request_0.head(int_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = 'Upv'
        connection_error_0 = module_0.ConnectionError()
        no_s_s_l_error_0 = None
        int_0 = 44
        bool_0 = False
        request_0 = module_0.Request(no_s_s_l_error_0, int_0, connection_error_0, int_0, bool_0, str_0)
        var_0 = request_0.options(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = 'https://pypi.python.org/pypi/'
        var_0 = module_0.open_url(str_0)
        bytes_0 = b'\\\xean5\x87'
        float_0 = -4119.543375
        s_s_l_validation_error_0 = None
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(s_s_l_validation_error_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(bytes_0, float_0, unix_h_t_t_p_s_connection_0)
        var_1 = s_s_l_validation_handler_0.get_ca_certs()
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'https://pypi.python.org/pypi/'
        var_0 = module_0.open_url(str_0)
        bool_0 = True
        var_1 = module_0.getpeercert(var_0, bool_0)
        bytes_0 = b'-----BEGIN CERTIFICATE-----'
        float_0 = 354.2
        set_0 = {float_0, bytes_0}
        var_2 = module_0.build_ssl_validation_error(float_0, bytes_0, bool_0, set_0)
    except BaseException:
        pass

def test_case_32():
    try:
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        bool_0 = False
        str_0 = 'fk<--K*m3;\n[2k.('
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler(str_0)
        str_1 = ']>;1p@tGR%,C'
        bytes_0 = b"\xb6_\xd2\xe3\x19'\xb2\x98Q\xf9\xb8\xcf\xdb\xd3\xa8\r\xd0\xfa"
        list_0 = []
        dict_0 = {}
        parse_result_dotted_dict_1 = module_0.ParseResultDottedDict(*list_0, **dict_0)
        request_0 = module_0.Request(bool_0, custom_h_t_t_p_s_handler_0, str_1, bytes_0, parse_result_dotted_dict_1)
        var_0 = request_0.patch(parse_result_dotted_dict_0, s_s_l_validation_error_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = ';Bs30\x0b%v0P'
        var_0 = module_0.generic_urlparse(str_0)
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        float_0 = -508.2128
        bool_0 = False
        str_1 = 'o3;To?\n@(co3ezFYTL'
        missing_module_error_0 = module_0.MissingModuleError(bool_0, str_1)
        tuple_0 = None
        request_0 = module_0.Request(bool_0, missing_module_error_0, tuple_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        proxy_error_0 = module_0.ProxyError()
        str_2 = 'ZXl'
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(str_2)
        str_3 = 'cE~>\n Nt`J\x0cXM'
        dict_0 = {str_3: float_0, str_3: var_0}
        var_1 = request_0.get(unix_h_t_t_p_connection_0, **dict_0)
    except BaseException:
        pass

def test_case_34():
    try:
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, tuple_0]
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        str_0 = 'KSpbi*'
        str_1 = 'https'
        dict_0 = {str_0: tuple_0, str_1: str_0, str_1: tuple_0}
        list_1 = [str_1]
        bytes_0 = b'\xc4\xc3\x8f]\xbb\xca'
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(dict_0, list_1, bytes_0)
        bytes_1 = b'\xa3\xbf\xdaAs\x9f\xc5+i;\xb5\x86|\xfaf\x1e\x18\xc8|\\'
        str_2 = "*v''Zccy?qn$`A*sMd;"
        var_0 = module_0.atexit_remove_file(str_2)
        var_1 = module_0.generic_urlparse(bytes_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler(s_s_l_validation_handler_0, bytes_1)
        var_2 = custom_h_t_t_p_s_handler_0.https_open(list_0)
    except BaseException:
        pass

def test_case_35():
    try:
        int_0 = 55
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(int_0)
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        str_0 = 'ftp'
        str_1 = 'Darwin'
        str_2 = '\t_Xeo#=_@*UE'
        dict_0 = {str_0: int_0, str_1: str_1, str_2: h_t_t_p_s_client_auth_handler_0}
        missing_module_error_0 = module_0.MissingModuleError(str_0, dict_0)
        custom_h_t_t_p_s_connection_0 = None
        tuple_0 = ()
        list_0 = [h_t_t_p_s_client_auth_handler_0, h_t_t_p_s_client_auth_handler_0, parse_result_dotted_dict_0]
        dict_1 = {}
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(dict_1)
        dict_2 = {}
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(unix_h_t_t_p_s_connection_0, dict_2)
        dict_3 = {}
        request_0 = module_0.Request(tuple_0, list_0, s_s_l_validation_handler_0, dict_3, s_s_l_validation_handler_0)
        var_0 = request_0.put(missing_module_error_0, custom_h_t_t_p_s_connection_0)
    except BaseException:
        pass

def test_case_36():
    try:
        connection_error_0 = module_0.ConnectionError()
        str_0 = '*B$Wm.?|r6bm*<]V}Y3T'
        float_0 = -1754.134707
        str_1 = 'hn;p'
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        tuple_0 = (float_0, str_1, s_s_l_validation_error_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(str_0, tuple_0)
        var_0 = s_s_l_validation_handler_0.get_ca_certs()
        str_2 = ''
        str_3 = 'Linux'
        dict_0 = {str_2: var_0, str_3: str_2}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
        var_1 = parse_result_dotted_dict_0.as_list()
        set_0 = set()
        var_2 = s_s_l_validation_handler_0.validate_proxy_response(set_0, tuple_0)
    except BaseException:
        pass

def test_case_37():
    try:
        custom_h_t_t_p_s_handler_0 = None
        str_0 = 'AY-,40I s\\'
        var_0 = module_0.get_channel_binding_cert_hash(custom_h_t_t_p_s_handler_0)
        dict_0 = {str_0: custom_h_t_t_p_s_handler_0, str_0: custom_h_t_t_p_s_handler_0, str_0: str_0, str_0: str_0}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        float_0 = 60.0
        no_s_s_l_error_0 = module_0.NoSSLError()
        request_0 = module_0.Request()
        var_1 = request_0.delete(float_0, **dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        int_0 = 86
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(int_0)
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        str_0 = 'directories'
        connection_error_0 = module_0.ConnectionError()
        no_s_s_l_error_0 = None
        list_0 = [str_0, str_0, str_0, str_0, parse_result_dotted_dict_0]
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler(list_0)
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(custom_h_t_t_p_s_handler_0)
        request_0 = module_0.Request(no_s_s_l_error_0, no_s_s_l_error_0, unix_h_t_t_p_s_connection_0, str_0, h_t_t_p_s_client_auth_handler_0, parse_result_dotted_dict_0)
        var_0 = request_0.options(str_0)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = 'https://pypi.python.org/pypi/'
        str_1 = None
        var_0 = module_0.open_url(str_1, str_0, str_0, str_1, str_1, str_0, str_0, str_1, str_0)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'https://pypi.python.org/pypi/'
        str_1 = 'E\\lud\neeNY,RN\tkbg?V'
        dict_0 = {}
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(str_1, **dict_0)
        list_0 = [str_0, str_1, dict_0]
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        dict_1 = {str_1: list_0}
        set_0 = set()
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        var_0 = module_0.open_url(unix_h_t_t_p_handler_0, s_s_l_validation_error_0, dict_1, set_0, dict_0, no_s_s_l_error_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'https://pypi.python.org/pypi/'
        var_0 = module_0.open_url(str_0)
        bytes_0 = b'\\\xean5\x87'
        list_0 = [bytes_0, bytes_0, str_0]
        bool_0 = True
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        dict_0 = {}
        no_s_s_l_error_0 = module_0.NoSSLError(**dict_0)
        bool_1 = True
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(bool_1)
        unix_h_t_t_p_handler_1 = module_0.UnixHTTPHandler(unix_h_t_t_p_handler_0)
        float_0 = 122.9
        missing_module_error_0 = module_0.MissingModuleError(float_0, parse_result_dotted_dict_0)
        missing_module_error_1 = module_0.MissingModuleError(unix_h_t_t_p_handler_1, missing_module_error_0)
        int_0 = 1065
        request_0 = module_0.Request(parse_result_dotted_dict_0, no_s_s_l_error_0, missing_module_error_1, unix_h_t_t_p_handler_0, list_0, int_0)
        var_1 = request_0.post(bool_0)
    except BaseException:
        pass