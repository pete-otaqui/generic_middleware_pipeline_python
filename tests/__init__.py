import pytest
from generic_middleware_pipeline_python import run_middleware_pipeline

def test_no_middleware():
    req = {}
    res = {}
    middlewares = []
    run_middleware_pipeline(req, res, middlewares)
    assert res == {}

def test_null_middleware():
    pass

def test_mutate_count_and_call_next_middleware():
    pass

def test_mutate_count_only_middleware():
    pass

def test_next_then_not_next():
    pass

def test_not_next_then_next():
    pass

def test_multiple_mutations():
    pass

def test_child_pipeline_middleware():
    pass

def test_next_then_child_pipeline():
    pass