class 税額控除の算出に用いるデータ:
    """
    所得税や住民税の税額控除額を算出する際に用いる情報
    """
    # TODO
    def __init__(self):
        # 支払済の予定納税額
        self.予定納税額_第1期分: int = 0
        self.予定納税額_第2期分: int = 0

        # ふるさと納税額(実質負担額2,000円を含む額)
        self.ふるさと納税額: int = 0
        self.is_ワンストップ特例制度: bool = False
