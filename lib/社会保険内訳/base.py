from abc import ABCMeta, abstractmethod


class 種類別保険料(metaclass=ABCMeta):
    @property
    @abstractmethod
    def 被保険者負担額(self) -> int:
        """
        被保険者が負担する総額
        """
        ...

    @property
    @abstractmethod
    def 事業主負担額(self) -> int:
        """
        事業主が負担する総額
        """
        ...


class 社会保険Base:
    def __init__(self):
        # 種類別の保険料
        self.月額保険料: 種類別保険料
        self.賞与額保険料: 種類別保険料

    @property
    def 被保険者負担額(self) -> int:
        """
        被保険者が負担する総額
        """
        return self.月額保険料.被保険者負担額 + self.賞与額保険料.被保険者負担額

    @property
    def 事業主負担額(self) -> int:
        """
        事業主が負担する総額
        """
        return self.月額保険料.事業主負担額  + self.賞与額保険料.事業主負担額
