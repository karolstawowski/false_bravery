class SummonerSpell:
    def __init__(
        self,
        id: str,
        en_name: str,
        pl_name: str,
        image_x_axis: int,
        image_y_axis: int,
        image_width: int,
        image_height: int,
    ):
        self.image_height = image_height
        self.image_width = image_width
        self.image_y_axis = image_y_axis
        self.image_x_axis = image_x_axis
        self.pl_name = pl_name
        self.en_name = en_name
        self.id = id
