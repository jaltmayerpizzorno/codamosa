# Automatically generated by Pynguin.
import ansible.vars.plugins as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    tuple_0 = ()
    str_0 = "Matching according to RFC 6125, section 6.4.3\n\n        - Hostnames are compared lower case.\n        - For IDNA, both dn and hostname must be encoded as IDN A-label (ACE).\n        - Partial wildcards like 'www*.example.org', multiple wildcards, sole\n          wildcard or wildcards in labels other then the left-most label are not\n          supported and a CertificateError is raised.\n        - A wildcard must match at least one character.\n        "
    float_0 = -1563.251644
    var_0 = module_0.get_vars_from_inventory_sources(tuple_0, str_0, list_0, float_0)
    var_1 = module_0.get_vars_from_inventory_sources(str_0, list_0, list_0, float_0)

def test_case_2():
    float_0 = -2146.0
    set_0 = set()
    var_0 = module_0.get_plugin_vars(float_0, set_0, float_0, set_0)

def test_case_3():
    float_0 = None
    str_0 = 'inventory'
    var_0 = module_0.get_vars_from_path(float_0, str_0, float_0, str_0)