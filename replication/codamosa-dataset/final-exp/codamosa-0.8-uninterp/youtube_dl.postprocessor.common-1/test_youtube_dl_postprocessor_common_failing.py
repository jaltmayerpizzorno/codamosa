# Automatically generated by Pynguin.
import youtube_dl.postprocessor.common as module_0

def test_case_0():
    try:
        post_processor_0 = module_0.PostProcessor()
        float_0 = -505.14
        int_0 = -1059
        var_0 = post_processor_0.run(int_0)
        audio_conversion_error_0 = module_0.AudioConversionError(float_0)
        int_1 = None
        str_0 = '2017-01-07_2100_tl_54_7DaysSat18_31295'
        str_1 = '8qkP/9'
        bytes_0 = b'\x1dls\xc8a\xf1F\xac(\x95h\xedRjc\xcbs'
        post_processor_1 = module_0.PostProcessor()
        audio_conversion_error_1 = module_0.AudioConversionError(int_1)
        post_processor_2 = module_0.PostProcessor(post_processor_1)
        post_processor_3 = module_0.PostProcessor()
        var_1 = post_processor_2.try_utime(int_1, str_0, str_1, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        post_processor_0 = module_0.PostProcessor()
        var_0 = post_processor_0.try_utime(post_processor_0, post_processor_0, post_processor_0)
    except BaseException:
        pass