# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    try:
        str_0 = 'format_options'
        var_0 = {}
        var_1 = {str_0: var_0}
        formatter_plugin_0 = module_0.FormatterPlugin(**var_1)
        str_1 = formatter_plugin_0.format_headers(str_0)
        auth_plugin_0 = module_0.AuthPlugin()
        var_2 = auth_plugin_0.get_auth()
    except BaseException:
        pass

def test_case_1():
    try:
        transport_plugin_0 = module_0.TransportPlugin()
        var_0 = transport_plugin_0.get_adapter()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '$T)BA@Bx.N.8|cY'
        converter_plugin_0 = module_0.ConverterPlugin(str_0)
        formatter_plugin_0 = module_0.FormatterPlugin()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        str_0 = '$T)BA@Bx.N.8|cY'
        converter_plugin_0 = module_0.ConverterPlugin(str_0)
        var_0 = converter_plugin_0.convert(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        formatter_plugin_0 = module_0.FormatterPlugin()
    except BaseException:
        pass