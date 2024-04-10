# Automatically generated by Pynguin.
import ansible.collections.list as module_0

def test_case_0():
    try:
        var_0 = module_0.list_collection_dirs()
        var_1 = set(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = []
        var_1 = module_0.list_collection_dirs(var_0)
        var_2 = set(var_1)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = []
        var_1 = module_0.list_collection_dirs(var_0, var_0)
        var_2 = set(var_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ansible_collections.testcoll'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\nname: url\nauthor: Brian Coca (@bcoca)\nversion_added: "1.9"\nshort_description: return contents from URL\ndescription:\n    - Returns the content of the URL requested to be used as data in play.\noptions:\n  _terms:\n    description: urls to query\n  validate_certs:\n    description: Flag to control SSL certificate validation\n    type: boolean\n    default: True\n  split_lines:\n    description: Flag to control if content is returned as a list of lines or as a single text blob\n    type: boolean\n    default: True\n  use_proxy:\n    description: Flag to control if the lookup will observe HTTP proxy environment variables when present.\n    type: boolean\n    default: True\n  username:\n    description: Username to use for HTTP authentication.\n    type: string\n    version_added: "2.8"\n  password:\n    description: Password to use for HTTP authentication.\n    type: string\n    version_added: "2.8"\n  headers:\n    description: HTTP request headers\n    type: dictionary\n    default: {}\n    version_added: "2.9"\n  force:\n    description: Whether or not to set "cache-control" header with value "no-cache"\n    type: boolean\n    version_added: "2.10"\n    default: False\n    vars:\n        - name: ansible_lookup_url_force\n    env:\n        - name: ANSIBLE_LOOKUP_URL_FORCE\n    ini:\n        - section: url_lookup\n          key: force\n  timeout:\n    description: How long to wait for the server to send data before giving up\n    type: float\n    version_added: "2.10"\n    default: 10\n    vars:\n        - name: ansible_lookup_url_timeout\n    env:\n        - name: ANSIBLE_LOOKUP_URL_TIMEOUT\n    ini:\n        - section: url_lookup\n          key: timeout\n  http_agent:\n    description: User-Agent to use in the request. The default was changed in 2.11 to C(ansible-httpget).\n    type: string\n    version_added: "2.10"\n    default: ansible-httpget\n    vars:\n        - name: ansible_lookup_url_agent\n    env:\n        - name: ANSIBLE_LOOKUP_URL_AGENT\n    ini:\n        - section: url_lookup\n          key: agent\n  force_basic_auth:\n    description: Force basic authentication\n    type: boolean\n    version_added: "2.10"\n    default: False\n    vars:\n        - name: ansible_lookup_url_agent\n    env:\n        - name: ANSIBLE_LOOKUP_URL_AGENT\n    ini:\n        - section: url_lookup\n          key: agent\n  follow_redirects:\n    description: String of urllib2, all/yes, safe, none to determine how redirects are followed, see RedirectHandlerFactory for more information\n    type: string\n    version_added: "2.10"\n    default: \'urllib2\'\n    vars:\n        - name: ansible_lookup_url_follow_redirects\n    env:\n        - name: ANSIBLE_LOOKUP_URL_FOLLOW_REDIRECTS\n    ini:\n        - section: url_lookup\n          key: follow_redirects\n  use_gssapi:\n    description:\n    - Use GSSAPI handler of requests\n    - As of Ansible 2.11, GSSAPI credentials can be specified with I(username) and I(password).\n    type: boolean\n    version_added: "2.10"\n    default: False\n    vars:\n        - name: ansible_lookup_url_use_gssapi\n    env:\n        - name: ANSIBLE_LOOKUP_URL_USE_GSSAPI\n    ini:\n        - section: url_lookup\n          key: use_gssapi\n  unix_socket:\n    description: String of file system path to unix socket file to use when establishing connection to the provided url\n    type: string\n    version_added: "2.10"\n    vars:\n        - name: ansible_lookup_url_unix_socket\n    env:\n        - name: ANSIBLE_LOOKUP_URL_UNIX_SOCKET\n    ini:\n        - section: url_lookup\n          key: unix_socket\n  ca_path:\n    description: String of file system path to CA cert bundle to use\n    type: string\n    version_added: "2.10"\n    vars:\n        - name: ansible_lookup_url_ca_path\n    env:\n        - name: ANSIBLE_LOOKUP_URL_CA_PATH\n    ini:\n        - section: url_lookup\n          key: ca_path\n  unredirected_headers:\n    description: A list of headers to not attach on a redirected request\n    type: list\n    version_added: "2.10"\n    vars:\n        - name: ansible_lookup_url_unredir_headers\n    env:\n        - name: ANSIBLE_LOOKUP_URL_UNREDIR_HEADERS\n    ini:\n        - section: url_lookup\n          key: unredirected_headers\n'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass