# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    try:
        var_0 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        bytes_0 = None
        plugin_load_context_0 = module_0.PluginLoadContext()
        int_1 = 2542
        str_0 = '# \\(/tmp/.*installed on.*\\)'
        str_1 = 'board_version'
        dict_0 = {str_0: int_1, str_1: int_1}
        list_0 = [bytes_0, int_0, str_1]
        set_0 = {int_0, str_1, str_1}
        tuple_0 = (set_0, set_0)
        list_1 = [str_0, int_1, bytes_0]
        plugin_path_context_0 = module_0.PluginPathContext(tuple_0, list_1)
        var_0 = plugin_load_context_0.resolve(int_1, dict_0, list_0, plugin_path_context_0)
        var_1 = module_0.get_shell_plugin(int_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'mN'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        list_0 = []
        list_1 = [bool_0, bool_0, bool_0]
        str_0 = 'BId.Pni<U,pnc_'
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, bool_0, list_0, list_1, str_0)
        var_0 = module_0.get_shell_plugin(jinja2_loader_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 3687
        float_0 = None
        str_0 = "'*\t$ngzPJi&0#4VX\n"
        int_1 = 4095
        bytes_0 = b'\x10\x9a4\x92\\'
        jinja2_loader_0 = module_0.Jinja2Loader(int_0, float_0, str_0, int_1, bytes_0)
        str_1 = 'Service instantiated - platform %s'
        list_0 = [float_0]
        str_2 = '0\rYlu'
        str_3 = 'c0'
        bytes_1 = None
        bool_0 = True
        set_0 = None
        bool_1 = True
        list_1 = [bool_0, bool_1]
        jinja2_loader_1 = module_0.Jinja2Loader(set_0, set_0, bool_1, list_1, float_0)
        tuple_0 = (bytes_1, bool_0, jinja2_loader_1, set_0)
        float_1 = 304.07
        plugin_loader_0 = module_0.PluginLoader(tuple_0, list_1, jinja2_loader_1, float_1)
        plugin_loader_1 = module_0.PluginLoader(str_2, str_3, tuple_0, plugin_loader_0, jinja2_loader_1)
        var_0 = plugin_loader_1.find_plugin(jinja2_loader_0, str_1, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 't'
        list_0 = None
        bool_0 = False
        set_0 = {str_0, bool_0}
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, str_0, set_0, str_0)
        var_0 = jinja2_loader_0.find_plugin(str_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = None
        int_0 = 2542
        str_0 = '# \\(/tmp/.*installed on.*\\)'
        str_1 = 'board_version'
        set_0 = {int_0, str_1, str_1}
        tuple_0 = (set_0, set_0)
        list_0 = [str_0, int_0, bytes_0]
        plugin_path_context_0 = module_0.PluginPathContext(tuple_0, list_0)
        var_0 = module_0.get_shell_plugin(int_0, bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = None
        bytes_0 = None
        str_0 = 'this role does not appear to have a meta/main.yml file.'
        bytes_1 = b''
        plugin_load_context_0 = module_0.PluginLoadContext()
        list_0 = [bytes_0, bytes_0, bytes_0]
        bool_0 = False
        plugin_loader_0 = module_0.PluginLoader(bytes_1, plugin_load_context_0, list_0, bool_0)
        var_0 = plugin_loader_0.format_paths(str_0)
        str_1 = ''
        plugin_load_context_1 = module_0.PluginLoadContext()
        int_1 = 2542
        str_2 = '# \\(/tmp/.*installed on.*\\)'
        str_3 = 'board_version'
        dict_0 = {str_2: int_1, str_3: int_1}
        list_1 = [bytes_0, int_0, str_3]
        set_0 = {int_0, str_3, str_3}
        tuple_0 = (set_0, set_0)
        list_2 = [str_2, int_1, bytes_0]
        plugin_path_context_0 = module_0.PluginPathContext(tuple_0, list_2)
        var_1 = plugin_load_context_1.resolve(int_1, dict_0, list_1, plugin_path_context_0)
        var_2 = plugin_load_context_1.redirect(str_1)
        var_3 = module_0.get_shell_plugin(int_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\x1f\x98&\xd5\x87\x18\xc1O\xf9\xe2'
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = '}/\x0b'
        str_1 = 'kiyj\x0b'
        dict_0 = {str_0: plugin_load_context_0, str_0: bytes_0, str_1: bytes_0}
        float_0 = 1780.86963
        bytes_1 = b'\xc2@=\xa5\x90\xbb\xbc\xaf,\xab\xa6'
        plugin_loader_0 = module_0.PluginLoader(bytes_0, dict_0, float_0, bytes_1)
        var_0 = plugin_loader_0.print_paths()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 't'
        dict_0 = None
        var_0 = module_0.get_shell_plugin(dict_0, str_0)
        bool_0 = False
        set_0 = {var_0, bool_0}
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, str_0, set_0, str_0)
        var_1 = jinja2_loader_0.find_plugin(jinja2_loader_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'X>!B%A'
        str_1 = '/pynguin/&/windows'
        int_0 = -2010
        list_0 = [str_1]
        jinja2_loader_0 = module_0.Jinja2Loader(str_1, int_0, int_0, list_0)
        var_0 = jinja2_loader_0.get(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -1722
        str_0 = 'R_t}d)'
        list_0 = [str_0, str_0]
        tuple_0 = ()
        bool_0 = True
        plugin_loader_0 = module_0.PluginLoader(str_0, list_0, tuple_0, bool_0)
        var_0 = plugin_loader_0.__setstate__(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "'b7;"
        plugin_load_context_0 = module_0.PluginLoadContext()
        tuple_0 = None
        set_0 = set()
        dict_0 = {tuple_0: tuple_0, plugin_load_context_0: str_0}
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_1.record_deprecation(tuple_0, set_0, dict_0)
        var_1 = plugin_load_context_0.record_deprecation(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = "'b7;"
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.record_deprecation(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '<N'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'H*df\x0bm\t;Y2Q?wI?3`'
        list_0 = []
        int_0 = 512
        bool_0 = False
        set_0 = {bool_0, int_0, int_0}
        bytes_0 = b'\r\x0e\xb7R?IU\xa1'
        bool_1 = False
        float_0 = 890.85911
        dict_0 = {int_0: float_0, bool_0: int_0, bool_1: bool_0}
        list_1 = [float_0, float_0]
        get_with_context_result_0 = module_0.get_with_context_result(*list_1)
        jinja2_loader_0 = module_0.Jinja2Loader(bool_1, float_0, dict_0, get_with_context_result_0)
        plugin_loader_0 = module_0.PluginLoader(int_0, bool_0, set_0, bytes_0, jinja2_loader_0)
        var_0 = plugin_loader_0.get(str_0, *list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'c.^>=WkW8I&x}BP'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'mN'
        tuple_0 = ()
        bool_0 = True
        str_1 = '6wN'
        set_0 = {str_1, tuple_0, str_0, str_1}
        plugin_loader_0 = module_0.PluginLoader(tuple_0, bool_0, str_1, set_0)
        var_0 = plugin_loader_0.print_paths()
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = None
        list_0 = [bytes_0]
        str_0 = '/root/.ansible/plugins/doc_fragments/windows'
        float_0 = 849.307234
        tuple_0 = ()
        plugin_loader_0 = module_0.PluginLoader(float_0, str_0, float_0, float_0, tuple_0)
        var_0 = plugin_loader_0.has_plugin(tuple_0, list_0)
        int_0 = 5
        var_1 = module_0.get_shell_plugin(int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'mN'
        bool_0 = False
        dict_0 = {}
        list_0 = [str_0, str_0]
        list_1 = []
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, dict_0, list_0, list_1)
        var_0 = jinja2_loader_0.all()
        float_0 = None
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_1 = 'mOI:D^3WF`@edLYsd'
        complex_0 = None
        tuple_0 = (dict_0, list_0)
        int_0 = 2070
        tuple_1 = (tuple_0, int_0)
        bool_1 = None
        dict_1 = {}
        plugin_loader_0 = module_0.PluginLoader(str_1, complex_0, tuple_1, bool_1, dict_1)
        plugin_loader_1 = module_0.PluginLoader(float_0, plugin_load_context_0, plugin_loader_0, plugin_load_context_0)
        set_0 = set()
        var_1 = plugin_loader_1.has_plugin(set_0)
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_2 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = ''
        bool_0 = False
        dict_0 = {}
        list_0 = [str_0, str_0]
        list_1 = []
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, dict_0, list_0, list_1)
        var_0 = jinja2_loader_0.all()
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_1 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'C+^!'
        set_0 = {str_0, str_0}
        dict_0 = {str_0: str_0, str_0: set_0}
        tuple_0 = (dict_0,)
        bytes_0 = b'1\x15s\xe7\x11\xe1\xb7\xaf\xbe\x8b\xb9\x92\n\xc5\xbc\x1d)\xedI'
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.record_deprecation(tuple_0, dict_0, bytes_0)
        dict_1 = {}
        float_0 = 2667.90946
        plugin_loader_0 = module_0.PluginLoader(dict_1, plugin_load_context_0, float_0, plugin_load_context_0, dict_1)
    except BaseException:
        pass

def test_case_22():
    try:
        bytes_0 = None
        str_0 = '_m'
        list_0 = [str_0, str_0]
        str_1 = '/root/.ansible/plugins/doc_fragments/windows'
        float_0 = 849.307234
        plugin_loader_0 = module_0.PluginLoader(str_1, list_0, list_0, float_0)
        var_0 = plugin_loader_0.has_plugin(bytes_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_1 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'N'
        list_0 = [str_0, str_0]
        dict_0 = None
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = module_0.get_shell_plugin(dict_0, str_0)
        plugin_load_context_1 = module_0.PluginLoadContext()
        bytes_0 = b'\xfe\x90\x05'
        var_1 = plugin_load_context_0.redirect(bytes_0)
        var_2 = module_0.get_shell_plugin(dict_0, list_0)
        str_1 = '-fOW,.'
        dict_1 = {str_1: dict_0}
        list_1 = [bytes_0, str_0, plugin_load_context_1, dict_1]
        bytes_1 = b'BCN\xdd\x00'
        float_0 = 267.118165
        set_0 = {dict_0, float_0, str_0, float_0}
        plugin_loader_0 = module_0.PluginLoader(bytes_1, float_0, list_0, list_0, set_0)
        var_3 = plugin_loader_0.get(dict_0, *list_1)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 's'
        tuple_0 = ()
        float_0 = 0.2
        bool_0 = True
        str_1 = 'oM'
        set_0 = {bool_0, bool_0, str_0}
        bytes_0 = b''
        plugin_loader_0 = module_0.PluginLoader(float_0, bool_0, str_1, set_0, bytes_0)
        var_0 = plugin_loader_0.has_plugin(tuple_0)
        list_0 = [str_0]
        dict_0 = None
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_1 = module_0.get_shell_plugin(dict_0, str_0)
        plugin_load_context_1 = module_0.PluginLoadContext()
        str_2 = '/pynguin/qN/windows'
        str_3 = None
        dict_1 = {str_2: set_0, str_2: str_0, str_3: str_0}
        var_2 = module_0.add_all_plugin_dirs(dict_1)
        var_3 = plugin_loader_0.add_directory(bytes_0)
        var_4 = plugin_load_context_1.redirect(str_1)
        var_5 = module_0.get_shell_plugin(dict_0, list_0)
        bool_1 = None
        var_6 = plugin_loader_0.has_plugin(bool_1)
        plugin_load_context_2 = module_0.PluginLoadContext()
        bool_2 = False
        var_7 = module_0.get_shell_plugin(bool_2)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '__init__'
        dict_0 = {}
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_1 = 'oM'
        var_0 = module_0.get_shell_plugin(dict_0, str_0)
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_1 = plugin_load_context_1.redirect(str_1)
        bytes_0 = b'Bq\x1a\x08\x8d'
        var_2 = module_0.get_shell_plugin(bytes_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = '__init__'
        tuple_0 = ()
        bool_0 = True
        list_0 = [bool_0, str_0, tuple_0]
        dict_0 = {str_0: list_0, str_0: bool_0}
        dict_1 = {}
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.record_deprecation(dict_0, dict_0, dict_1)
        str_1 = 'oM'
        set_0 = {bool_0, bool_0, str_0}
        bytes_0 = b'\xb3'
        plugin_loader_0 = module_0.PluginLoader(var_0, bool_0, str_1, var_0, bytes_0)
        var_1 = plugin_loader_0.has_plugin(tuple_0)
        list_1 = [str_0]
        dict_2 = None
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_2 = plugin_loader_0.all(*list_0)
        var_3 = module_0.get_shell_plugin(dict_2, str_0)
        plugin_load_context_2 = module_0.PluginLoadContext()
        str_2 = '/pynguin/qN/windows'
        str_3 = None
        dict_3 = {str_2: set_0, str_2: str_0, str_3: str_0}
        var_4 = module_0.add_all_plugin_dirs(dict_3)
        var_5 = plugin_loader_0.add_directory(bytes_0)
        var_6 = plugin_load_context_2.redirect(str_1)
        var_7 = module_0.get_shell_plugin(dict_2, list_1)
        tuple_1 = ()
        str_4 = 'a~pB"dk*'
        var_8 = plugin_loader_0.has_plugin(tuple_1, str_4)
        plugin_load_context_3 = module_0.PluginLoadContext()
        bool_1 = False
        var_9 = module_0.get_shell_plugin(bool_1)
    except BaseException:
        pass