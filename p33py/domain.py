from typing import Literal

LifestageName = Literal["k8", "hs", "college", "career"]


class Lifestage:
    name: LifestageName

    def __init__(self, name: LifestageName):
        self.name = name


k8 = Lifestage("k8")
hs = Lifestage("hs")
college = Lifestage("college")
career = Lifestage("career")

lifestages = [k8, hs, college, career]
