# Automatically generated by Pynguin.
import httpie.plugins.manager as module_0

def test_case_0():
    try:
        plugin_manager_0 = module_0.PluginManager()
        dict_0 = plugin_manager_0.get_auth_plugin_mapping()
        str_0 = '/BS(W%$>'
        list_0 = []
        type_0 = None
        list_1 = [list_0, type_0]
        var_0 = plugin_manager_0.register(*list_1)
        var_1 = plugin_manager_0.load_installed_plugins()
        type_1 = plugin_manager_0.get_auth_plugin(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        plugin_manager_0 = module_0.PluginManager()
        dict_0 = plugin_manager_0.get_auth_plugin_mapping()
        var_0 = plugin_manager_0.filter()
        var_1 = plugin_manager_0.__repr__()
        list_0 = plugin_manager_0.get_transport_plugins()
        list_1 = plugin_manager_0.get_transport_plugins()
        str_0 = '* 5Fl'
        var_2 = plugin_manager_0.register()
        var_3 = plugin_manager_0.unregister(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Fm*3@Bo!,xAI]"\'dLPwL'
        list_0 = []
        plugin_manager_0 = module_0.PluginManager(*list_0)
        type_0 = plugin_manager_0.get_auth_plugin(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'[\x8c\xa6\xec\x8a'
        dict_0 = {}
        plugin_manager_0 = module_0.PluginManager(**dict_0)
        list_0 = plugin_manager_0.get_converters()
        list_1 = [bytes_0]
        plugin_manager_1 = module_0.PluginManager(*list_1)
        list_2 = plugin_manager_1.get_converters()
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        plugin_manager_0 = module_0.PluginManager(*list_0)
        var_0 = plugin_manager_0.__repr__()
        str_0 = 'Fm*3@Bo!,xAI]"\'dLPwL'
        list_1 = []
        plugin_manager_1 = module_0.PluginManager(*list_1)
        type_0 = plugin_manager_1.get_auth_plugin(str_0)
    except BaseException:
        pass