# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    try:
        str_0 = 'zh'
        var_0 = module_0.get_all_plugin_loaders()
        var_1 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1000.0
        int_0 = None
        var_0 = module_0.add_dirs_to_loader(float_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        plugin_loader_0 = None
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.redirect(plugin_loader_0)
        str_0 = ''
        var_1 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/bin/bash'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        str_0 = ')!mBa3:spF'
        str_1 = 'lv\n(I'
        bytes_0 = b'&\xea'
        bytes_1 = b'\xe1\t8\xf0]Y\xcaV\x8d\xce\xb1Z\xe0\xc8c~\xe5\xa4\x93'
        jinja2_loader_0 = module_0.Jinja2Loader(str_0, str_1, dict_0, bytes_0, bytes_1)
        var_0 = jinja2_loader_0.get(str_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        str_1 = 'S}`/'
        var_0 = module_0.get_shell_plugin(str_0, str_1)
        plugin_load_context_0 = module_0.PluginLoadContext()
        float_0 = -968.3
        bytes_0 = b'\x96\x8c:\x80\x9c\x91\xf8\xfe]\x0fL\r\xd7 >\xec{h&'
        bool_0 = False
        jinja2_loader_0 = module_0.Jinja2Loader(plugin_load_context_0, float_0, bytes_0, bool_0)
        var_1 = module_0.get_shell_plugin(jinja2_loader_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'sh'
        var_0 = module_0.get_shell_plugin(str_0)
        var_1 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = None
        int_0 = 906
        bytes_0 = b'D>\xc8\x91'
        bytes_1 = b'\x08\xeb\xcb\x11\xe5\xb44e\xa8b\x9e\xf0H\x19'
        int_1 = 520
        plugin_loader_0 = module_0.PluginLoader(int_0, set_0, bytes_0, bytes_0, bytes_1, int_1)
        var_0 = plugin_loader_0.__getstate__()
        list_0 = []
        var_1 = module_0.add_all_plugin_dirs(list_0)
        get_with_context_result_0 = module_0.get_with_context_result()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'test'
        str_1 = 'I[\r\x0bT`iDNOR"PU\x0cLc'
        float_0 = 294.055
        dict_0 = {}
        str_2 = 'FDOIMYVJ>okv.pMuUG.z'
        bytes_0 = b'r\x95\x1bi\xf8\x7fm\xdd\xf4'
        set_0 = {str_0}
        plugin_path_context_0 = module_0.PluginPathContext(bytes_0, set_0)
        jinja2_loader_0 = module_0.Jinja2Loader(float_0, dict_0, str_2, plugin_path_context_0, dict_0)
        var_0 = jinja2_loader_0.find_plugin(str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        set_0 = None
        list_0 = [set_0, set_0, set_0]
        float_0 = 0.2
        float_1 = -789.745096
        float_2 = -314.98
        var_0 = module_0.get_all_plugin_loaders()
        str_0 = 't6)TV~$=XO;cnE<;'
        plugin_loader_0 = module_0.PluginLoader(float_0, float_1, float_2, str_0)
        var_1 = plugin_loader_0.has_plugin(list_0)
        bytes_0 = b'\xff\xa9}\t-7\x8e`\xe7&9\x88\xbdw8C\x19*\xac'
        var_2 = plugin_loader_0.__setstate__(bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'J'
        var_0 = module_0.get_shell_plugin(str_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '~^Xz7VnWx%x}?MBhiA'
        set_0 = {str_0}
        dict_0 = {}
        plugin_load_context_0 = module_0.PluginLoadContext()
        jinja2_loader_0 = module_0.Jinja2Loader(str_0, set_0, dict_0, plugin_load_context_0)
        var_0 = jinja2_loader_0.all()
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'test'
        float_0 = 300.6153870175769
        dict_0 = None
        plugin_load_context_0 = None
        list_0 = []
        int_0 = None
        jinja2_loader_0 = module_0.Jinja2Loader(dict_0, plugin_load_context_0, list_0, int_0)
        dict_1 = {}
        str_1 = 'FDOIMYVJ>okv.pMuUG.z'
        bytes_0 = b'Y\x9d\xafT\xd5'
        set_0 = {str_0}
        plugin_path_context_0 = module_0.PluginPathContext(bytes_0, set_0)
        jinja2_loader_1 = module_0.Jinja2Loader(float_0, dict_1, str_1, plugin_path_context_0, dict_1)
        int_1 = 1190
        bool_0 = True
        float_1 = -884.8503
        plugin_loader_0 = module_0.PluginLoader(bool_0, float_1, str_1, bool_0)
        var_0 = plugin_loader_0.find_plugin_with_context(set_0, int_1)
    except BaseException:
        pass

def test_case_13():
    try:
        set_0 = None
        list_0 = [set_0, set_0, set_0]
        var_0 = module_0.get_all_plugin_loaders()
        get_with_context_result_0 = None
        str_0 = 'Type is not a valid list, set, or dict'
        var_1 = module_0.get_all_plugin_loaders()
        tuple_0 = ()
        dict_0 = {str_0: str_0, str_0: var_0}
        float_0 = 951.0
        bool_0 = False
        plugin_path_context_0 = module_0.PluginPathContext(list_0, get_with_context_result_0)
        jinja2_loader_0 = module_0.Jinja2Loader(float_0, bool_0, get_with_context_result_0, plugin_path_context_0, tuple_0)
        var_2 = jinja2_loader_0.all(**dict_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_3 = module_0.add_all_plugin_dirs(plugin_path_context_0)
        var_4 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_14():
    try:
        set_0 = None
        list_0 = [set_0, set_0, set_0]
        float_0 = 0.2
        float_1 = -789.745096
        float_2 = -2305.7
        float_3 = -787.257
        str_0 = '7{Sws\rMS1>i'
        plugin_path_context_0 = module_0.PluginPathContext(float_3, str_0)
        str_1 = 'qb2k@sJL'
        plugin_path_context_1 = module_0.PluginPathContext(plugin_path_context_0, str_1)
        var_0 = module_0.add_all_plugin_dirs(float_2)
        float_4 = -303.97793654314097
        var_1 = module_0.get_all_plugin_loaders()
        str_2 = 'tq)TV~$OXO;cnE<4'
        plugin_loader_0 = module_0.PluginLoader(float_0, float_1, float_4, str_2)
        var_2 = plugin_loader_0.has_plugin(list_0)
        dict_0 = {set_0: str_1}
        var_3 = plugin_loader_0.__setstate__(dict_0)
        var_4 = plugin_loader_0.get(str_2)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '/root/.ansible/plugins/doc_frments/windows'
        var_0 = module_0.get_shell_plugin(str_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        set_0 = None
        list_0 = [set_0, set_0, set_0]
        float_0 = -788.7059814464247
        var_0 = module_0.get_all_plugin_loaders()
        get_with_context_result_0 = None
        str_0 = 'Type is not a valid list, set, or dict'
        var_1 = module_0.get_all_plugin_loaders()
        tuple_0 = ()
        dict_0 = {str_0: str_0, str_0: var_0}
        float_1 = 951.0
        bool_0 = False
        plugin_path_context_0 = module_0.PluginPathContext(list_0, get_with_context_result_0)
        jinja2_loader_0 = module_0.Jinja2Loader(float_1, bool_0, get_with_context_result_0, plugin_path_context_0, tuple_0)
        var_2 = jinja2_loader_0.all(**dict_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_3 = module_0.add_all_plugin_dirs(plugin_path_context_0)
        plugin_path_context_1 = module_0.PluginPathContext(plugin_load_context_0, list_0)
        plugin_path_context_2 = module_0.PluginPathContext(dict_0, plugin_path_context_1)
        bool_1 = False
        plugin_loader_0 = module_0.PluginLoader(float_0, set_0, bool_1, set_0, list_0)
        str_1 = ".m\x0bY,:\x0b] 9M_:1Mo'(C"
        var_4 = plugin_loader_0.has_plugin(str_1)
        var_5 = plugin_loader_0.has_plugin(plugin_loader_0)
        var_6 = plugin_loader_0.get(get_with_context_result_0, *list_0, **dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        set_0 = None
        float_0 = -788.7059814464247
        var_0 = module_0.get_all_plugin_loaders()
        float_1 = None
        get_with_context_result_0 = None
        var_1 = module_0.get_all_plugin_loaders()
        tuple_0 = ()
        str_0 = 'set_dscp_mark'
        dict_0 = {float_1: float_0}
        plugin_loader_0 = module_0.PluginLoader(get_with_context_result_0, dict_0, get_with_context_result_0, tuple_0)
        var_2 = plugin_loader_0.add_directory(str_0)
        var_3 = plugin_loader_0.get(set_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'Expected AnsibleError to occur'
        var_0 = AssertionError(str_0)
        str_1 = 'zsh'
        var_1 = module_0.get_shell_plugin(str_1)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'test'
        str_1 = 'X}B/!u{ec/j\x0ci7.['
        float_0 = 316.8414165686764
        dict_0 = {}
        str_2 = 'FDOIMYVJ>okv.pMuUG.z'
        bytes_0 = b'r\x95\x1bi\xf8\x7fm\xdd\xf4'
        set_0 = {str_0}
        plugin_path_context_0 = module_0.PluginPathContext(bytes_0, set_0)
        jinja2_loader_0 = module_0.Jinja2Loader(float_0, dict_0, str_2, plugin_path_context_0, dict_0)
        var_0 = jinja2_loader_0.find_plugin(str_1)
    except BaseException:
        pass

def test_case_20():
    try:
        set_0 = None
        list_0 = [set_0, set_0, set_0]
        var_0 = module_0.get_all_plugin_loaders()
        get_with_context_result_0 = None
        str_0 = 'Type is not a valid list, set, or dict'
        var_1 = module_0.get_all_plugin_loaders()
        tuple_0 = ()
        dict_0 = {str_0: str_0, str_0: var_0}
        float_0 = 951.0
        bool_0 = False
        plugin_path_context_0 = module_0.PluginPathContext(list_0, get_with_context_result_0)
        jinja2_loader_0 = module_0.Jinja2Loader(float_0, bool_0, get_with_context_result_0, plugin_path_context_0, tuple_0)
        var_2 = jinja2_loader_0.all(**dict_0)
        bool_1 = False
        plugin_loader_0 = module_0.PluginLoader(bool_1, plugin_path_context_0, get_with_context_result_0, tuple_0)
        var_3 = plugin_loader_0.format_paths(list_0)
    except BaseException:
        pass

def test_case_21():
    try:
        dict_0 = None
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = module_0.get_shell_plugin(dict_0, plugin_load_context_0)
        var_1 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '_'
        var_0 = module_0.get_shell_plugin(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        set_0 = None
        var_0 = module_0.get_all_plugin_loaders()
        bool_0 = False
        plugin_load_context_0 = module_0.PluginLoadContext()
        bytes_0 = b'v\xf5\xea\x99\x14<W\xac\x89w\x16\xfd7\xee\xeb\xa9\xc3'
        plugin_loader_0 = module_0.PluginLoader(bool_0, plugin_load_context_0, bytes_0, set_0)
        tuple_0 = ()
        str_0 = 'S>Y6cvFDJA'
        var_1 = plugin_loader_0.add_directory(str_0, tuple_0)
        str_1 = '+x@Y'
        str_2 = '>J,E#\x0b@Yh6K/]~D'
        dict_0 = {str_1: str_1, str_1: str_1, str_2: str_1, str_2: str_1}
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_2 = plugin_loader_0.has_plugin(dict_0, plugin_loader_0)
        str_3 = '2JxbO Bl;oQ3%'
        float_0 = 3155.427531
        var_3 = plugin_loader_0.has_plugin(str_3, float_0)
        bool_1 = True
        var_4 = plugin_loader_0.get(bool_1)
    except BaseException:
        pass