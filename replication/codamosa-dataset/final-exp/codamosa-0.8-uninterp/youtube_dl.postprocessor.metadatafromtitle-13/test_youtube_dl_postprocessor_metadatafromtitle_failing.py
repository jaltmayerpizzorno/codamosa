# Automatically generated by Pynguin.
import youtube_dl.postprocessor.metadatafromtitle as module_0

def test_case_0():
    try:
        bool_0 = True
        int_0 = 1589262469
        metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(bool_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        float_0 = 3132.60519
        str_0 = 'J'
        metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(float_0, str_0)
        var_0 = metadata_from_title_p_p_0.format_to_regex(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '%(title)s - %(artist)s'
        bytes_0 = b'\x9f\xae7\xe4\x94o5\xe0\xb1\xbfW\x9c'
        metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(bytes_0, str_0)
        set_0 = {str_0, str_0, str_0}
        metadata_from_title_p_p_1 = module_0.MetadataFromTitlePP(str_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'title'
        str_1 = '37.111.0.0/17'
        str_2 = {str_0: str_1, str_0: str_0}
        str_3 = '%(ile)s - %(artist)s'
        metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_2, str_3)
        str_4 = 'dummy - foo - bar'
        str_5 = {str_0: str_4}
        var_0 = metadata_from_title_p_p_0.run(str_5)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'title'
        str_1 = 'abcd efg hijk'
        str_2 = {str_0: str_1}
        var_0 = None
        str_3 = '%(title)s - %(artist)s'
        metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(var_0, str_3)
        var_1 = metadata_from_title_p_p_0.run(str_2)
    except BaseException:
        pass