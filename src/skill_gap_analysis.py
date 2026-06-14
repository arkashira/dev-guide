from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Skill:
    name: str
    level: int

@dataclass
class LearningPath:
    skills: List[Skill]
    duration: int

def identify_skill_gaps(user_skills: List[Skill], required_skills: List[Skill]) -> List[Skill]:
    skill_gaps = []
    for required_skill in required_skills:
        if not any(user_skill.name == required_skill.name and user_skill.level >= required_skill.level for user_skill in user_skills):
            skill_gaps.append(required_skill)
    return skill_gaps

def recommend_learning_path(skill_gaps: List[Skill], learning_paths: List[LearningPath]) -> Optional[LearningPath]:
    recommended_path = None
    for path in learning_paths:
        if all(any(skill.name == gap.name and skill.level >= gap.level for skill in path.skills) for gap in skill_gaps):
            if recommended_path is None or path.duration < recommended_path.duration:
                recommended_path = path
    return recommended_path

def generate_learning_plan(user_skills: List[Skill], required_skills: List[Skill], learning_paths: List[LearningPath]) -> Optional[LearningPath]:
    skill_gaps = identify_skill_gaps(user_skills, required_skills)
    if not skill_gaps:
        return None
    return recommend_learning_path(skill_gaps, learning_paths)
