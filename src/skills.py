import random


def randomize_skill_order() -> list:
    skills = ["Q", "W", "E"]
    random.shuffle(skills)
    random.shuffle(skills)
    random.shuffle(skills)
    return skills
