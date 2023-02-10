import datetime


def logger(old_function):

    def new_function(*args, **kwargs):
        function_call_time = str(datetime.datetime.now())
        f = open('main.log', 'a')
        f.write(f'{function_call_time}\n{old_function.__name__}\n')
        f.close()
        for i in args:
            f = open('main.log', 'a')
            f.write(f'{i}\n')
            f.close()
        for i_1 in kwargs.values():
            f = open('main.log', 'a')
            f.write(f'{i_1}\n')
            f.close()
        result = old_function(*args, **kwargs)
        f = open('main.log', 'a')
        f.write(f'{result}\n')
        f.close()
        return result
    return new_function
