from typing import Callable
from fastapi import Request

def get_cache_key(
    func: Callable,
    namespace: str = "",
    request: Request = None,
    *args,
    **kwargs,
) -> str:
    prefix = f"{namespace}:{func.__module__}:{func.__name__}"
    if request:
        return f"{prefix}:{request.url.path}:{request.query_params}"
    return prefix 