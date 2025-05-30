from collections.abc import Hashable
import datetime
from typing import overload

import numpy as np
import pandas as pd
from pandas import Index
from pandas.core.indexes.accessors import PeriodIndexFieldOps
from pandas.core.indexes.datetimelike import DatetimeIndexOpsMixin
from pandas.core.indexes.timedeltas import TimedeltaIndex
from typing_extensions import Self

from pandas._libs.tslibs import (
    BaseOffset,
    NaTType,
    Period,
)
from pandas._libs.tslibs.period import _PeriodAddSub

class PeriodIndex(DatetimeIndexOpsMixin[pd.Period], PeriodIndexFieldOps):
    def __new__(
        cls,
        data=...,
        ordinal=...,
        freq=...,
        tz=...,
        dtype=...,
        copy: bool = ...,
        name: Hashable = ...,
        **fields,
    ): ...
    @property
    def values(self): ...
    def __contains__(self, key) -> bool: ...
    @overload
    def __sub__(self, other: Period) -> Index: ...
    @overload
    def __sub__(self, other: Self) -> Index: ...
    @overload
    def __sub__(self, other: _PeriodAddSub) -> Self: ...
    @overload
    def __sub__(self, other: NaTType) -> NaTType: ...
    @overload
    def __sub__(self, other: TimedeltaIndex | pd.Timedelta) -> Self: ...
    @overload  # type: ignore[override]
    def __rsub__(self, other: Period) -> Index: ...
    @overload
    def __rsub__(self, other: Self) -> Index: ...
    @overload
    def __rsub__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, other: NaTType
    ) -> NaTType: ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __array_wrap__(self, result, context=...): ...
    def asof_locs(self, where, mask): ...
    def astype(self, dtype, copy: bool = ...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    @property
    def is_full(self) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def get_indexer(self, target, method=..., limit=..., tolerance=...): ...
    def get_indexer_non_unique(self, target): ...
    def insert(self, loc, item): ...
    def join(
        self,
        other,
        *,
        how: str = ...,
        level=...,
        return_indexers: bool = ...,
        sort: bool = ...,
    ): ...
    def difference(self, other, sort=...): ...
    def memory_usage(self, deep: bool = ...): ...
    @property
    def freqstr(self) -> str: ...
    def shift(self, periods: int = ..., freq=...) -> Self:
        """
Shift index by desired number of time frequency increments.

This method is for shifting the values of datetime-like indexes
by a specified time increment a given number of times.

Parameters
----------
periods : int, default 1
    Number of periods (or increments) to shift by,
    can be positive or negative.
freq : pandas.DateOffset, pandas.Timedelta or string, optional
    Frequency increment to shift by.
    If None, the index is shifted by its own `freq` attribute.
    Offset aliases are valid strings, e.g., 'D', 'W', 'M' etc.

Returns
-------
pandas.DatetimeIndex
    Shifted index.

See Also
--------
Index.shift : Shift values of Index.
PeriodIndex.shift : Shift values of PeriodIndex.
        """
        pass

def period_range(
    start: (
        str | datetime.datetime | datetime.date | pd.Timestamp | pd.Period | None
    ) = ...,
    end: (
        str | datetime.datetime | datetime.date | pd.Timestamp | pd.Period | None
    ) = ...,
    periods: int | None = ...,
    freq: str | BaseOffset | None = ...,
    name: Hashable | None = ...,
) -> PeriodIndex: ...
