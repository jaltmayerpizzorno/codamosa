# Automatically generated by Pynguin.
import ansible.plugins.filter.urlsplit as module_0

def test_case_0():
    float_0 = None
    var_0 = module_0.split_url(float_0)

def test_case_1():
    str_0 = 'https://www.example.com:8080/foo/bar?hello=world%20with%20spaces&foo=bar'
    str_1 = 'netloc'
    var_0 = module_0.split_url(str_0, str_1)