# Generic Middleware Pipeline

This is a generic middleware pipeline that can be used to create a pipeline of
middleware functions that can be used to process a request and response.

It is purely an example project.

## Installation

This project is managed with [poetry](https://python-poetry.org/)

```bash
poetry install # install pytest

poetry run pytest # run tests
```

## About the middleware pipeline

Each middleware function will receive three parameters:

- `req`: The request object, which may be mutated by the middleware function
- `res`: The response object, which may be mutated by the middleware function
- `next`: The next middleware function in the pipeline

If the middleware function does not call `next()`, the pipeline will not continue.

Here is an example of how to use the middleware pipeline:

```python
from generic_middleware_pipeline import run_middleware_pipeline

def middleware1(req, res, next):
    if req['some_condition']:
        res['some_value'] = 'some_value'
        # in this case we will allow the pipeline to continue
        next()
    else:
        # in this case we will not allow the pipeline to continue
        res['some_value'] = 'some_other_value'

def middleware2(req, res, next):
    # Do something, and then allow the pipeline to continue
    res['mutated_by_m2'] = True
    next()

# note that we _mutate_ the `req` and `res` that are passed in.
# this method of using the response is just for convenience.
req, res = run_middleware_pipeline({}, {}, [
    middleware1,
    middleware2
])
```

You can easily create a middleware that itself calls a pipeline of middleware
functions.

```python
from generic_middleware_pipeline import run_middleware_pipeline

def child1(req, res, next):
    # Do something
    next()

def child2(req, res, next):
    # Do something
    next()

def my_child_pipeline_middleware(req, res, next):
    run_middleware_pipeline(req, res, [
        child_1,
        child_2
    ])
```
