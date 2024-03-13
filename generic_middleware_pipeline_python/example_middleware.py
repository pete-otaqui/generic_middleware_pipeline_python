from .middleware_pipeline import run_middleware_pipeline


def null_middleware(request, response, next):
    next()


def mutate_count_and_call_next_middleware(request, response, next):
    if "mutate_and_call_next" not in response:
        response["mutate_and_call_next"] = 0
    response["mutate_and_call_next"] += 1
    next()


def mutate_count_only_middleware(request, response, next):
    if "mutate_only" not in response:
        response["mutate_only"] = 0
    response["mutate_only"] += 1


def child_pipeline_middleware(request, response, next):
    if "child_pipeline" not in response:
        response["child_pipeline"] = 0
    response["child_pipeline"] += 1

    def child_middleware1(request, response, next):
        if "child_middleware1" not in response:
            response["child_middleware1"] = 0
        response["child_middleware1"] += 1
        next()

    def child_middleware2(request, response, next):
        if "child_middleware2" not in response:
            response["child_middleware2"] = 0
        response["child_middleware2"] += 1
        next()

    run_middleware_pipeline(request, response, [child_middleware1, child_middleware2])
    next()
