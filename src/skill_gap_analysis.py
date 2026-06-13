import json
from dataclasses import dataclass
from typing import List

@dataclass
class Skill:
    name: str
    level: int

    def __eq__(self, other):
        return self.name == other.name and self.level == other.level

@dataclass
class LearningPath:
    skills: List[Skill]
    recommended_resources: List[str]

class SkillGapAnalysis:
    def __init__(self, skills: List[Skill], learning_paths: List[LearningPath]):
        self.skills = skills
        self.learning_paths = learning_paths

    def generate_personalized_learning_path(self, user_skills: List[Skill]) -> LearningPath:
        recommended_skills = []
        for skill in self.skills:
            if skill not in user_skills:
                recommended_skills.append(skill)
        recommended_resources = []
        for learning_path in self.learning_paths:
            for skill in recommended_skills:
                if skill in learning_path.skills:
                    for resource in learning_path.recommended_resources:
                        if skill.name.lower() in resource.lower():
                            recommended_resources.append(resource)
        return LearningPath(recommended_skills, recommended_resources)

    def save_to_json(self, filename: str):
        data = {
            "skills": [{"name": skill.name, "level": skill.level} for skill in self.skills],
            "learning_paths": [
                {
                    "skills": [{"name": skill.name, "level": skill.level} for skill in learning_path.skills],
                    "recommended_resources": learning_path.recommended_resources
                }
                for learning_path in self.learning_paths
            ]
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    @classmethod
    def load_from_json(cls, filename: str):
        with open(filename, "r") as f:
            data = json.load(f)
        skills = [Skill(skill["name"], skill["level"]) for skill in data["skills"]]
        learning_paths = [
            LearningPath(
                [Skill(skill["name"], skill["level"]) for skill in learning_path["skills"]],
                learning_path["recommended_resources"]
            )
            for learning_path in data["learning_paths"]
        ]
        return cls(skills, learning_paths)
