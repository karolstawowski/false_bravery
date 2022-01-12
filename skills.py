import random


def randomizeSkillOrder():
    skills = ['Q', 'W', 'E']
    random.shuffle(skills)
    random.shuffle(skills)
    random.shuffle(skills)
    return skills
