from recommendation_engine import RecommendationEngine, SkillGap, LearningPath

def test_generate_recommendations():
    skill_gaps = [SkillGap("Python", 5), SkillGap("Java", 3)]
    learning_paths = [LearningPath(["Python", "JavaScript"], ["Python Tutorial", "JavaScript Tutorial"]), 
                      LearningPath(["Java", "C++"], ["Java Tutorial", "C++ Tutorial"])]
    engine = RecommendationEngine(skill_gaps, learning_paths)
    recommendations = engine.generate_recommendations()
    assert len(recommendations) == 2
    assert recommendations[0].skills == ["Python", "JavaScript"]
    assert recommendations[1].skills == ["Java", "C++"]

def test_get_skill_gaps():
    skill_gaps = [SkillGap("Python", 5), SkillGap("Java", 3)]
    learning_paths = [LearningPath(["Python", "JavaScript"], ["Python Tutorial", "JavaScript Tutorial"]), 
                      LearningPath(["Java", "C++"], ["Java Tutorial", "C++ Tutorial"])]
    engine = RecommendationEngine(skill_gaps, learning_paths)
    assert engine.get_skill_gaps() == skill_gaps

def test_get_learning_paths():
    skill_gaps = [SkillGap("Python", 5), SkillGap("Java", 3)]
    learning_paths = [LearningPath(["Python", "JavaScript"], ["Python Tutorial", "JavaScript Tutorial"]), 
                      LearningPath(["Java", "C++"], ["Java Tutorial", "C++ Tutorial"])]
    engine = RecommendationEngine(skill_gaps, learning_paths)
    assert engine.get_learning_paths() == learning_paths

def test_empty_skill_gaps():
    skill_gaps = []
    learning_paths = [LearningPath(["Python", "JavaScript"], ["Python Tutorial", "JavaScript Tutorial"]), 
                      LearningPath(["Java", "C++"], ["Java Tutorial", "C++ Tutorial"])]
    engine = RecommendationEngine(skill_gaps, learning_paths)
    assert engine.generate_recommendations() == []

def test_empty_learning_paths():
    skill_gaps = [SkillGap("Python", 5), SkillGap("Java", 3)]
    learning_paths = []
    engine = RecommendationEngine(skill_gaps, learning_paths)
    assert engine.generate_recommendations() == []
