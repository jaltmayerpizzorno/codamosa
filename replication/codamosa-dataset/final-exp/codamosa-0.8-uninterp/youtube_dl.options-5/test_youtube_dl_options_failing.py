# Automatically generated by Pynguin.
import youtube_dl.options as module_0

def test_case_0():
    try:
        str_0 = 'https?://live\\.line\\.me/channels/(?P<id>\\d+)(?!/broadcast/\\d+)(?:[/?&#]|$)'
        var_0 = module_0.parseOpts(str_0)
    except BaseException:
        pass