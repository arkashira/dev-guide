// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CareerDevelopmentWidget() {
    const [recommendations, setRecommendations] = useState([]);
    const [mentors, setMentors] = useState([]);

    useEffect(() => {
        // Fetch personalized learning recommendations
        axios.get('/api/recommendations')
            .then(response => setRecommendations(response.data))
            .catch(error => console.error('Error fetching recommendations:', error));

        // Fetch mentorship matches
        axios.get('/api/mentors')
            .then(response => setMentors(response.data))
            .catch(error => console.error('Error fetching mentors:', error));
    }, []);

    return (
        <div>
            <h2>Personalized Learning Recommendations</h2>
            <ul>
                {recommendations.map((rec, index) => (
                    <li key={index}>{rec.title}</li>
                ))}
            </ul>

            <h2>Mentorship Matches</h2>
            <ul>
                {mentors.map((mentor, index) => (
                    <li key={index}>{mentor.name} - {mentor.specialty}</li>
                ))}
            </ul>
        </div>
    );
}

export default CareerDevelopmentWidget;