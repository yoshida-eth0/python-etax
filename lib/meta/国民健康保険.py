"""
抽象 国民健康保険
"""
from abc import ABCMeta, abstractmethod


class 国民健康保険料率区分:
    """
    国民健康保険料率 区分
    """
    def __init__(self, 区分: str, 対象年齢: range, 均等割: int, 所得割: float, 最高限度額: int):
        self.区分 = 区分
        self.対象年齢 = 対象年齢
        self.均等割 = 均等割
        self.所得割 = 所得割
        self.最高限度額 = 最高限度額


class I国民健康保険(metaclass=ABCMeta):
    """
    定数データの抽象クラス
    国民健康保険
    """
    @abstractmethod
    def 国民健康保険料率区分一覧(self, 地域: int) -> list[国民健康保険料率区分]:
        """
        国民健康保険料率区分一覧
        """
        ...

    @abstractmethod
    def 低所得世帯軽減割合(self, 総所得金額等の合計: int) -> float:
        """
        低所得世帯軽減割合
        """
        ...
