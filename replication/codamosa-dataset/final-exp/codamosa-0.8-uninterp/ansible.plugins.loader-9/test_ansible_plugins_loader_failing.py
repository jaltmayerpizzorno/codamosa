# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    try:
        var_0 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "|BlOs\t$%-D'!"
        set_0 = {str_0}
        var_0 = module_0.add_dirs_to_loader(str_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'EBS!V|Rc\x0cvXjX[K'
        set_0 = {str_0, str_0}
        str_1 = 'A;'
        plugin_path_context_0 = module_0.PluginPathContext(set_0, str_1)
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        list_0 = [plugin_load_context_0, plugin_load_context_0, plugin_load_context_0]
        str_0 = '9cQ~/x||s4yw]'
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_1.record_deprecation(list_0, plugin_load_context_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '__init__'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 3
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.redirect(int_0)
        str_0 = 'jBS!K|Rc\x0cvXjX[K'
        var_1 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'EVS!V|Rc\x0cvXjX[K'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'x\rT!H]-o'
        float_0 = 383.0
        set_0 = set()
        plugin_loader_0 = module_0.PluginLoader(float_0, float_0, set_0, float_0)
        var_0 = plugin_loader_0.get_with_context(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -1614
        var_0 = module_0.get_shell_plugin(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -206.94573
        bool_0 = False
        get_with_context_result_0 = None
        plugin_loader_0 = module_0.PluginLoader(bool_0, get_with_context_result_0, get_with_context_result_0, float_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        bytes_0 = b'\xc6m|\x1eVx'
        bytes_1 = b'\xdf\xdb9\xbb('
        plugin_loader_1 = module_0.PluginLoader(float_0, plugin_loader_0, plugin_load_context_0, bytes_0, bytes_1)
        set_0 = {bytes_1, plugin_load_context_0, bytes_1}
        var_0 = plugin_loader_1.find_plugin_with_context(set_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -2215.3
        set_0 = None
        list_0 = [float_0, float_0]
        bytes_0 = None
        jinja2_loader_0 = module_0.Jinja2Loader(float_0, set_0, list_0, set_0, bytes_0)
        str_0 = ''
        dict_0 = {str_0: str_0}
        list_1 = [str_0, str_0]
        list_2 = [dict_0]
        float_1 = -844.92317
        plugin_path_context_0 = module_0.PluginPathContext(list_2, float_1)
        str_1 = 'Qk_Z-3RB'
        plugin_loader_0 = module_0.PluginLoader(str_0, dict_0, list_1, plugin_path_context_0, str_1)
        var_0 = plugin_loader_0.format_paths(jinja2_loader_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ']'
        set_0 = set()
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_loader_0 = module_0.PluginLoader(str_0, set_0, plugin_load_context_0, set_0)
        var_0 = plugin_loader_0.has_plugin(str_0)
        var_1 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'state=link'
        float_0 = -861.9
        bytes_0 = b'\x84\xd0\x19\x1e{\xf2/\xfb\xc4\xac'
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_loader_0 = module_0.PluginLoader(str_0, float_0, bytes_0, plugin_load_context_0)
        var_0 = plugin_loader_0.print_paths()
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -410.75041
        list_0 = []
        plugin_path_context_0 = module_0.PluginPathContext(float_0, list_0)
        var_0 = module_0.get_shell_plugin(plugin_path_context_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'uno*s'
        str_1 = '%s -n -r -v %s'
        list_0 = [str_1, str_0]
        plugin_load_context_0 = module_0.PluginLoadContext()
        jinja2_loader_0 = module_0.Jinja2Loader(str_1, list_0, list_0, plugin_load_context_0)
        var_0 = jinja2_loader_0.all()
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = "~/r!<MJ7'aMB$e?csB\rq"
        bytes_0 = b'I\x854\x12\xbe\x1a\x9c'
        plugin_loader_0 = None
        str_1 = 'U'
        plugin_path_context_0 = module_0.PluginPathContext(plugin_loader_0, str_1)
        bytes_1 = b'HP\xea\x1dx?:\x9b\xf5\x90\xaf\x0f\x9fM*\xff\xbc\xe8\x1f_'
        tuple_0 = (plugin_path_context_0, bytes_0, bytes_1)
        dict_0 = {plugin_path_context_0: bytes_0, tuple_0: plugin_path_context_0, bytes_1: bytes_0}
        list_0 = [plugin_path_context_0, bytes_0]
        plugin_loader_1 = module_0.PluginLoader(bytes_0, tuple_0, dict_0, dict_0, list_0)
        var_0 = plugin_loader_1.add_directory(str_0)
        str_2 = 'Failed to init/update submodules: %s'
        dict_1 = {str_0: list_0, str_2: plugin_path_context_0}
        var_1 = plugin_loader_1.get(plugin_path_context_0, **dict_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'su'
        str_1 = None
        var_0 = module_0.get_shell_plugin(str_1, str_0)
        str_2 = '<\\x01S*Er['
        bytes_0 = b'Y'
        bool_0 = False
        bytes_1 = b'_l\x0f'
        plugin_loader_0 = module_0.PluginLoader(str_2, bytes_0, bool_0, bytes_1)
        var_1 = plugin_loader_0.all()
        var_2 = module_0.get_all_plugin_loaders()
        dict_0 = {str_2: bytes_1, str_1: var_1, str_1: var_2}
        var_3 = plugin_loader_0.__setstate__(dict_0)
        var_4 = plugin_loader_0.all()
        dict_1 = None
        var_5 = plugin_loader_0.has_plugin(dict_1)
        var_6 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '/pynguin/.VsVKk\\D_3l>e-\tt/windows'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b'@\x94=6\xa47w`\xf9e\xc8\xcc\x8c\xc8'
        str_0 = 'sslclientkey'
        set_0 = {str_0, str_0}
        str_1 = '/pynguin/shell_plugins/windows'
        dict_0 = {str_0: set_0}
        jinja2_loader_0 = module_0.Jinja2Loader(str_0, set_0, str_1, dict_0)
        var_0 = jinja2_loader_0.find_plugin(bytes_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'EVS!V|Rc\x0cvXjX[K'
        plugin_load_context_0 = module_0.PluginLoadContext()
        int_0 = -2409
        list_0 = [str_0]
        plugin_load_context_1 = module_0.PluginLoadContext()
        bool_0 = False
        set_0 = {bool_0, str_0}
        plugin_loader_0 = module_0.PluginLoader(int_0, list_0, plugin_load_context_1, set_0)
        var_0 = plugin_loader_0.__setstate__(plugin_load_context_0)
    except BaseException:
        pass

def test_case_20():
    try:
        float_0 = -2215.3
        set_0 = None
        list_0 = [float_0, float_0]
        bytes_0 = None
        jinja2_loader_0 = module_0.Jinja2Loader(float_0, set_0, list_0, set_0, bytes_0)
        str_0 = ''
        list_1 = [str_0, str_0]
        var_0 = jinja2_loader_0.find_plugin(list_1)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'sunos'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '__init__'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        list_0 = []
        bool_0 = False
        int_0 = 973
        bool_1 = True
        int_1 = -3131
        tuple_0 = (int_1,)
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, int_0, bool_1, tuple_0)
        var_0 = jinja2_loader_0.get(list_0, *list_0)
    except BaseException:
        pass

def test_case_24():
    try:
        float_0 = 0.1
        tuple_0 = None
        plugin_path_context_0 = module_0.PluginPathContext(float_0, tuple_0)
        var_0 = module_0.add_all_plugin_dirs(plugin_path_context_0)
        str_0 = 'su'
        str_1 = None
        var_1 = module_0.get_shell_plugin(str_1, str_0)
        str_2 = '<\\x01S*Er['
        bytes_0 = b'Y'
        bool_0 = False
        bytes_1 = b'_l\x0f'
        plugin_loader_0 = module_0.PluginLoader(str_2, bytes_0, bool_0, bytes_1)
        var_2 = plugin_loader_0.all()
        var_3 = plugin_loader_0.all()
        dict_0 = None
        var_4 = plugin_loader_0.has_plugin(dict_0)
        bytes_2 = b'y^\x1a'
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_5 = plugin_loader_0.find_plugin(bytes_2, plugin_load_context_0, plugin_load_context_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '5)5$Ez^0M*9-hhhKzD"\r'
        dict_0 = {str_0: str_0, str_0: str_0}
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_path_context_0 = module_0.PluginPathContext(dict_0, plugin_load_context_0)
        int_0 = -1844
        plugin_load_context_1 = module_0.PluginLoadContext()
        float_0 = 1942.048
        list_0 = [int_0, float_0, int_0]
        tuple_0 = (list_0, list_0)
        str_1 = "c;:dMRo'?m-:"
        int_1 = -889
        plugin_loader_0 = module_0.PluginLoader(str_1, plugin_path_context_0, tuple_0, int_1, int_1)
        int_2 = -1124
        plugin_loader_1 = module_0.PluginLoader(plugin_loader_0, dict_0, int_2, tuple_0)
        var_0 = plugin_loader_1.format_paths(list_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'su'
        str_1 = None
        var_0 = module_0.get_shell_plugin(str_1, str_0)
        str_2 = '<\\x01S*Er['
        bytes_0 = b'Y'
        bool_0 = False
        bytes_1 = b'_l\x0f'
        plugin_loader_0 = module_0.PluginLoader(str_2, bytes_0, bool_0, bytes_1)
        dict_0 = {}
        var_1 = module_0.get_shell_plugin(dict_0)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = "':OZ)4+d"
        dict_0 = {str_0: str_0}
        str_1 = '/pynguin/.VsVKk\\D_3l>e-\tt/windows'
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_2 = ']LF8'
        int_0 = 1767
        tuple_0 = ()
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, str_2, int_0, tuple_0)
        var_0 = plugin_loader_0.has_plugin(str_1, dict_0)
        plugin_load_context_1 = module_0.PluginLoadContext()
        float_0 = -1842.4318
        list_0 = None
        get_with_context_result_0 = None
        var_1 = plugin_load_context_1.record_deprecation(float_0, list_0, get_with_context_result_0)
        var_2 = plugin_loader_0.print_paths()
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = "~/r!<MJ7'aMB$e?csB\rq"
        bytes_0 = b'I\x854\x12\xbe\x1a\x9c'
        plugin_loader_0 = None
        str_1 = 'U'
        plugin_path_context_0 = module_0.PluginPathContext(plugin_loader_0, str_1)
        bytes_1 = b'HP\xea\x1dx?:\x9b\xf5\x90\xaf\x0f\x9fM*\xff\xbc\xe8\x1f_'
        tuple_0 = (plugin_path_context_0, bytes_0, bytes_1)
        dict_0 = {plugin_path_context_0: bytes_0, tuple_0: plugin_path_context_0, bytes_1: bytes_0}
        list_0 = [bytes_0]
        plugin_loader_1 = module_0.PluginLoader(bytes_0, tuple_0, dict_0, dict_0, list_0)
        var_0 = plugin_loader_1.add_directory(str_0)
        str_2 = 'Failed to init/update submodules: %s'
        dict_1 = {str_0: list_0, str_2: plugin_path_context_0}
        var_1 = plugin_loader_1.get(plugin_path_context_0, **dict_1)
    except BaseException:
        pass

def test_case_29():
    try:
        float_0 = -21.81064526643386
        tuple_0 = None
        plugin_path_context_0 = module_0.PluginPathContext(float_0, tuple_0)
        var_0 = module_0.add_all_plugin_dirs(plugin_path_context_0)
        str_0 = 'su'
        str_1 = None
        var_1 = module_0.get_shell_plugin(str_1, str_0)
        str_2 = '<\\x01S*Er['
        int_0 = 73
        int_1 = -718
        str_3 = 'R'
        set_0 = {tuple_0}
        list_0 = [str_2, tuple_0]
        plugin_loader_0 = module_0.PluginLoader(str_0, set_0, tuple_0, list_0)
        jinja2_loader_0 = module_0.Jinja2Loader(plugin_loader_0, list_0, plugin_loader_0, set_0)
        plugin_loader_1 = module_0.PluginLoader(int_1, str_3, str_2, jinja2_loader_0)
        var_2 = plugin_loader_1.has_plugin(int_0)
        bool_0 = True
        str_4 = 'poqJf'
        str_5 = '`Vnp6Ks/-u05 HqKibU'
        dict_0 = {str_4: jinja2_loader_0, str_1: bool_0, str_5: str_2}
        var_3 = jinja2_loader_0.find_plugin(jinja2_loader_0, dict_0)
    except BaseException:
        pass