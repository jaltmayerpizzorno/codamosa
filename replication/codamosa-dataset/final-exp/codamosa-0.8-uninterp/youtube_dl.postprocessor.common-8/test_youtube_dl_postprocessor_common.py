# Automatically generated by Pynguin.
import youtube_dl.postprocessor.common as module_0

def test_case_0():
    pass

def test_case_1():
    post_processor_0 = module_0.PostProcessor()

def test_case_2():
    float_0 = -1261.782356
    audio_conversion_error_0 = module_0.AudioConversionError(float_0)
    float_1 = 901.326
    dict_0 = {float_1: audio_conversion_error_0, float_1: audio_conversion_error_0, float_0: float_1, float_0: float_1}
    post_processor_0 = module_0.PostProcessor()
    var_0 = post_processor_0.set_downloader(dict_0)

def test_case_3():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    post_processor_0 = module_0.PostProcessor()
    var_0 = post_processor_0.run(set_0)