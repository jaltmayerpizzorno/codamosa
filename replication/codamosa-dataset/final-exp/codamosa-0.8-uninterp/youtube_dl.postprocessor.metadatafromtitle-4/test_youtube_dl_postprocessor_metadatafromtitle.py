# Automatically generated by Pynguin.
import youtube_dl.postprocessor.metadatafromtitle as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '_.#>5km[p*hn$'
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_0, str_0)

def test_case_2():
    str_0 = 'm>Z7\x0b9r'
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_0, str_0)
    var_0 = metadata_from_title_p_p_0.format_to_regex(str_0)

def test_case_3():
    var_0 = None
    str_0 = '%(title)s - %(artist)s'
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(var_0, str_0)

def test_case_4():
    str_0 = 'The.Big.Bang.Theory.S03E01.HDTV.XviD-LOL.avi'
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_0, str_0)
    str_1 = 'title'
    str_2 = {str_1: str_0}
    var_0 = metadata_from_title_p_p_0.run(str_2)