# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    try:
        bool_0 = True
        auth_plugin_0 = module_0.AuthPlugin()
        var_0 = auth_plugin_0.get_auth(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        base_plugin_0 = module_0.BasePlugin(*list_0)
        transport_plugin_0 = module_0.TransportPlugin()
        transport_plugin_1 = module_0.TransportPlugin(*list_0)
        var_0 = transport_plugin_1.get_adapter()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = None
        converter_plugin_0 = module_0.ConverterPlugin(dict_0)
        int_0 = -866
        var_0 = converter_plugin_0.convert(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        formatter_plugin_0 = module_0.FormatterPlugin()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        str_1 = 'format_options'
        list_0 = []
        dict_0 = {str_1: list_0, str_1: str_1}
        formatter_plugin_0 = module_0.FormatterPlugin(**dict_0)
        str_2 = formatter_plugin_0.format_headers(str_0)
        base_plugin_0 = None
        converter_plugin_0 = module_0.ConverterPlugin(base_plugin_0)
        bytes_0 = b'x\x14O\xd0\x88;\x1a$\x00\xad\xe9\x18\x82\x96'
        var_0 = converter_plugin_0.convert(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'format_options'
        list_0 = []
        dict_0 = {str_0: list_0, str_0: str_0}
        formatter_plugin_0 = module_0.FormatterPlugin(**dict_0)
        formatter_plugin_1 = module_0.FormatterPlugin(**dict_0)
        transport_plugin_0 = module_0.TransportPlugin(*list_0)
        str_1 = 'm'
        str_2 = formatter_plugin_1.format_body(str_0, str_1)
        formatter_plugin_2 = module_0.FormatterPlugin()
    except BaseException:
        pass