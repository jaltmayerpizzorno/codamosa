# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    pass

def test_case_1():
    queue_full_0 = module_0.QueueFull()
    queue_0 = module_0.Queue()
    var_0 = queue_0.__aiter__()

def test_case_2():
    queue_0 = module_0.Queue()

def test_case_3():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()

def test_case_4():
    queue_0 = module_0.Queue()
    bool_0 = queue_0.empty()

def test_case_5():
    var_0 = None
    queue_0 = module_0.Queue()
    queue_0.put_nowait(var_0)

def test_case_6():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__repr__()

def test_case_7():
    priority_queue_0 = module_0.PriorityQueue()
    queue_0 = module_0.Queue()
    bool_0 = queue_0.empty()

def test_case_8():
    queue_0 = module_0.Queue()
    bool_0 = queue_0.full()
    var_0 = None
    queue_0.put_nowait(var_0)
    str_0 = queue_0.__str__()
    str_1 = queue_0.__str__()
    var_1 = queue_0.get_nowait()
    queue_0.put_nowait(var_1)
    queue_1 = module_0.Queue()
    str_2 = queue_1.__repr__()