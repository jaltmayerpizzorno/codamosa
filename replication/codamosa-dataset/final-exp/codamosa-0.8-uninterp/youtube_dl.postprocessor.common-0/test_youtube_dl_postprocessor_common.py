# Automatically generated by Pynguin.
import youtube_dl.postprocessor.common as module_0

def test_case_0():
    pass

def test_case_1():
    post_processor_0 = module_0.PostProcessor()

def test_case_2():
    bool_0 = False
    post_processor_0 = module_0.PostProcessor()
    var_0 = post_processor_0.set_downloader(bool_0)
    post_processor_1 = module_0.PostProcessor()

def test_case_3():
    bool_0 = False
    str_0 = 'O>?Hix\n6H'
    audio_conversion_error_0 = module_0.AudioConversionError(str_0)
    post_processor_0 = module_0.PostProcessor(audio_conversion_error_0)
    var_0 = post_processor_0.run(bool_0)