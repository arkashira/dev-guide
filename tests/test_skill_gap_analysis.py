from src.skill_gap_analysis import Skill, LearningPath, identify_skill_gaps, recommend_learning_path, generate_learning_plan
import pytest

def test_identify_skill_gaps():
    user_skills = [Skill("Python", 3), Skill("Java", 2)]
    required_skills = [Skill("Python", 3), Skill("Java", 3), Skill("C++", 2)]
    expected_gaps = [Skill("Java", 3), Skill("C++", 2)]
    assert identify_skill_gaps(user_skills, required_skills) == expected_gaps

def test_recommend_learning_path():
    skill_gaps = [Skill("Java", 3), Skill("C++", 2)]
    learning_paths = [
        LearningPath([Skill("Java", 3), Skill("C++", 2)], 6),
        LearningPath([Skill("Java", 3), Skill("C++", 3)], 9),
        LearningPath([Skill("Python", 3), Skill("C++", 2)], 6)
    ]
    expected_path = learning_paths[0]
    assert recommend_learning_path(skill_gaps, learning_paths) == expected_path

def test_generate_learning_plan():
    user_skills = [Skill("Python", 3), Skill("Java", 2)]
    required_skills = [Skill("Python", 3), Skill("Java", 3), Skill("C++", 2)]
    learning_paths = [
        LearningPath([Skill("Java", 3), Skill("C++", 2)], 6),
        LearningPath([Skill("Java", 3), Skill("C++", 3)], 9),
        LearningPath([Skill("Python", 3), Skill("C++", 2)], 6)
    ]
    expected_path = learning_paths[0]
    assert generate_learning_plan(user_skills, required_skills, learning_paths) == expected_path

def test_edge_case_no_gaps():
    user_skills = [Skill("Python", 3), Skill("Java", 3), Skill("C++", 2)]
    required_skills = [Skill("Python", 3), Skill("Java", 3), Skill("C++", 2)]
    learning_paths = [
        LearningPath([Skill("Java", 3), Skill("C++", 2)], 6),
        LearningPath([Skill("Java", 3), Skill("C++", 3)], 9),
        LearningPath([Skill("Python", 3), Skill("C++", 2)], 6)
    ]
    assert generate_learning_plan(user_skills, required_skills, learning_paths) is None
