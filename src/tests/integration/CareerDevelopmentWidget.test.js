import React from 'react';
import { render, screen } from '@testing-library/react';
import axios from 'axios';
import CareerDevelopmentWidget from '../components/CareerDevelopmentWidget';

jest.mock('axios');

describe('CareerDevelopmentWidget', () => {
    beforeEach(() => {
        axios.get.mockResolvedValue({ data: [] });
    });

    test('renders personalized learning recommendations', async () => {
        axios.get.mockResolvedValueOnce({ data: [{ title: 'Learn React' }] });
        render(<CareerDevelopmentWidget />);
        expect(await screen.findByText('Learn React')).toBeInTheDocument();
    });

    test('renders mentorship matches', async () => {
        axios.get.mockResolvedValueOnce({ data: [{ name: 'John Doe', specialty: 'Frontend Development' }] });
        render(<CareerDevelopmentWidget />);
        expect(await screen.findByText('John Doe - Frontend Development')).toBeInTheDocument();
    });
});