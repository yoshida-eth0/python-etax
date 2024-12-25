"""
抽象 所得税
"""
from abc import ABCMeta, abstractmethod


class I所得税_基礎控除(metaclass=ABCMeta):
    """
    定数データの抽象クラス
    所得税 基礎控除
    """
    @abstractmethod
    def 所得税_基礎控除(self, 所得金額等_合計: int) -> int:
        """
        所得金額等の合計に対応する所得税の基礎控除額を返す
        """
        ...


class 所得税の税率:
    """
    所得税の税率

    No.2260 所得税の税率｜国税庁
    https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm
    """
    def __init__(self, 税率: float, 控除額: int, 復興特別所得税率: float = 0.0):
        self.税率 = 税率
        self.控除額 = 控除額
        self.復興特別所得税率 = 復興特別所得税率

class I所得税_税率(metaclass=ABCMeta):
    """
    定数データの抽象クラス
    所得税 所得税の税率
    """
    @abstractmethod
    def 所得税の税率(self, 課税される所得金額: int) -> 所得税の税率:
        """
        課税される所得金額に対応するオブジェクトを返す
        """
        ...
