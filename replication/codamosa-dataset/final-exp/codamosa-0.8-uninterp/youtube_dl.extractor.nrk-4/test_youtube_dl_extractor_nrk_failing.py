# Automatically generated by Pynguin.
import youtube_dl.extractor.nrk as module_0

def test_case_0():
    try:
        str_0 = None
        n_r_k_t_v_direkte_i_e_0 = module_0.NRKTVDirekteIE(str_0)
        str_1 = 'https://tv.nrk.no/serie/blank'
        str_2 = 'entries'
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        var_0 = var_1._real_extract(str_1)[str_2]
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'https://tv.nrk.no/serie/blank'
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        var_0 = var_1._real_extract(str_0)[str_0]
    except BaseException:
        pass

def test_case_2():
    try:
        n_r_k_radio_podkast_i_e_0 = module_0.NRKRadioPodkastIE()
        n_r_k_t_v_episode_i_e_0 = module_0.NRKTVEpisodeIE(n_r_k_radio_podkast_i_e_0)
        str_0 = 'https://tv.nrk.no/serie/blank'
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        var_0 = var_1._real_extract(str_0)[str_0]
    except BaseException:
        pass

def test_case_3():
    try:
        n_r_k_skole_i_e_0 = module_0.NRKSkoleIE()
        n_r_k_t_v_episodes_i_e_0 = module_0.NRKTVEpisodesIE(n_r_k_skole_i_e_0)
        set_0 = {n_r_k_t_v_episodes_i_e_0, n_r_k_t_v_episodes_i_e_0, n_r_k_t_v_episodes_i_e_0, n_r_k_t_v_episodes_i_e_0}
        n_r_k_t_v_serie_base_i_e_0 = module_0.NRKTVSerieBaseIE(set_0)
        str_0 = 'https://tv.nrk.no/serie/blank'
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        var_0 = var_1._real_extract(str_0)[n_r_k_t_v_series_i_e_0]
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'https://tv.nrk.no/serie/blank'
        n_r_k_skole_i_e_0 = module_0.NRKSkoleIE()
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        n_r_k_t_v_season_i_e_0 = module_0.NRKTVSeasonIE()
        var_0 = var_1._real_extract(str_0)[str_0]
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'https://tv.nrk.no/serie/blank'
        n_r_k_t_v_season_i_e_0 = module_0.NRKTVSeasonIE()
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        var_0 = var_1._real_extract(str_0)[n_r_k_t_v_series_i_e_0]
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'https://tv.nrk.no/serie/blank'
        n_r_k_i_e_0 = module_0.NRKIE()
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        var_0 = var_1._real_extract(str_0)[str_0]
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ':t'
        n_r_k_radio_podkast_i_e_0 = module_0.NRKRadioPodkastIE(str_0)
        set_0 = {n_r_k_radio_podkast_i_e_0}
        n_r_k_skole_i_e_0 = module_0.NRKSkoleIE(set_0)
        str_1 = 'https://tv.nrk.no/serie/blank'
        n_r_k_t_v_series_i_e_0 = module_0.NRKTVSeriesIE()
        var_0 = var_1._real_extract(str_1)[n_r_k_t_v_series_i_e_0]
    except BaseException:
        pass