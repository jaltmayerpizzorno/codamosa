# Automatically generated by Pynguin.
import youtube_dl.extractor.itv as module_0

def test_case_0():
    try:
        bytes_0 = b"(\xd0\xdeq\xfb\xe9\x02\xe1\x0c'\xfa\xb7\xeb\xc8B\x90k\x96\xe4"
        i_t_v_i_e_0 = module_0.ITVIE()
        i_t_v_i_e_1 = module_0.ITVIE(bytes_0)
        str_0 = 'https://www.itv.com/hub/liar/2a4547a0012'
        str_1 = 'title'
        i_t_v_i_e_2 = module_0.ITVIE()
        var_0 = var_1._real_extract(str_0)[str_1]
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"(\xd0\xdeq\xfb\xe9\x02\xe1\x0c'\xfa\xb7\xeb\xc8B\x90k\x96\xe4"
        i_t_v_b_t_c_c_i_e_0 = module_0.ITVBTCCIE()
        i_t_v_i_e_0 = module_0.ITVIE()
        i_t_v_i_e_1 = module_0.ITVIE(bytes_0)
        str_0 = 'https://www.itv.com/hub/liar/2a4547a0012'
        str_1 = 'title'
        i_t_v_i_e_2 = module_0.ITVIE()
        var_0 = var_1._real_extract(str_0)[str_1]
    except BaseException:
        pass