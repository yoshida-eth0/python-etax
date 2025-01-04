from enum import Enum

from meta.社会保険 import 事業の種類名, 都道府県名


class 障害(Enum):
    """
    障害
    """
    なし = 0
    障害者 = 1
    特別障害者 = 2
    同居特別障害者 = 3


class 人物:
    def __init__(self):
        self.年齢: int = None
        self.障害 = 障害.なし

class 納税者本人(人物):
    """
    納税者本人
    """
    def __init__(self):
        super().__init__()

        # 勤労学生
        #
        # 参考:
        #   No.1175 勤労学生控除｜国税庁
        #   https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1175.htm
        self.is_勤労学生 = False

class 扶養親族(人物):
    """
    扶養親族
    """
    def __init__(self):
        super().__init__()
        self.合計所得: int = 0
        self.is_給与所得のみ: bool = True
        self.is_事業専従者: bool = False
        self.is_他の方の扶養親族: bool = False

class 配偶者(扶養親族):
    """
    配偶者
    """
    def __init__(self):
        super().__init__()
        self.is_一方の配偶者がこの控除を受けている: bool = False


class 雑損:
    def __init__(self):
        self.損失金額: int = 0
        self.保険金などで補填される金額: int = 0


class 医療費:
    def __init__(self):
        self.医療費の実質負担額: int = 0
        self.スイッチOTC医薬品の実質負担額: int = 0


class 納税者:
    """
    所得税や住民税の控除額を算出する際に用いる納税者の情報
    """
    def __init__(self):
        """
        控除
        """
        # 社会保険料
        # 支払った金額
        self.社会保険料: int = 0

        # 小規模企業共済等掛金
        # 支払った金額
        self.小規模企業共済等掛金: int = 0

        # 生命保険料
        # 支払った金額
        self.生命保険料: int = 0

        # 地震保険料
        # 支払った金額
        self.地震保険料: int = 0

        # 寡婦
        #
        # 参考:
        #   No.1170 寡婦控除｜国税庁
        #   https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1170.htm
        self.is_寡婦: bool = False

        # ひとり親
        #
        # 参考:
        #   No.1171 ひとり親控除｜国税庁
        #   https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1171.htm
        self.is_ひとり親: bool = False

        # 本人
        self.納税者本人 = 納税者本人()

        # 配偶者
        #
        # 参考:
        #   No.1191 配偶者控除｜国税庁
        #   https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1191.htm
        #
        #   No.1195 配偶者特別控除｜国税庁
        #   https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1195.htm
        self.配偶者: 配偶者|None = None

        # 扶養親族一覧
        #
        # 参考:
        #   No.1180 扶養控除｜国税庁
        #   https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1180.htm
        self.扶養親族一覧: list[扶養親族] = []

        # 雑損
        self.雑損: 雑損 = 雑損()

        # 医療費
        self.医療費: 医療費 = 医療費()

        # ふるさと納税額(実質負担額2,000円を含む額)
        self.ふるさと納税額: int = 0
        self.is_ワンストップ特例制度: bool = False

        # 支払済の予定納税額
        self.予定納税額_第1期分: int = 0
        self.予定納税額_第2期分: int = 0

        """
        社会保険
        """
        # 健康保険
        # 事業所所在地
        self.事業所所在地: 都道府県名

        # 雇用保険
        # 事業の種類
        self.事業の種類: 事業の種類名 = '一般の事業'

        """
        国民健康保険
        """
        # 自治体
        self.国民健康保険_加入地域: str

    @property
    def 障害者一覧(self) -> list[人物]:
        """
        障害者

        参考:
            No.1160 障害者控除｜国税庁
            https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1160.htm
        """
        people = [self.納税者本人, self.配偶者] + self.扶養親族一覧
        people = [person for person in people if person is not None]
        people = [person for person in people if person.障害!=障害.なし]
        return people

    @property
    def 控除対象配偶者又は扶養親族の人数(self) -> int:
        """
        控除対象配偶者又は扶養親族(非居住者を除く)の人数
        住民税の定額減税の算出に使用
        """
        total = 0
        if self.配偶者 is not None and not self.配偶者.is_一方の配偶者がこの控除を受けている:
            total += 1
        total += len(self.扶養親族一覧)
        return total
