# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        str_0 = 'd|F'
        list_0 = [str_0, str_0]
        var_0 = module_0.check_required_one_of(str_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '{0} must be installed and visible from {1}.'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '9c~$.@$tf*bA'
        str_1 = "/'<"
        var_0 = module_0.safe_eval(str_1)
        int_0 = -488
        var_1 = module_0.check_mutually_exclusive(str_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'lvlF`Pz9dpZ'
        str_1 = '}p$qpdm,0'
        tuple_0 = (str_1,)
        var_0 = module_0.check_mutually_exclusive(tuple_0, str_0)
        var_1 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'q<[`qUFxSQW#'
        tuple_0 = None
        bool_0 = True
        var_0 = module_0.check_required_together(str_0, tuple_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'G\x0b=?'
        var_0 = module_0.check_type_dict(str_0)
        int_0 = 1874
        bytes_0 = None
        var_1 = module_0.check_required_by(int_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'G/nY>6'
        var_0 = module_0.check_type_list(str_0)
        tuple_0 = ()
        bool_0 = False
        var_1 = module_0.check_required_arguments(tuple_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '{0} must be installed and visible from {1}.'
        set_0 = {str_0, str_0, str_0}
        float_0 = 3414.0
        var_0 = module_0.check_required_if(set_0, float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 512.0
        str_0 = ''
        int_0 = -98
        var_0 = module_0.check_required_together(str_0, int_0)
        bytes_0 = b'a\xca\xd8\x02\x0bB\xb7\xb3kN'
        var_1 = module_0.check_missing_parameters(float_0, bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = ' MKEa-t.'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.check_type_str(dict_0, str_0)
        bytes_0 = b'\x9d\x0e\xf4\n\xe9T7\xb0'
        var_1 = module_0.check_type_bits(bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 1182.4203
        var_0 = module_0.check_type_path(float_0)
        var_1 = module_0.check_missing_parameters(float_0)
        complex_0 = None
        dict_0 = None
        bool_0 = False
        var_2 = module_0.check_type_str(complex_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'needs root privileges'
        float_0 = -1491.4
        tuple_0 = (str_0, float_0)
        var_0 = module_0.count_terms(str_0, tuple_0)
        str_1 = None
        var_1 = module_0.check_type_list(str_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'G?'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        list_0 = []
        var_0 = module_0.check_type_dict(list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'W'
        str_1 = '\noptions:\n  method:\n    description:\n    - The HTTP Method of the request.\n    type: str\n  follow_redirects:\n    description:\n    - Whether or the module should follow redirects.\n    - C(all) will follow all redirect.\n    - C(none) will not follow any redirect.\n    - C(safe) will follow only "safe" redirects, where "safe" means that the\n      client is only doing a C(GET) or C(HEAD) on the URI to which it is being\n      redirected.\n    - When following a redirected URL, the C(Authorization) header and any\n      credentials set will be dropped and not redirected.\n    choices:\n    - all\n    - none\n    - safe\n    default: safe\n    type: str\n  headers:\n    description:\n    - Extra headers to set on the request.\n    - This should be a dictionary where the key is the header name and the\n      value is the value for that header.\n    type: dict\n  http_agent:\n    description:\n    - Header to identify as, generally appears in web server logs.\n    - This is set to the C(User-Agent) header on a HTTP request.\n    default: ansible-httpget\n    type: str\n  maximum_redirection:\n    description:\n    - Specify how many times the module will redirect a connection to an\n      alternative URI before the connection fails.\n    - If set to C(0) or I(follow_redirects) is set to C(none), or C(safe) when\n      not doing a C(GET) or C(HEAD) it prevents all redirection.\n    default: 50\n    type: int\n  timeout:\n    description:\n    - Specifies how long the request can be pending before it times out (in\n      seconds).\n    - Set to C(0) to specify an infinite timeout.\n    default: 30\n    type: int\n  validate_certs:\n    description:\n    - If C(no), SSL certificates will not be validated.\n    - This should only be used on personally controlled sites using self-signed\n      certificates.\n    default: yes\n    type: bool\n  client_cert:\n    description:\n    - The path to the client certificate (.pfx) that is used for X509\n      authentication. This path can either be the path to the C(pfx) on the\n      filesystem or the PowerShell certificate path\n      C(Cert:\\CurrentUser\\My\\<thumbprint>).\n    - The WinRM connection must be authenticated with C(CredSSP) or C(become)\n      is used on the task if the certificate file is not password protected.\n    - Other authentication types can set I(client_cert_password) when the cert\n      is password protected.\n    type: str\n  client_cert_password:\n    description:\n    - The password for I(client_cert) if the cert is password protected.\n    type: str\n  force_basic_auth:\n    description:\n    - By default the authentication header is only sent when a webservice\n      responses to an initial request with a 401 status. Since some basic auth\n      services do not properly send a 401, logins will fail.\n    - This option forces the sending of the Basic authentication header upon\n      the original request.\n    default: no\n    type: bool\n  url_username:\n    description:\n    - The username to use for authentication.\n    type: str\n  url_password:\n    description:\n    - The password for I(url_username).\n    type: str\n  use_default_credential:\n    description:\n    - Uses the current user\'s credentials when authenticating with a server\n      protected with C(NTLM), C(Kerberos), or C(Negotiate) authentication.\n    - Sites that use C(Basic) auth will still require explicit credentials\n      through the I(url_username) and I(url_password) options.\n    - The module will only have access to the user\'s credentials if using\n      C(become) with a password, you are connecting with SSH using a password,\n      or connecting with WinRM using C(CredSSP) or C(Kerberos with delegation).\n    - If not using C(become) or a different auth method to the ones stated\n      above, there will be no default credentials available and no\n      authentication will occur.\n    default: no\n    type: bool\n  use_proxy:\n    description:\n    - If C(no), it will not use the proxy defined in IE for the current user.\n    default: yes\n    type: bool\n  proxy_url:\n    description:\n    - An explicit proxy to use for the request.\n    - By default, the request will use the IE defined proxy unless I(use_proxy)\n      is set to C(no).\n    type: str\n  proxy_username:\n    description:\n    - The username to use for proxy authentication.\n    type: str\n  proxy_password:\n    description:\n    - The password for I(proxy_username).\n    type: str\n  proxy_use_default_credential:\n    description:\n    - Uses the current user\'s credentials when authenticating with a proxy host\n      protected with C(NTLM), C(Kerberos), or C(Negotiate) authentication.\n    - Proxies that use C(Basic) auth will still require explicit credentials\n      through the I(proxy_username) and I(proxy_password) options.\n    - The module will only have access to the user\'s credentials if using\n      C(become) with a password, you are connecting with SSH using a password,\n      or connecting with WinRM using C(CredSSP) or C(Kerberos with delegation).\n    - If not using C(become) or a different auth method to the ones stated\n      above, there will be no default credentials available and no proxy\n      authentication will occur.\n    default: no\n    type: bool\nseealso:\n- module: community.windows.win_inet_proxy\n'
        var_0 = module_0.check_type_jsonarg(str_1)
        bool_0 = False
        int_0 = 86
        set_0 = {str_0, str_0, str_0, int_0}
        list_0 = [str_0, bool_0, str_0]
        var_1 = module_0.check_mutually_exclusive(set_0, list_0)
        float_0 = None
        var_2 = module_0.check_type_bool(float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = 1386
        list_0 = []
        str_0 = '\rLM*_v%F~s8PMx'
        var_0 = module_0.check_required_together(list_0, str_0)
        var_1 = module_0.check_type_int(int_0)
        complex_0 = None
        str_1 = ''
        var_2 = module_0.check_required_if(complex_0, str_1)
        var_3 = module_0.check_type_bool(str_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "Uc|mm3tF;j'F*"
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '^'
        var_0 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        tuple_0 = ()
        bool_0 = True
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: bool_0, bool_0: bool_0}
        dict_1 = {tuple_0: dict_0, bool_0: dict_0}
        list_0 = [tuple_0, tuple_0, dict_1, dict_0]
        var_0 = module_0.check_type_path(list_0)
        var_1 = module_0.check_type_float(tuple_0)
    except BaseException:
        pass

def test_case_19():
    try:
        list_0 = None
        var_0 = module_0.check_type_bytes(list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        list_0 = None
        var_0 = module_0.check_type_jsonarg(list_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'Es^{^'
        var_0 = module_0.check_type_jsonarg(str_0)
        var_1 = module_0.safe_eval(str_0)
        bool_0 = None
        var_2 = module_0.check_type_bits(bool_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '{0} must be installed and visible from {1}.'
        dict_0 = {str_0: str_0, str_0: str_0}
        bytes_0 = b'\xf2A\xdec\x0c\xafP\xfd\x9c\xb3\x96\xddl\x83'
        var_0 = module_0.count_terms(dict_0, bytes_0)
        var_1 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = ': : Warning: Cannot stat: No such file or directory$'
        str_1 = 'V\r4bQ'
        var_0 = module_0.check_required_together(str_0, str_1)
        list_0 = [str_1, str_1, str_1]
        var_1 = module_0.check_type_dict(list_0)
    except BaseException:
        pass

def test_case_24():
    try:
        float_0 = 3076.7119
        var_0 = module_0.check_type_list(float_0)
        bytes_0 = b'\x04\x1a\xb9;H\x92\xda\xdc\x15\xe5\xde'
        var_1 = module_0.check_type_float(bytes_0)
    except BaseException:
        pass

def test_case_25():
    try:
        dict_0 = {}
        int_0 = 1900
        var_0 = module_0.check_mutually_exclusive(dict_0, int_0)
        tuple_0 = None
        var_1 = module_0.check_type_int(tuple_0)
    except BaseException:
        pass

def test_case_26():
    try:
        float_0 = 3076.7119
        var_0 = module_0.check_type_list(float_0)
        bytes_0 = b'\x04\x1a\xb9;H\x92\xda\xdc\x15\xe5\xde'
        str_0 = None
        dict_0 = {str_0: str_0, str_0: str_0}
        var_1 = module_0.check_mutually_exclusive(str_0, dict_0)
        var_2 = module_0.check_type_float(bytes_0)
    except BaseException:
        pass

def test_case_27():
    try:
        set_0 = set()
        bool_0 = False
        var_0 = module_0.check_required_one_of(set_0, bool_0)
        bytes_0 = b'\x05\xa9\x90\xc2\xfe`\x11\x00p\xf6\xc5\xbe\x12\xb3\xcc\xdb\x00\xb9!'
        var_1 = module_0.check_missing_parameters(bytes_0)
        str_0 = 'True'
        var_2 = module_0.safe_eval(str_0)
        float_0 = -2746.7
        set_1 = {float_0, float_0, var_2}
        var_3 = module_0.check_type_bits(set_1)
    except BaseException:
        pass

def test_case_28():
    try:
        set_0 = None
        float_0 = 1941.7
        var_0 = module_0.check_required_if(set_0, float_0)
        list_0 = None
        var_1 = module_0.check_type_bytes(list_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = '/I5\\N+WP/B'
        var_0 = module_0.check_type_bits(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = '\\H|>\x0bs>8]\x0bj=lWX\n=p='
        float_0 = None
        dict_0 = {float_0: str_0, float_0: str_0, str_0: float_0}
        var_0 = module_0.check_required_by(float_0, dict_0)
        str_1 = ' -\r\r}VX@u'
        set_0 = {str_1, str_0}
        dict_1 = {str_1: set_0, str_1: str_0, str_0: str_0}
        int_0 = 2541
        var_1 = module_0.check_required_by(dict_1, int_0, dict_1)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'p\x0c@FHdMfi[PS]C*Ktut'
        str_1 = 'P1\x0cUc-y'
        list_0 = [str_0, str_0, str_1, str_0]
        var_0 = module_0.check_type_list(list_0)
        tuple_0 = (str_0,)
        int_0 = 0
        bytes_0 = b'\xc0tX\x80\xab\xa3\xe4\xd6 \xe3}\xb8'
        var_1 = module_0.check_mutually_exclusive(tuple_0, int_0, bytes_0)
    except BaseException:
        pass

def test_case_32():
    try:
        float_0 = -833.445
        var_0 = module_0.check_type_bool(float_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = '3"Q<+tECVM'
        bool_0 = True
        list_0 = [str_0, str_0, bool_0, bool_0]
        bytes_0 = b'(%F'
        int_0 = -920
        var_0 = module_0.safe_eval(int_0, list_0, bytes_0)
        bool_1 = True
        var_1 = module_0.check_type_float(bool_1)
        str_1 = 'v'
        var_2 = module_0.check_type_bytes(str_1)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = 'a'
        str_1 = '1'
        str_2 = {str_0: str_1}
        str_3 = [str_0]
        var_0 = module_0.check_missing_parameters(str_2, str_3)
        str_4 = 'a'
        str_5 = '1'
        str_6 = {str_4: str_5}
        str_7 = 'c'
        str_8 = [str_7]
        var_1 = module_0.check_missing_parameters(str_6, str_8)
    except BaseException:
        pass

def test_case_35():
    try:
        float_0 = 4705.0635
        var_0 = module_0.check_type_float(float_0)
        bytes_0 = b'\x15Z\x12i\xb5K__\xdd\xf6#F/'
        var_1 = module_0.check_type_dict(bytes_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = '\\H|>\x0bs>8]\x0bj=lWX\n=p='
        set_0 = {str_0, str_0}
        dict_0 = {str_0: set_0, str_0: str_0, str_0: str_0}
        int_0 = 2541
        var_0 = module_0.check_required_by(dict_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = '{0} must be installed and visible from {1}.'
        str_1 = '.*z~'
        set_0 = {str_1, str_1}
        var_0 = module_0.check_required_together(set_0, str_0)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'present'
        str_1 = (str_0,)
        bool_0 = False
        str_2 = (str_1,)
        var_0 = [str_1, str_0, str_2, bool_0]
        str_3 = (str_0,)
        var_1 = [str_3, str_2, str_3, bool_0]
        var_2 = [var_0, var_1]
        str_4 = {str_1: str_0}
        var_3 = module_0.check_required_if(var_2, str_4)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = "1fB'H,P4\x0be9{s[9-6"
        bytes_0 = None
        tuple_0 = (str_0, bytes_0, bytes_0)
        var_0 = module_0.check_required_one_of(tuple_0, tuple_0)
        dict_0 = {}
        var_1 = module_0.check_type_path(dict_0)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'D'
        var_0 = module_0.check_type_jsonarg(str_0)
        str_1 = 'Io\x0cPKT31BB<B]{-654c\\'
        str_2 = '59j\r]cApZ;S^f<'
        str_3 = ';i?'
        list_0 = [str_1, str_2, str_2]
        bytes_0 = b'M\xf4p\\'
        var_1 = module_0.check_required_one_of(str_3, list_0, bytes_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'presenA4t'
        str_1 = (str_0,)
        bool_0 = True
        str_2 = (str_1,)
        var_0 = [str_1, str_0, str_2, bool_0]
        str_3 = (str_0,)
        var_1 = [str_3, str_2, str_3, bool_0]
        var_2 = [var_0, var_1]
        str_4 = {str_1: str_0}
        var_3 = module_0.check_required_if(var_2, str_4)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'param1'
        str_1 = 'param2'
        str_2 = [str_0, str_1]
        str_3 = 'param3'
        str_4 = [str_3, str_3]
        str_5 = [str_2, str_4]
        bool_0 = {}
        var_0 = module_0.check_mutually_exclusive(str_5, bool_0)
        bool_1 = {str_0: bool_0, str_1: bool_0, str_3: bool_0}
        var_1 = module_0.check_mutually_exclusive(str_5, bool_1)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'a'
        str_1 = 'b'
        str_2 = [str_0, str_1]
        str_3 = [str_0, str_0]
        str_4 = [str_2, str_3]
        int_0 = 1
        var_0 = dict(a=int_0)
        str_5 = 'parent1'
        str_6 = 'parent2'
        str_7 = [str_5, str_6]
        var_1 = module_0.check_required_together(str_4, var_0, str_7)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'foo'
        str_1 = 'quIx'
        str_2 = {str_1: str_0, str_0: str_1}
        var_0 = None
        var_1 = {str_0: str_2, str_0: str_2, str_1: var_0}
        var_2 = module_0.check_required_by(str_2, var_1)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'bar'
        str_1 = 'required'
        bool_0 = True
        bool_1 = {str_1: bool_0}
        bool_2 = True
        bool_3 = {str_1: bool_2}
        bool_4 = {str_1: bool_1, str_0: bool_3}
        var_0 = module_0.check_required_arguments(bool_4, bool_1)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = 'foo'
        str_1 = 'iBs"WLpS.F\x0b!=%'
        str_2 = '--with-fingerprint'
        dict_0 = {str_2: str_2, str_2: str_0}
        var_0 = module_0.check_type_path(str_2)
        var_1 = module_0.check_type_dict(dict_0)
        str_3 = [str_2, str_1]
        str_4 = 'quux'
        str_5 = {str_0: str_0, str_0: str_3, str_1: str_4}
        str_6 = ''
        var_2 = module_0.check_required_by(str_5, str_2)
        list_0 = [str_6]
        var_3 = module_0.check_type_bits(list_0)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'foo'
        str_1 = '\n'
        str_2 = [str_0, str_1]
        set_0 = set()
        bool_0 = False
        var_0 = module_0.check_required_if(str_2, set_0, bool_0)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = 'a=b'
        var_0 = module_0.check_type_dict(str_0)
        str_1 = '`a=b, c=d'
        var_1 = module_0.check_type_dict(str_1)
        str_2 = 'l$A}i_fVf'
        str_3 = '1Tb'
        dict_0 = {str_3: str_0, str_1: var_1, str_1: str_1, str_3: str_2}
        var_2 = module_0.check_type_bits(dict_0)
    except BaseException:
        pass

def test_case_49():
    try:
        str_0 = 'state'
        str_1 = 'present'
        str_2 = 'absent'
        bool_0 = False
        str_3 = (str_2,)
        var_0 = [str_0, str_1, str_3, bool_0]
        str_4 = (str_1,)
        var_1 = [str_0, str_2, str_4, bool_0]
        var_2 = [var_0, var_1]
        str_5 = {str_0: str_2}
        var_3 = module_0.check_required_if(var_2, str_5)
    except BaseException:
        pass

def test_case_50():
    try:
        str_0 = 'a'
        str_1 = 'c'
        str_2 = 'b'
        str_3 = 'd'
        str_4 = {str_0: str_2, str_1: str_3}
        bool_0 = True
        bool_1 = {str_0: bool_0, str_1: bool_0}
        var_0 = module_0.check_required_by(str_4, bool_1)
    except BaseException:
        pass