"""
抽象 住民税
"""
from abc import ABCMeta, abstractmethod


class I住民税_基礎控除(metaclass=ABCMeta):
    """
    定数データの抽象クラス
    住民税 基礎控除
    """
    @abstractmethod
    def 住民税_基礎控除(self, 合計所得金額: int) -> int:
        """
        合計所得金額に対応する住民税の基礎控除額を返す
        """
        ...

class 住民税の税率:
    """
    住民税の税率区分
    """
    def __init__(self, 区分: str, 所得割: float, 均等割: int, 定額減税: int = 0):
        self.区分 = 区分
        self.所得割 = 所得割
        self.均等割 = 均等割
        self.定額減税 = 定額減税

class I住民税_税率一覧(metaclass=ABCMeta):
    """
    定数データの抽象クラス
    住民税 住民税の税率一覧
    """
    @abstractmethod
    def 住民税の税率一覧(self) -> list[住民税の税率]:
        """
        住民税の税率の一覧を返す
        特別区民税と都民税など
        """
        ...

    @abstractmethod
    def 住民税_定額減税対象可否(self, 合計所得金額: int) -> bool:
        """
        合計所得金額をもとに定額減税の対象者か否かを返す
        """
        ...
