from skill_gap_analysis import Skill, LearningPath, SkillGapAnalysis

def test_generate_personalized_learning_path():
    skills = [Skill("Python", 1), Skill("Java", 2)]
    learning_paths = [
        LearningPath([Skill("Python", 1), Skill("Java", 2)], ["Python tutorial", "Java tutorial"]),
        LearningPath([Skill("C++", 3), Skill("JavaScript", 4)], ["C++ tutorial", "JavaScript tutorial"])
    ]
    analysis = SkillGapAnalysis(skills, learning_paths)
    user_skills = [Skill("Python", 1)]
    result = analysis.generate_personalized_learning_path(user_skills)
    assert result.skills == [Skill("Java", 2)]
    assert result.recommended_resources == ["Java tutorial"]

def test_save_to_json():
    skills = [Skill("Python", 1), Skill("Java", 2)]
    learning_paths = [
        LearningPath([Skill("Python", 1), Skill("Java", 2)], ["Python tutorial", "Java tutorial"]),
        LearningPath([Skill("C++", 3), Skill("JavaScript", 4)], ["C++ tutorial", "JavaScript tutorial"])
    ]
    analysis = SkillGapAnalysis(skills, learning_paths)
    analysis.save_to_json("test.json")
    loaded_analysis = SkillGapAnalysis.load_from_json("test.json")
    assert loaded_analysis.skills == skills
    assert loaded_analysis.learning_paths == learning_paths
