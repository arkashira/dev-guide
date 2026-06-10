# test_user_profile.py

def test_onboarding_wizard_collects_skills():
    user_input = {
        "current_skills": ["Python", "JavaScript"],
        "desired_roles": ["Backend Developer", "Frontend Developer"],
        "learning_preferences": ["Online Courses", "Books"]
    }
    result = onboarding_wizard.collect_user_input(user_input)
    assert result["current_skills"] == user_input["current_skills"]
    assert result["desired_roles"] == user_input["desired_roles"]
    assert result["learning_preferences"] == user_input["learning_preferences"]

def test_profile_data_storage():
    user_profile = UserProfile()
    user_profile.save({
        "current_skills": ["Python", "JavaScript"],
        "desired_roles": ["Backend Developer"],
        "learning_preferences": ["Online Courses"]
    })
    stored_data = user_profile.get_data()
    assert stored_data["current_skills"] == ["Python", "JavaScript"]
    assert stored_data["desired_roles"] == ["Backend Developer"]
    assert stored_data["learning_preferences"] == ["Online Courses"]

def test_edit_profile():
    user_profile = UserProfile()
    user_profile.save({
        "current_skills": ["Python"],
        "desired_roles": ["Backend Developer"],
        "learning_preferences": ["Books"]
    })
    user_profile.edit({
        "current_skills": ["Python", "Django"],
        "desired_roles": ["Full Stack Developer"]
    })
    updated_data = user_profile.get_data()
    assert updated_data["current_skills"] == ["Python", "Django"]
    assert updated_data["desired_roles"] == ["Full Stack Developer"]

def test_invalid_data_handling():
    user_profile = UserProfile()
    invalid_input = {
        "current_skills": "",
        "desired_roles": None,
        "learning_preferences": ["Online Courses"]
    }
    with pytest.raises(ValidationError):
        user_profile.save(invalid_input)

def test_security_measures():
    user_profile = UserProfile()
    user_profile.save({
        "current_skills": ["Python"],
        "desired_roles": ["Backend Developer"],
        "learning_preferences": ["Books"]
    })
    assert user_profile.is_data_encrypted() == True