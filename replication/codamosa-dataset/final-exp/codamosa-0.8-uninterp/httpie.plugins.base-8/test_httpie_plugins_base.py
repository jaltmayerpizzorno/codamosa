# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    pass

def test_case_1():
    tuple_0 = ()
    converter_plugin_0 = module_0.ConverterPlugin(tuple_0)

def test_case_2():
    str_0 = 'content'
    str_1 = 'application/atom+xml'
    str_2 = 'format_options'
    var_0 = None
    var_1 = {str_2: var_0}
    formatter_plugin_0 = module_0.FormatterPlugin(**var_1)
    str_3 = formatter_plugin_0.format_body(str_0, str_1)

def test_case_3():
    str_0 = 'content'
    str_1 = 'application/atom+xml'
    str_2 = 'format_options'
    var_0 = None
    var_1 = {str_2: var_0}
    formatter_plugin_0 = module_0.FormatterPlugin(**var_1)
    str_3 = formatter_plugin_0.format_headers(str_2)
    str_4 = formatter_plugin_0.format_body(str_0, str_1)