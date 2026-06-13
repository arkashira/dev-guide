import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class SkillGap:
    skill: str
    gap: int

@dataclass
class LearningPath:
    skills: List[str]
    resources: List[str]

class RecommendationEngine:
    def __init__(self, skill_gaps: List[SkillGap], learning_paths: List[LearningPath]):
        self.skill_gaps = skill_gaps
        self.learning_paths = learning_paths

    def generate_recommendations(self) -> List[LearningPath]:
        recommendations = []
        for skill_gap in self.skill_gaps:
            for learning_path in self.learning_paths:
                if skill_gap.skill in learning_path.skills:
                    recommendations.append(learning_path)
        return recommendations

    def get_skill_gaps(self) -> List[SkillGap]:
        return self.skill_gaps

    def get_learning_paths(self) -> List[LearningPath]:
        return self.learning_paths
