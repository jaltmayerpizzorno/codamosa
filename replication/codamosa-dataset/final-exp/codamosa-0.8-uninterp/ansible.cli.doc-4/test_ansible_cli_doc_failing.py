# Automatically generated by Pynguin.
import ansible.cli.doc as module_0

def test_case_0():
    try:
        int_0 = 123
        doc_c_l_i_0 = module_0.DocCLI(int_0)
        var_0 = module_0.jdump(doc_c_l_i_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        float_0 = 128.2776
        doc_c_l_i_0 = module_0.DocCLI(float_0)
        var_0 = doc_c_l_i_0.display_plugin_list(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_mixin_0 = module_0.RoleMixin()
        set_0 = {role_mixin_0}
        list_0 = [set_0]
        float_0 = -2207.84857
        doc_c_l_i_0 = module_0.DocCLI(float_0)
        doc_c_l_i_1 = module_0.DocCLI(doc_c_l_i_0)
        var_0 = doc_c_l_i_1.get_all_plugins_of_type(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        plugin_not_found_0 = module_0.PluginNotFound()
        str_0 = '-o StrictHostKeyChecking=no'
        doc_c_l_i_0 = module_0.DocCLI(str_0)
        role_mixin_0 = module_0.RoleMixin()
        role_mixin_1 = None
        var_0 = doc_c_l_i_0.get_plugin_metadata(role_mixin_1, doc_c_l_i_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        str_0 = 'EK'
        float_0 = 100.0
        float_1 = -839.14
        doc_c_l_i_0 = module_0.DocCLI(float_1)
        var_0 = doc_c_l_i_0.find_plugins(bool_0, str_0, float_0)
        str_1 = ';nve+tory'
        int_0 = -1376
        str_2 = '___?ioBuluU/'
        var_1 = doc_c_l_i_0.namespace_from_plugin_filepath(str_1, int_0, str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -19
        str_0 = 'keyword'
        role_mixin_0 = module_0.RoleMixin()
        doc_c_l_i_0 = module_0.DocCLI(role_mixin_0)
        var_0 = doc_c_l_i_0.format_snippet(int_0, str_0, doc_c_l_i_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1336
        str_0 = "R=&CCg'\x0c$o\n"
        tuple_0 = (str_0,)
        dict_0 = {}
        str_1 = 'm2O'
        str_2 = "Failed to set {3} to '{2}': {0} {1}"
        dict_1 = {str_1: str_1, str_1: str_1, str_2: str_1}
        doc_c_l_i_0 = module_0.DocCLI(dict_1)
        var_0 = doc_c_l_i_0.add_fields(int_0, int_0, tuple_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        int_0 = -4363
        complex_0 = None
        str_0 = '\x0cq5VvY?UV#`L'
        str_1 = 'module'
        str_2 = 'LzAczOe/hv'
        dict_1 = {str_0: complex_0, str_1: dict_0, str_2: int_0, str_2: str_2}
        str_3 = '!\tM3 -u*t\x0cK@e /'
        float_0 = -2044.767428
        list_0 = [float_0]
        tuple_0 = (str_3, float_0, list_0, float_0)
        doc_c_l_i_0 = module_0.DocCLI(tuple_0)
        var_0 = doc_c_l_i_0.add_fields(bool_0, dict_0, int_0, complex_0, dict_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '1^2SDU{x7<'
        role_mixin_0 = module_0.RoleMixin()
        list_0 = [str_0, role_mixin_0, role_mixin_0]
        str_1 = 'python-apt'
        doc_c_l_i_0 = module_0.DocCLI(str_1)
        var_0 = doc_c_l_i_0.get_role_man_text(list_0, role_mixin_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -2652.3339
        bytes_0 = None
        list_0 = [bytes_0, bytes_0]
        doc_c_l_i_0 = module_0.DocCLI(list_0)
        doc_c_l_i_1 = module_0.DocCLI(doc_c_l_i_0)
        var_0 = doc_c_l_i_1.get_man_text(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 60.0
        list_0 = [float_0, float_0, float_0, float_0]
        str_0 = 'q~Sj}'
        str_1 = "Ifnk\x0b04'*"
        str_2 = 'b'
        dict_0 = {str_0: list_0, str_1: list_0, str_2: float_0}
        set_0 = {float_0, str_0, str_0, str_0}
        list_1 = [list_0]
        doc_c_l_i_0 = module_0.DocCLI(list_1)
        var_0 = doc_c_l_i_0.get_man_text(dict_0, set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '{mA)b\tga3?yM'
        str_1 = '-%vJGXW\x0cv-6An"'
        doc_c_l_i_0 = module_0.DocCLI(str_1)
        var_0 = doc_c_l_i_0.run()
        plugin_not_found_0 = module_0.PluginNotFound()
        set_0 = {doc_c_l_i_0, str_0}
        doc_c_l_i_1 = module_0.DocCLI(set_0)
        role_mixin_0 = module_0.RoleMixin()
        bool_0 = False
        bool_1 = False
        dict_0 = {var_0: var_0, bool_1: doc_c_l_i_1, doc_c_l_i_1: bool_0}
        int_0 = -357
        bytes_0 = b'f5\xc7\x14\xc4\x8chf\xd0X8\xc9\xbe\xa4\xef\xfc\xeb\xd5\xe6'
        int_1 = 440
        list_0 = [dict_0]
        var_1 = doc_c_l_i_1.format_plugin_doc(plugin_not_found_0, dict_0, int_0, bytes_0, int_1, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = True
        doc_c_l_i_0 = module_0.DocCLI(bool_0)
        str_0 = '-%vJGXW\x0cv-6A9"'
        doc_c_l_i_1 = module_0.DocCLI(str_0)
        var_0 = doc_c_l_i_1.run()
        plugin_not_found_0 = module_0.PluginNotFound()
        set_0 = {doc_c_l_i_1, str_0}
        doc_c_l_i_2 = module_0.DocCLI(set_0)
        role_mixin_0 = module_0.RoleMixin()
        str_1 = None
        var_1 = doc_c_l_i_2.namespace_from_plugin_filepath(plugin_not_found_0, str_1, str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = None
        bool_0 = True
        doc_c_l_i_0 = module_0.DocCLI(bool_0)
        list_0 = None
        tuple_0 = (list_0,)
        var_0 = doc_c_l_i_0.find_plugins(bool_0, dict_0, tuple_0)
        str_0 = '\x0c8"kir'
        role_mixin_0 = module_0.RoleMixin()
        doc_c_l_i_1 = module_0.DocCLI(str_0)
        plugin_not_found_0 = module_0.PluginNotFound()
        set_0 = {doc_c_l_i_1, str_0}
        doc_c_l_i_2 = module_0.DocCLI(set_0)
        bytes_0 = b'\x1eH^Np}\x80\xd7\xd1\x1d'
        dict_1 = {str_0: var_0}
        set_1 = None
        var_1 = doc_c_l_i_1.add_fields(bytes_0, dict_1, set_1, bytes_0, doc_c_l_i_2, dict_1)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        doc_c_l_i_0 = None
        float_0 = 3476.765
        doc_c_l_i_1 = module_0.DocCLI(float_0)
        var_0 = doc_c_l_i_1.get_man_text(list_0, doc_c_l_i_0)
    except BaseException:
        pass