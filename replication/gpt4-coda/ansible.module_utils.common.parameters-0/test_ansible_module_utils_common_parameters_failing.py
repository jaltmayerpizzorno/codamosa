# Automatically generated by Pynguin.
import ansible.module_utils.common.parameters as module_0

def test_case_0():
    try:
        str_0 = '8pB*Kgt\\?'
        int_0 = 1229
        tuple_0 = (int_0,)
        str_1 = ']u+\\k`'
        dict_0 = {str_0: str_1}
        var_0 = module_0.remove_values(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.env_fallback()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x94Y\xc1\xe4\xbd\x93\xfa\x91'
        list_0 = [bytes_0]
        var_0 = module_0.remove_values(bytes_0, list_0)
        dict_0 = {}
        var_1 = module_0.env_fallback(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        set_0 = set()
        var_0 = module_0.set_fallbacks(str_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '@X"\tt\\)'
        str_1 = None
        float_0 = 412.303
        dict_0 = {str_0: str_0, str_1: str_1, str_1: float_0, str_1: float_0}
        list_0 = [str_0, dict_0]
        var_0 = module_0.remove_values(dict_0, list_0)
        var_1 = module_0.sanitize_keys(list_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'q`Z5`'
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.remove_values(str_0, list_0)
        dict_0 = {str_0: str_0}
        bytes_0 = b'm\x8f\x85\xa7\x86@\x84<\xda'
        var_1 = module_0.sanitize_keys(dict_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b''
        set_0 = set()
        str_0 = ''
        list_0 = [str_0, bytes_0, set_0]
        var_0 = module_0.env_fallback(*list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b''
        set_0 = set()
        var_0 = module_0.sanitize_keys(bytes_0, set_0)
        dict_0 = {bytes_0: set_0}
        tuple_0 = (dict_0,)
        str_0 = 'duplicate loop in task: %s'
        var_1 = module_0.sanitize_keys(tuple_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '8pB*Kgt\\?'
        complex_0 = None
        list_0 = [complex_0]
        int_0 = 1229
        tuple_0 = (int_0,)
        str_1 = ']u+\\k`'
        dict_0 = {str_0: str_1}
        var_0 = module_0.remove_values(tuple_0, dict_0)
        var_1 = module_0.remove_values(complex_0, list_0)
        dict_1 = {str_1: var_0, str_1: dict_0, var_1: list_0}
        list_1 = []
        var_2 = module_0.set_fallbacks(dict_1, list_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '8pB*Kgt\\?'
        int_0 = 396
        str_1 = ")k'M\\c6iu5Va5GBs>"
        var_0 = module_0.remove_values(int_0, str_1)
        complex_0 = None
        list_0 = [complex_0]
        int_1 = 1229
        tuple_0 = (int_1,)
        str_2 = ']u+\\k`'
        dict_0 = {str_0: str_2}
        var_1 = module_0.remove_values(tuple_0, dict_0)
        var_2 = module_0.remove_values(complex_0, list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '8lPt\x0c<\\0mM=0&c6Z,X'
        str_1 = 't=r`'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_1}
        list_0 = [dict_0, str_0, str_1]
        str_2 = 'X z\tobZ}l&'
        var_0 = module_0.remove_values(list_0, str_2)
        var_1 = module_0.env_fallback(**dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'\x94Y\xc1\xe4\xbd\x93\xfa\x91'
        list_0 = [bytes_0, bytes_0]
        var_0 = module_0.remove_values(bytes_0, bytes_0)
        float_0 = 2702.238
        str_0 = '\nname: url\nauthor: Brian Coca (@bcoca)\nversion_added: "1.9"\nshort_description: return contents from URL\ndescription:\n    - Returns the content of the URL requested to be used as data in play.\noptions:\n  _terms:\n    description: urls to query\n  validate_certs:\n    description: Flag to control SSL certificate validation\n    type: boolean\n    default: True\n  split_lines:\n    description: Flag to control if content is returned as a list of lines or as a single text blob\n    type: boolean\n    default: True\n  use_proxy:\n    description: Flag to control if the lookup will observe HTTP proxy environment variables when present.\n    type: boolean\n    default: True\n  username:\n    description: Username to use for HTTP authentication.\n    type: string\n    version_added: "2.8"\n  password:\n    description: Password to use for HTTP authentication.\n    type: string\n    version_added: "2.8"\n  headers:\n    description: HTTP request headers\n    type: dictionary\n    default: {}\n    version_added: "2.9"\n  force:\n    description: Whether or not to set "cache-control" header with value "no-cache"\n    type: boolean\n    version_added: "2.10"\n    default: False\n    vars:\n        - name: ansible_lookup_url_force\n    env:\n        - name: ANSIBLE_LOOKUP_URL_FORCE\n    ini:\n        - section: url_lookup\n          key: force\n  timeout:\n    description: How long to wait for the server to send data before giving up\n    type: float\n    version_added: "2.10"\n    default: 10\n    vars:\n        - name: ansible_lookup_url_timeout\n    env:\n        - name: ANSIBLE_LOOKUP_URL_TIMEOUT\n    ini:\n        - section: url_lookup\n          key: timeout\n  http_agent:\n    description: User-Agent to use in the request. The default was changed in 2.11 to C(ansible-httpget).\n    type: string\n    version_added: "2.10"\n    default: ansible-httpget\n    vars:\n        - name: ansible_lookup_url_agent\n    env:\n        - name: ANSIBLE_LOOKUP_URL_AGENT\n    ini:\n        - section: url_lookup\n          key: agent\n  force_basic_auth:\n    description: Force basic authentication\n    type: boolean\n    version_added: "2.10"\n    default: False\n    vars:\n        - name: ansible_lookup_url_agent\n    env:\n        - name: ANSIBLE_LOOKUP_URL_AGENT\n    ini:\n        - section: url_lookup\n          key: agent\n  follow_redirects:\n    description: String of urllib2, all/yes, safe, none to determine how redirects are followed, see RedirectHandlerFactory for more information\n    type: string\n    version_added: "2.10"\n    default: \'urllib2\'\n    vars:\n        - name: ansible_lookup_url_follow_redirects\n    env:\n        - name: ANSIBLE_LOOKUP_URL_FOLLOW_REDIRECTS\n    ini:\n        - section: url_lookup\n          key: follow_redirects\n  use_gssapi:\n    description:\n    - Use GSSAPI handler of requests\n    - As of Ansible 2.11, GSSAPI credentials can be specified with I(username) and I(password).\n    type: boolean\n    version_added: "2.10"\n    default: False\n    vars:\n        - name: ansible_lookup_url_use_gssapi\n    env:\n        - name: ANSIBLE_LOOKUP_URL_USE_GSSAPI\n    ini:\n        - section: url_lookup\n          key: use_gssapi\n  unix_socket:\n    description: String of file system path to unix socket file to use when establishing connection to the provided url\n    type: string\n    version_added: "2.10"\n    vars:\n        - name: ansible_lookup_url_unix_socket\n    env:\n        - name: ANSIBLE_LOOKUP_URL_UNIX_SOCKET\n    ini:\n        - section: url_lookup\n          key: unix_socket\n  ca_path:\n    description: String of file system path to CA cert bundle to use\n    type: string\n    version_added: "2.10"\n    vars:\n        - name: ansible_lookup_url_ca_path\n    env:\n        - name: ANSIBLE_LOOKUP_URL_CA_PATH\n    ini:\n        - section: url_lookup\n          key: ca_path\n  unredirected_headers:\n    description: A list of headers to not attach on a redirected request\n    type: list\n    version_added: "2.10"\n    vars:\n        - name: ansible_lookup_url_unredir_headers\n    env:\n        - name: ANSIBLE_LOOKUP_URL_UNREDIR_HEADERS\n    ini:\n        - section: url_lookup\n          key: unredirected_headers\n'
        str_1 = 'VREo^{$+s4q(ybF'
        dict_0 = {str_1: str_0, str_0: str_1}
        var_1 = module_0.sanitize_keys(dict_0, dict_0, dict_0)
        tuple_0 = (float_0, str_0)
        var_2 = module_0.remove_values(tuple_0, list_0)
        int_0 = -1872
        var_3 = module_0.sanitize_keys(float_0, int_0)
    except BaseException:
        pass