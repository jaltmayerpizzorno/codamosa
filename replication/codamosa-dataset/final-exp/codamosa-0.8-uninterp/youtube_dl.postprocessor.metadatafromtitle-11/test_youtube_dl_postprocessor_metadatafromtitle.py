# Automatically generated by Pynguin.
import youtube_dl.postprocessor.metadatafromtitle as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'y|T=}|6{4[z?'
    int_0 = -397
    tuple_0 = (int_0,)
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(tuple_0, str_0)

def test_case_2():
    str_0 = '%(title)s'
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_0, str_0)
    str_1 = '%(artist)s - %(title)s'
    metadata_from_title_p_p_1 = module_0.MetadataFromTitlePP(str_1, str_1)

def test_case_3():
    str_0 = 'title'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(dict_0, str_0)
    var_0 = metadata_from_title_p_p_0.run(dict_0)