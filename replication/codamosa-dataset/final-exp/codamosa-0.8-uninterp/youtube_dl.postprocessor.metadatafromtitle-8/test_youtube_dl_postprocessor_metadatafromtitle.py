# Automatically generated by Pynguin.
import youtube_dl.postprocessor.metadatafromtitle as module_0

def test_case_0():
    pass

def test_case_1():
    metadata_from_title_p_p_0 = None
    str_0 = ''
    metadata_from_title_p_p_1 = module_0.MetadataFromTitlePP(metadata_from_title_p_p_0, str_0)
    metadata_from_title_p_p_2 = module_0.MetadataFromTitlePP(metadata_from_title_p_p_1, str_0)

def test_case_2():
    str_0 = 'title'
    str_1 = {str_0: str_0}
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_0, str_0)
    var_0 = metadata_from_title_p_p_0.run(str_1)