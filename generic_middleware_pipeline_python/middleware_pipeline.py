def run_middleware_pipeline(request, response, middlewares=[]):
    count = 0
    next_called = True
    while next_called and count < len(middlewares):
        next_called = run_middleware_step(request, response, middlewares[count])
        count += 1
    return request, response


def run_middleware_step(request, response, middleware):
    next_called = False

    def next():
        nonlocal next_called
        next_called = True

    middleware(request, response, next)
    return next_called
