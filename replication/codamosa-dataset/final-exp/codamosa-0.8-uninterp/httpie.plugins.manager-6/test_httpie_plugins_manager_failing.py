# Automatically generated by Pynguin.
import httpie.plugins.manager as module_0

def test_case_0():
    try:
        plugin_manager_0 = module_0.PluginManager()
        list_0 = plugin_manager_0.get_auth_plugins()
        type_0 = None
        list_1 = [type_0, type_0, type_0, type_0]
        var_0 = plugin_manager_0.register(*list_1)
        dict_0 = plugin_manager_0.get_auth_plugin_mapping()
    except BaseException:
        pass

def test_case_1():
    try:
        type_0 = None
        list_0 = [type_0, type_0, type_0]
        str_0 = 'Qdd`'
        str_1 = 'CTMM[iH\x0c'
        dict_0 = {str_0: str_0, str_1: str_0}
        plugin_manager_0 = module_0.PluginManager(**dict_0)
        var_0 = plugin_manager_0.unregister(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        plugin_manager_0 = module_0.PluginManager()
        list_0 = plugin_manager_0.get_auth_plugins()
        str_0 = 'TpJpk$`{QJH6}6U\tw^l'
        dict_0 = plugin_manager_0.get_auth_plugin_mapping()
        type_0 = plugin_manager_0.get_auth_plugin(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        plugin_manager_0 = module_0.PluginManager()
        list_0 = plugin_manager_0.get_converters()
        str_0 = None
        type_0 = plugin_manager_0.get_auth_plugin(str_0)
    except BaseException:
        pass