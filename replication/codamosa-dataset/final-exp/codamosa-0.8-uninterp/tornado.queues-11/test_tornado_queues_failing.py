# Automatically generated by Pynguin.
import tornado.queues as module_0
import datetime as module_1

def test_case_0():
    try:
        list_0 = []
        queue_full_0 = module_0.QueueFull(*list_0)
        queue_iterator_0 = module_0._QueueIterator(queue_full_0)
        awaitable_0 = queue_iterator_0.__anext__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -4226
        queue_0 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_3():
    try:
        queue_0 = module_0.Queue()
        bool_0 = queue_0.full()
        bool_1 = queue_0.empty()
        int_0 = -492
        var_0 = queue_0.__aiter__()
        str_0 = queue_0.__str__()
        dict_0 = {}
        dict_1 = {str_0: dict_0, str_0: bool_0}
        queue_iterator_0 = module_0._QueueIterator(dict_1)
        queue_full_0 = module_0.QueueFull()
        priority_queue_0 = module_0.PriorityQueue(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        queue_0 = module_0.Queue()
        awaitable_0 = queue_0.get()
    except BaseException:
        pass

def test_case_5():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()
        str_1 = queue_0.__repr__()
        int_0 = queue_0.qsize()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 934
        queue_0 = module_0.Queue(int_0)
        str_0 = queue_0.__repr__()
        str_1 = 'CGp%O|#gfk\x0c7weg\tfW>y'
        list_0 = [str_1]
        queue_1 = module_0.Queue()
        awaitable_0 = queue_1.join(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 384
        lifo_queue_0 = module_0.LifoQueue(int_0)
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        var_0 = queue_0.__aiter__()
        queue_1 = module_0.Queue()
        priority_queue_0 = module_0.PriorityQueue(int_0)
        var_1 = queue_1.get_nowait()
    except BaseException:
        pass

def test_case_8():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = queue_0.get_nowait()
        timedelta_0 = module_1.timedelta()
        future_0 = queue_0.put(var_1, timedelta_0)
    except BaseException:
        pass

def test_case_9():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = queue_0.get_nowait()
        timedelta_0 = module_1.timedelta()
        var_2 = queue_0.__aiter__()
        int_0 = None
        queue_1 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        queue_0 = module_0.Queue()
        var_0 = None
        queue_0.put_nowait(var_0)
        timedelta_0 = module_1.timedelta()
        str_0 = queue_0.__str__()
        int_0 = 1384
        queue_1 = module_0.Queue(int_0)
        queue_2 = module_0.Queue()
        var_1 = queue_1.get_nowait()
    except BaseException:
        pass

def test_case_11():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()
        var_0 = None
        queue_0.put_nowait(var_0)
        timedelta_0 = module_1.timedelta()
        var_1 = queue_0.__aiter__()
        queue_1 = module_0.Queue()
        queue_1.put_nowait(var_0)
        queue_1.task_done()
        bool_0 = queue_1.full()
        var_2 = queue_1.get_nowait()
        future_0 = queue_0.put(var_2)
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = None
        int_0 = 5029
        queue_0 = module_0.Queue(int_0)
        queue_0.put_nowait(var_0)
        var_1 = queue_0.__aiter__()
        queue_1 = module_0.Queue(int_0)
        queue_2 = module_0.Queue()
        var_2 = queue_0.get_nowait()
        queue_0.put_nowait(var_2)
        queue_0.task_done()
        priority_queue_0 = module_0.PriorityQueue()
        bool_0 = queue_0.full()
        queue_3 = module_0.Queue()
        var_3 = queue_1.get_nowait()
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 2
        queue_0 = module_0.Queue(int_0)
        int_1 = 3
        queue_0.put_nowait(int_1)
        str_0 = 'It is ok to put nowait when queue is not full'
        var_0 = print(str_0)
        int_2 = 4
        queue_0.put_nowait(int_2)
        str_1 = 'It is ok to put nowait when queue is not full'
        var_1 = print(str_1)
        int_3 = 5
        queue_0.put_nowait(int_3)
    except BaseException:
        pass