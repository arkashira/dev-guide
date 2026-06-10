# Add the following imports at the top of the file
import os
from flask import Flask, render_template
from recommendation_engine import RecommendationEngine
from mentorship_matching import MentorshipMatching
from skill_assessment import SkillAssessment

# Initialize the Flask app
app = Flask(__name__)

# Initialize the recommendation engine
recommendation_engine = RecommendationEngine()

# Initialize the mentorship matching module
mentorship_matching = MentorshipMatching()

# Initialize the skill assessment module
skill_assessment = SkillAssessment()

# Define the routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learning-paths')
def learning_paths():
    recommendations = recommendation_engine.get_recommendations()
    return render_template('learning_paths.html', recommendations=recommendations)

@app.route('/mentorship')
def mentorship():
    ment
