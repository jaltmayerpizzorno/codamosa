# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    try:
        var_0 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'csh'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        var_0 = module_0.get_shell_plugin(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        get_with_context_result_0 = None
        bytes_0 = b'\xff>[\xa8'
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_load_context_1 = module_0.PluginLoadContext()
        str_0 = ''
        plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_1, str_0)
        float_0 = 3340.6
        plugin_loader_0 = module_0.PluginLoader(float_0, float_0, get_with_context_result_0, get_with_context_result_0, plugin_path_context_0)
        var_0 = plugin_loader_0.find_plugin_with_context(bytes_0, plugin_load_context_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'csh'
        set_0 = None
        dict_0 = {set_0: str_0, str_0: str_0}
        str_1 = '/pynguin/V~T/f=UDkz=/windows'
        int_0 = 4792
        str_2 = 'RMzC(T'
        jinja2_loader_0 = module_0.Jinja2Loader(str_1, int_0, str_2, set_0)
        var_0 = jinja2_loader_0.get(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '/pynguin/shell_plugins/windows'
        plugin_load_context_0 = None
        int_0 = 3202
        bytes_0 = b't\x18N\x03\x00\x9b\x1e\xbf\x1cw?\xca6z\x9f^'
        float_0 = 1712.675457
        tuple_0 = ()
        jinja2_loader_0 = module_0.Jinja2Loader(float_0, tuple_0, int_0, plugin_load_context_0, tuple_0)
        list_0 = [str_0, float_0, bytes_0]
        dict_0 = {}
        var_0 = jinja2_loader_0.all(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        var_0 = module_0.get_shell_plugin(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '/pynguin/shell_plugins/windows'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        get_with_context_result_0 = None
        bytes_0 = b'\xff>[\xa8'
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_load_context_1 = module_0.PluginLoadContext()
        float_0 = 256.1167
        dict_0 = {}
        str_0 = ''
        plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_1, str_0)
        list_0 = [dict_0, plugin_path_context_0, dict_0, dict_0]
        var_0 = module_0.add_all_plugin_dirs(list_0)
        float_1 = 3340.6
        plugin_loader_0 = module_0.PluginLoader(float_1, float_1, get_with_context_result_0, get_with_context_result_0, plugin_path_context_0)
        set_0 = {float_0, bytes_0}
        var_1 = plugin_loader_0.find_plugin_with_context(set_0, get_with_context_result_0, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = {}
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_load_context_1 = module_0.PluginLoadContext()
        bytes_0 = b'!\xb0\x15\x8f3.3\x82-M3/'
        float_0 = 0.0
        str_0 = "'xHr\rR\n\x0c(e#gb|hH]y"
        list_0 = [str_0, plugin_load_context_1, plugin_load_context_1]
        jinja2_loader_0 = module_0.Jinja2Loader(plugin_load_context_1, float_0, str_0, list_0, plugin_load_context_1)
        var_0 = jinja2_loader_0.find_plugin(dict_0, bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '/etc'
        var_0 = module_0.add_all_plugin_dirs(str_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        bool_0 = False
        set_0 = set()
        bytes_0 = b'\x19\x08\n\x12I\xcc\xe8\xb3\x04\xfa3T\x7f\xea$+\xe3\x8c'
        plugin_loader_0 = module_0.PluginLoader(bytes_0, bytes_0, set_0, str_0)
        tuple_0 = (set_0, plugin_loader_0)
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, tuple_0, bool_0, plugin_load_context_0)
        var_1 = jinja2_loader_0.find_plugin(plugin_load_context_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = None
        str_1 = 'hy'
        set_0 = {str_0, str_1, str_0, str_1}
        str_2 = '4H#j?g@'
        int_0 = -988
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.record_deprecation(set_0, str_2, int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '}5DcUjv!.1voRbb\r5i'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'k'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '_'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bytes_0 = b'{'
        plugin_load_context_0 = module_0.PluginLoadContext()
        dict_0 = {}
        str_0 = '.'
        plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, str_0)
        dict_1 = {str_0: plugin_path_context_0, str_0: str_0, str_0: plugin_load_context_0, str_0: str_0}
        var_0 = plugin_load_context_0.record_deprecation(dict_0, dict_1, bytes_0)
        var_1 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'csh'
        set_0 = None
        var_0 = module_0.get_shell_plugin(set_0, str_0)
        float_0 = 0.0001
        plugin_load_context_0 = module_0.PluginLoadContext()
        list_0 = [str_0, str_0, set_0]
        plugin_loader_0 = module_0.PluginLoader(float_0, plugin_load_context_0, list_0, set_0)
        var_1 = plugin_loader_0.print_paths()
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = None
        str_0 = '{W*\\7L9D'
        list_0 = [bytes_0, bytes_0, str_0]
        complex_0 = None
        list_1 = [str_0, str_0, list_0, bytes_0]
        tuple_0 = (str_0, list_0, complex_0, list_1)
        bool_0 = None
        jinja2_loader_0 = module_0.Jinja2Loader(bytes_0, tuple_0, list_0, bool_0)
        int_0 = 692
        str_1 = 'ssh_key_bits'
        dict_0 = {str_1: int_0}
        plugin_path_context_0 = module_0.PluginPathContext(str_1, dict_0)
        int_1 = 101
        jinja2_loader_1 = module_0.Jinja2Loader(int_0, str_1, plugin_path_context_0, int_1)
        var_0 = jinja2_loader_1.find_plugin(jinja2_loader_0)
    except BaseException:
        pass

def test_case_18():
    try:
        tuple_0 = None
        list_0 = [tuple_0]
        get_with_context_result_0 = None
        int_0 = 2790
        plugin_loader_0 = module_0.PluginLoader(tuple_0, list_0, get_with_context_result_0, int_0)
        bool_0 = False
        bytes_0 = b'\xd0DO]\x060\x18\x16\xdf\xb4\xd9\x86\xe4*\n4%\x87\xe2'
        float_0 = 921.7329
        float_1 = -144.024
        int_1 = -229
        str_0 = 'T7M*"\x0cuXnnM9tQ'
        list_1 = []
        jinja2_loader_0 = module_0.Jinja2Loader(get_with_context_result_0, int_1, str_0, list_1)
        str_1 = '\'?Ph|"$R]U"~_Fd'
        plugin_loader_1 = module_0.PluginLoader(plugin_loader_0, float_1, jinja2_loader_0, str_1)
        var_0 = plugin_loader_1.find_plugin(bool_0, bytes_0, plugin_loader_0, float_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'sh'
        var_0 = None
        var_1 = module_0.get_shell_plugin(str_0, var_0)
        var_2 = type(var_1)
        var_3 = module_0.get_shell_plugin()
    except BaseException:
        pass