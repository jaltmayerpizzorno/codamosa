# Automatically generated by Pynguin.
import tornado.httpclient as module_0
import tornado.ioloop as module_1

def test_case_0():
    pass

def test_case_1():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_2():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_3():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://ww.google.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)

def test_case_4():
    int_0 = -1186
    dict_0 = {int_0: int_0}
    list_0 = [dict_0, int_0, int_0]
    h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0, list_0)
    str_0 = h_t_t_p_client_error_0.__str__()

def test_case_5():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://ww.googqe.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    h_t_t_p_response_0.rethrow()
    h_t_t_p_client_0.close()

def test_case_6():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://ww.google.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    var_0 = h_t_t_p_response_0.body
    var_1 = print(h_t_t_p_response_0)
    h_t_t_p_client_1 = module_0.HTTPClient()
    h_t_t_p_client_0.close()

def test_case_7():
    bool_0 = False
    i_o_loop_0 = module_1.IOLoop()
    i_o_loop_0.make_current()
    async_h_t_t_p_client_0 = module_0.AsyncHTTPClient()
    async_h_t_t_p_client_0.close()
    async_h_t_t_p_client_0.close()
    async_h_t_t_p_client_0.close()
    async_h_t_t_p_client_0.close()
    async_h_t_t_p_client_0.close()
    async_h_t_t_p_client_0.close()

def test_case_8():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://ww.google.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    var_0 = h_t_t_p_response_0.body