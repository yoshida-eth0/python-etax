"""
抽象 給与所得控除
"""
from abc import ABCMeta, abstractmethod
from typing import Protocol


class 給与所得控除後の金額Protocol(Protocol):
    def __call__(self, 給与等の収入金額: int) -> int:
        """
        給与等の収入金額から給与所得控除後の金額を算出する
        """
        ...


class I給与所得控除(metaclass=ABCMeta):
    """
    定数データの抽象クラス
    給与所得控除
    """
    @abstractmethod
    def 給与所得控除後の金額の式(self, 給与等の収入金額: int) -> 給与所得控除後の金額Protocol:
        """
        給与等の収入金額に対応する給与所得控除後の金額の式を返す
        """
        ...

