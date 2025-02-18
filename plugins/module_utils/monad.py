# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2024 Kirill Satarin (@kksat)
#
# Copyright 2024 Kirill Satarin (@kksat)
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from typing import Callable, Any, Union, TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar("T")
S = TypeVar("S")
F = TypeVar("F")
J = TypeVar("J")


class Monoid(ABC):
    pass


class Functor(Monoid, Generic[T]):
    pass


class Applicative(Functor):
    pass


class Monad(Applicative):
    @abstractmethod
    def __init__(self, *args, **kvargs):
        """Monad class."""
        pass

    @abstractmethod
    def bind(self, func) -> "Monad":
        pass

    @abstractmethod
    def apply(self, func: Any) -> Any:
        pass

    @abstractmethod
    def map(self, func: Callable) -> "Monad":
        pass

    def then(self, func):
        return self.bind(func)

    def items(self):
        return self.__dict__.items()


class Maybe(Monad, Generic[J]):
    @abstractmethod
    def is_just(self) -> bool:
        pass

    @abstractmethod
    def is_nothing(self) -> bool:
        pass

    def bind(
        self: "Maybe[J]", func: Callable[[J], "Maybe[T]"]
    ) -> "Union[Maybe[T], Maybe[J]]":
        if self.is_just():
            result = func(self.value)
            if isinstance(result, Maybe):
                return result
            else:
                return Just(result)
        return self

    def map(self: "Maybe[J]", func: Callable[[J], T]) -> "Union[Maybe[T],Maybe[J]]":
        if self.is_just():
            return Just(func(self.value))
        return self

    def apply(
        self: "Maybe[J]", func: "Union[Maybe[Callable[[J],Any]], Nothing]"
    ) -> "Union[Just[J], Nothing]":
        if self.is_just() and func.is_just():
            return Just(func.value(self.value))
        if self.is_nothing():
            return self
        return func


class Just(Maybe[J]):
    def __init__(self, value: J):
        """Just instance of Maybe."""
        self.value = value

    def is_just(self) -> bool:
        return True

    def is_nothing(self) -> bool:
        return False


class Nothing(Maybe[J]):
    def __init__(self):
        """Nothing instance of Maybe."""
        pass

    def is_just(self) -> bool:
        return False

    def is_nothing(self) -> bool:
        return True


class Result(Monad, Generic[S, F]):
    def __init__(
        self,
        value,
    ):
        """Result monad."""
        self.value = value

    @property
    def result(
        self,
    ):
        return self.value

    @abstractmethod
    def is_success(self) -> bool:
        pass

    @abstractmethod
    def is_failure(self) -> bool:
        pass

    def bind(
        self: "Result[S, F]", func: Callable[[T], "Result[S,F]"]
    ) -> "Result[S, F]":
        if self.is_success():
            result = func(self.value)
            if isinstance(result, Result):
                return result
            else:
                return Success(result)
        return self

    def apply(self, func: "Result[S, F]") -> "Result[S, F]":
        if self.is_success() and func.is_success():
            return Success(func.value(self.value))
        return self if self.is_failure() else func

    def map(self, func: Callable[[Any], Any]) -> "Result[S, F]":
        if self.is_success():
            return Success(func(self.value))
        return self


class Success(Result):
    def is_success(self):
        return True

    def is_failure(self):
        return False


class Failure(Result):
    def is_success(self):
        return False

    def is_failure(self):
        return True


def changed(attribute: str) -> Callable:
    def f(result: dict) -> dict:
        return {"changed": True, attribute: result}

    return f


def same(attribute: str) -> Callable:
    def f(result) -> dict:
        return {"changed": False, attribute: result}

    return f


def liftA2(func: Callable, a: Result, b: Result) -> Result:
    if a.is_success() and b.is_success():
        return Success(func(a.value, b.value))
    return a if a.is_failure() else b
