# Automatically generated by Pynguin.
import isort.exceptions as module_0
import builtins as module_1

def test_case_0():
    try:
        str_0 = '@I'
        introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_0)
        unsupported_encoding_0 = module_0.UnsupportedEncoding(str_0)
        dict_0 = {}
        str_1 = None
        dict_1 = {str_1: dict_0}
        unsupported_settings_0 = module_0.UnsupportedSettings(dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '--fgw'
        unsupported_encoding_0 = module_0.UnsupportedEncoding(str_0)
        file_skip_comment_0 = module_0.FileSkipComment(str_0)
        str_1 = '`iiD2*\tMB$'
        missing_section_0 = module_0.MissingSection(str_1, str_0)
        str_2 = '`DJUu\tUyxPB4.!o:*-F'
        list_0 = []
        i_sort_error_0 = module_0.ISortError(*list_0)
        introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_2)
        list_1 = [str_2, str_0]
        str_3 = 'r-2c.m\x0b\x0ctq'
        str_4 = "'|P'\n$Rd,ORpfI>g"
        invalid_settings_path_0 = module_0.InvalidSettingsPath(str_4)
        exception_0 = None
        literal_parsing_failure_0 = module_0.LiteralParsingFailure(str_3, exception_0)
        dict_0 = {str_2: str_2}
        exception_1 = module_1.Exception(*list_1, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        unsupported_encoding_0 = module_0.UnsupportedEncoding(str_0)
        profile_does_not_exist_0 = module_0.ProfileDoesNotExist(str_0)
        formatting_plugin_does_not_exist_0 = module_0.FormattingPluginDoesNotExist(str_0)
        i_sort_error_0 = module_0.ISortError()
        str_1 = '--fgw'
        str_2 = '*CU'
        str_3 = 'f/2/JGJ)bG\n" #=x'
        str_4 = ''
        file_skipped_0 = module_0.FileSkipped(str_3, str_4)
        str_5 = ') while trying to identify the '
        introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_0)
        str_6 = None
        str_7 = 'OH(Y'
        file_skip_setting_0 = module_0.FileSkipSetting(str_7)
        dict_0 = {str_0: str_2, str_2: str_5, str_6: str_1}
        type_0 = None
        literal_sort_type_mismatch_0 = module_0.LiteralSortTypeMismatch(type_0, type_0)
        dict_1 = {str_1: dict_0}
        unsupported_settings_0 = module_0.UnsupportedSettings(dict_1)
    except BaseException:
        pass