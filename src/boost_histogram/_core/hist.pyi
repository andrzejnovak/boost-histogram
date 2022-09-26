from __future__ import annotations

from typing import Any, ClassVar, Iterable, Iterator, Tuple, Type, TypeVar

import numpy as np
from numpy.typing import ArrayLike

from . import accumulators, axis, storage
from .axis import transform

T = TypeVar("T", bound="_BaseHistogram")

_axes_limit: int

class _BaseHistogram:
    _storage_type: ClassVar[Type[storage._BaseStorage]]
    # Note that storage has a default simply because subclasses always handle it.
    def __init__(
        self, axis: list[axis._BaseAxis], storage: storage._BaseStorage = ...
    ) -> None: ...
    def rank(self) -> int: ...
    def size(self) -> int: ...
    def reset(self) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __copy__(self: T) -> T: ...
    def __deepcopy__(self: T, memo: Any) -> T: ...
    def __iadd__(self: T, other: _BaseHistogram) -> T: ...
    def to_numpy(self, flow: bool = ...) -> Tuple["np.typing.NDArray[Any]", ...]: ...
    def view(self, flow: bool = ...) -> "np.typing.NDArray[Any]": ...
    def axis(self, i: int = ...) -> axis._BaseAxis: ...
    def fill(
        self,
        *args: ArrayLike,
        weight: ArrayLike | None = ...,
        sample: ArrayLike | None = ...,
    ) -> None: ...
    def empty(self, flow: bool = ...) -> bool: ...
    def reduce(self: T, *args: Any) -> T: ...
    def project(self: T, *args: int) -> T: ...
    def sum(self, flow: bool = ...) -> Any: ...
    def at(self, *args: int) -> Any: ...

class any_int64(_BaseHistogram):
    def __idiv__(self: T, other: any_int64) -> T: ...
    def __imul__(self: T, other: any_int64) -> T: ...
    def at(self, *args: int) -> int: ...
    def _at_set(self, value: int, *args: int) -> None: ...
    def sum(self, flow: bool = ...) -> int: ...

class any_unlimited(_BaseHistogram):
    def __idiv__(self: T, other: any_unlimited) -> T: ...
    def __imul__(self: T, other: any_unlimited) -> T: ...
    def at(self, *args: int) -> float: ...
    def _at_set(self, value: float, *args: int) -> None: ...
    def sum(self, flow: bool = ...) -> float: ...

class any_double(_BaseHistogram):
    def __idiv__(self: T, other: any_double) -> T: ...
    def __imul__(self: T, other: any_double) -> T: ...
    def at(self, *args: int) -> float: ...
    def _at_set(self, value: float, *args: int) -> None: ...
    def sum(self, flow: bool = ...) -> float: ...

class any_atomic_int64(_BaseHistogram):
    def __idiv__(self: T, other: any_atomic_int64) -> T: ...
    def __imul__(self: T, other: any_atomic_int64) -> T: ...
    def at(self, *args: int) -> int: ...
    def _at_set(self, value: int, *args: int) -> None: ...
    def sum(self, flow: bool = ...) -> int: ...

class any_weight(_BaseHistogram):
    def __idiv__(self: T, other: any_weight) -> T: ...
    def __imul__(self: T, other: any_weight) -> T: ...
    def at(self, *args: int) -> accumulators.WeightedSum: ...
    def _at_set(self, value: accumulators.WeightedSum, *args: int) -> None: ...
    def sum(self, flow: bool = ...) -> accumulators.WeightedSum: ...

class any_mean(_BaseHistogram):
    def at(self, *args: int) -> accumulators.Mean: ...
    def _at_set(self, value: accumulators.Mean, *args: int) -> None: ...
    def sum(self, flow: bool = ...) -> accumulators.Mean: ...
    def fill(
        self,
        *args: ArrayLike,
        weight: ArrayLike | None = ...,
        sample: ArrayLike | None = ...,
    ) -> None: ...

class any_weighted_mean(_BaseHistogram):
    def at(self, *args: int) -> accumulators.WeightedMean: ...
    def _at_set(self, value: accumulators.WeightedMean, *args: int) -> None: ...
    def sum(self, flow: bool = ...) -> accumulators.WeightedMean: ...
    def fill(
        self,
        *args: ArrayLike,
        weight: ArrayLike | None = ...,
        sample: ArrayLike | None = ...,
    ) -> None: ...
