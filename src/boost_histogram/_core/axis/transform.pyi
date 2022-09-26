from __future__ import annotations

from typing import Any, Callable, TypeVar

T = TypeVar("T", bound="_BaseTransform")

def _log_fn(arg0: float) -> float: ...
def _exp_fn(arg0: float) -> float: ...
def _sqrt_fn(arg0: float) -> float: ...
def _sq_fn(arg0: float) -> float: ...

class _BaseTransform:
    def forward(self, arg0: float) -> float: ...
    def reverse(self, arg0: float) -> float: ...
    def __repr__(self) -> str: ...
    def __copy__(self: T) -> T: ...
    def __deepcopy__(self: T, memo: Any) -> T: ...

class id(_BaseTransform): ...
class sqrt(_BaseTransform): ...
class log(_BaseTransform): ...

class pow(_BaseTransform):
    def __init__(self, power: float) -> None: ...
    @property
    def power(self) -> float: ...

class func_transform(_BaseTransform):
    def __init__(
        self,
        forward: Callable[[float], float],
        inverse: Callable[[float], float],
        convert: Callable[[float], float],
        name: str,
    ) -> None: ...
