# Automatically generated by Pynguin.
import ansible.utils.version as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    try:
        tuple_0 = ()
        int_0 = 73
        float_0 = -3335.9
        bytes_0 = b"\xc8\xda\xbd'"
        alpha_0 = module_0._Alpha(bytes_0)
        var_0 = alpha_0.__eq__(float_0)
        alpha_1 = module_0._Alpha(int_0)
        var_1 = alpha_1.__lt__(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '0.1.2'
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        var_0 = semantic_version_1.__eq__(semantic_version_0)
        semantic_version_2 = module_0.SemanticVersion()
        bytes_0 = b'\xb9Nw#)f\xce'
        tuple_0 = (semantic_version_2, bytes_0)
        alpha_0 = module_0._Alpha(tuple_0)
        var_1 = alpha_0.__ne__(semantic_version_0)
        loose_version_0 = module_1.LooseVersion(str_0)
        var_2 = semantic_version_1.from_loose_version(loose_version_0)
        semantic_version_3 = module_0.SemanticVersion()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        set_0 = set()
        set_1 = {bool_0, bool_0}
        alpha_0 = module_0._Alpha(set_1)
        var_0 = alpha_0.__ge__(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        alpha_0 = None
        tuple_0 = (alpha_0,)
        tuple_1 = (tuple_0, tuple_0)
        dict_0 = {}
        int_0 = 6
        numeric_0 = module_0._Numeric(int_0)
        alpha_1 = module_0._Alpha(dict_0)
        var_0 = alpha_1.__gt__(tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        complex_0 = None
        list_0 = None
        float_0 = 200.302
        numeric_0 = module_0._Numeric(float_0)
        float_1 = 2120.0
        numeric_1 = module_0._Numeric(float_1)
        var_0 = numeric_1.__ne__(numeric_0)
        tuple_0 = (complex_0, list_0)
        float_2 = -2373.49392
        numeric_2 = module_0._Numeric(float_2)
        alpha_0 = module_0._Alpha(tuple_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.parse(semantic_version_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 81
        numeric_0 = module_0._Numeric(int_0)
        var_0 = numeric_0.__repr__()
        bool_0 = True
        var_1 = numeric_0.__gt__(bool_0)
        bool_1 = True
        alpha_0 = None
        var_2 = numeric_0.__ne__(alpha_0)
        list_0 = [bool_1]
        var_3 = numeric_0.__ne__(list_0)
        bool_2 = True
        numeric_1 = module_0._Numeric(bool_2)
        var_4 = numeric_1.__lt__(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__repr__()
        str_0 = 'EAg~@%04J}\r)^t'
        str_1 = '&R-(Jh>gZYL4\rg``P$0m'
        int_0 = 302
        tuple_0 = (str_0, str_1, int_0)
        numeric_0 = module_0._Numeric(int_0)
        var_1 = numeric_0.__le__(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '.RMZ\r*E>f_|ne[^S6nl-'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__eq__(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__ge__(semantic_version_0)
        bytes_0 = None
        var_1 = semantic_version_0.from_loose_version(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 81
        numeric_0 = module_0._Numeric(int_0)
        var_0 = numeric_0.__repr__()
        bool_0 = True
        var_1 = numeric_0.__gt__(bool_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_2 = numeric_0.__eq__(semantic_version_0)
        semantic_version_1 = module_0.SemanticVersion()
        list_0 = [int_0]
        var_3 = semantic_version_1.__ne__(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 0.2
        dict_0 = {float_0: float_0}
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__lt__(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = 159.6152
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__le__(float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 699
        alpha_0 = module_0._Alpha(int_0)
        str_0 = 'i,2rg\\2G&b0v!b'
        list_0 = []
        semantic_version_0 = module_0.SemanticVersion(list_0)
        var_0 = semantic_version_0.__gt__(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 81
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__repr__()
        numeric_0 = module_0._Numeric(int_0)
        var_1 = numeric_0.__repr__()
        var_2 = numeric_0.__ge__(numeric_0)
        bool_0 = True
        var_3 = numeric_0.__gt__(bool_0)
        bool_1 = False
        str_0 = 'G0,Oqh3\t@'
        semantic_version_1 = module_0.SemanticVersion()
        var_4 = numeric_0.__eq__(semantic_version_1)
        alpha_0 = module_0._Alpha(str_0)
        var_5 = alpha_0.__gt__(bool_1)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = 81
        numeric_0 = module_0._Numeric(int_0)
        bool_0 = True
        var_0 = numeric_0.__gt__(bool_0)
        str_0 = '}s\n*2)qr'
        var_1 = numeric_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = 820.81
        alpha_0 = module_0._Alpha(float_0)
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        var_0 = alpha_0.__lt__(numeric_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.from_loose_version(semantic_version_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 699
        alpha_0 = module_0._Alpha(int_0)
        var_0 = alpha_0.__gt__(alpha_0)
        bytes_0 = b'aeldlI\x96)\xb2\xe3\xa7\xa41\xc9^~'
        semantic_version_0 = module_0.SemanticVersion(bytes_0)
    except BaseException:
        pass

def test_case_17():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__ge__(semantic_version_0)
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        var_1 = numeric_0.__repr__()
        int_0 = -999
        str_0 = 'uRq|pb9B}<u8;'
        alpha_0 = module_0._Alpha(str_0)
        var_2 = numeric_0.__ge__(alpha_0)
        float_0 = -561.26419
        numeric_1 = module_0._Numeric(float_0)
        var_3 = numeric_1.__gt__(int_0)
        var_4 = semantic_version_0.__repr__()
        set_0 = set()
        var_5 = semantic_version_0.from_loose_version(set_0)
    except BaseException:
        pass

def test_case_18():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__ge__(semantic_version_0)
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        var_1 = numeric_0.__repr__()
        int_0 = 134
        float_0 = -561.26419
        numeric_1 = module_0._Numeric(float_0)
        var_2 = numeric_1.__gt__(int_0)
        var_3 = semantic_version_0.__repr__()
        set_0 = set()
        var_4 = semantic_version_0.from_loose_version(set_0)
    except BaseException:
        pass

def test_case_19():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        loose_version_0 = module_1.LooseVersion()
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bytes_0 = b'\xa2\x0e\xee\xa4\x1c\xb5\x0c'
        str_0 = 'qi*_n>zj~,&\x0c2DKW_'
        str_1 = 'Extract FQCN from the given on-disk collection artifact.\n\n        If the collection is virtual, ``None`` is returned instead\n        of a string.\n        '
        alpha_0 = module_0._Alpha(str_1)
        alpha_1 = module_0._Alpha(alpha_0)
        var_0 = alpha_1.__le__(str_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.__lt__(bytes_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = '0.1.2'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__eq__(semantic_version_0)
        var_1 = semantic_version_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        str_0 = ';W'
        loose_version_0 = module_1.LooseVersion(str_0)
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '..'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__eq__(semantic_version_0)
        loose_version_0 = module_1.LooseVersion(str_0)
        var_1 = semantic_version_0.from_loose_version(loose_version_0)
        dict_0 = None
        set_0 = {dict_0}
        var_2 = semantic_version_0.from_loose_version(set_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '+sx$TR72.eI*2'
        semantic_version_0 = module_0.SemanticVersion()
        loose_version_0 = module_1.LooseVersion(str_0)
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '\n---\nauthor: Ansible Core Team (@ansible)\nmodule: import_playbook\nshort_description: Import a playbook\ndescription:\n  - Includes a file with a list of plays to be executed.\n  - Files with a list of plays can only be included at the top level.\n  - You cannot use this action inside a play.\nversion_added: "2.4"\noptions:\n  free-form:\n    description:\n      - The name of the imported playbook is specified directly without any other option.\nextends_documentation_fragment:\n  - action_common_attributes\n  - action_common_attributes.conn\n  - action_common_attributes.flow\n  - action_core\n  - action_core.import\nattributes:\n    check_mode:\n        support: full\n    diff_mode:\n        support: none\n    platform:\n        platforms: all\nnotes:\n  - This is a core feature of Ansible, rather than a module, and cannot be overridden like a module.\nseealso:\n- module: ansible.builtin.import_role\n- module: ansible.builtin.import_tasks\n- module: ansible.builtin.include_role\n- module: ansible.builtin.include_tasks\n- ref: playbooks_reuse_includes\n  description: More information related to including and importing playbooks, roles and tasks.\n'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__eq__(semantic_version_0)
        loose_version_0 = module_1.LooseVersion(str_0)
        var_1 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass