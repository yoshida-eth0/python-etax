"""
抽象 社会保険
"""
from abc import ABCMeta, abstractmethod
from typing import Literal

都道府県名 = Literal['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']

class 標準額区分:
    def __init__(self, 等級: int|None, 月額: int):
        self.等級 = 等級
        self.月額 = 月額


class I社会保険(metaclass=ABCMeta):
    """
    定数データの抽象クラス
    社会保険
    厚生年金保険と健康保険で継承
    """
    @abstractmethod
    def 標準報酬額区分(self, 報酬月額: int) -> 標準額区分:
        """
        報酬月額に対応する標準報酬額の区分を返す
        """
        ...

    @abstractmethod
    def 標準賞与額区分(self, 賞与額: int) -> 標準額区分:
        """
        賞与額に対応する標準賞与額の区分を返す
        """
        ...
