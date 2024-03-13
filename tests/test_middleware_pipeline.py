import pytest
from generic_middleware_pipeline_python import run_middleware_pipeline
from generic_middleware_pipeline_python.example_middleware import (
    null_middleware,
    mutate_count_and_call_next_middleware,
    mutate_count_only_middleware,
    child_pipeline_middleware,
)


def test_no_middleware():
    req = {}
    res = {}
    middlewares = []
    run_middleware_pipeline(req, res, middlewares)
    assert res == {}


def test_null_middleware():
    req = {}
    res = {}
    middlewares = [null_middleware]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {}


def test_mutate_count_and_call_next_middleware():
    req = {}
    res = {}
    middlewares = [mutate_count_and_call_next_middleware]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {"mutate_and_call_next": 1}


def test_mutate_count_only_middleware():
    req = {}
    res = {}
    middlewares = [mutate_count_only_middleware]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {"mutate_only": 1}


def test_next_then_not_next():
    req = {}
    res = {}
    middlewares = [mutate_count_and_call_next_middleware, mutate_count_only_middleware]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {"mutate_and_call_next": 1, "mutate_only": 1}


def test_not_next_then_next():
    req = {}
    res = {}
    middlewares = [mutate_count_only_middleware, mutate_count_and_call_next_middleware]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {"mutate_only": 1}


def test_multiple_mutations():
    req = {}
    res = {}
    middlewares = [
        mutate_count_and_call_next_middleware,
        mutate_count_and_call_next_middleware,
    ]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {"mutate_and_call_next": 2}


def test_child_pipeline_middleware():
    req = {}
    res = {}
    middlewares = [child_pipeline_middleware]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {"child_middleware1": 1, "child_middleware2": 1, "child_pipeline": 1}


def test_next_then_child_pipeline():
    req = {}
    res = {}
    middlewares = [mutate_count_and_call_next_middleware, child_pipeline_middleware]
    run_middleware_pipeline(req, res, middlewares)
    assert res == {
        "mutate_and_call_next": 1,
        "child_middleware1": 1,
        "child_middleware2": 1,
        "child_pipeline": 1,
    }
