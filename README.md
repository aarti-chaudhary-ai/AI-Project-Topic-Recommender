# AI Project Topic Recommender

## Project Overview
The AI Project Topic Recommender is a Python-based recommendation system that suggests suitable project topics for students based on their interests, skills, and career goals.
The system uses Natural Language Processing (NLP), TF-IDF vectorization, and Cosine Similarity to calculate the relevance between a student's profile and available project topics.

## Features
- Student profile-based project recommendations
- NLP text preprocessing
- TF-IDF vectorization
- Cosine Similarity-based matching
- Top-N project recommendations
- Domain filtering
- Difficulty filtering
- Input validation
- Handles cases where no relevant project is found
- 12 sample project topics

## Technologies Used
- Python
- Pandas
- NLTK
- Scikit-learn
- TF-IDF
- Cosine Similarity

## How It Works

The recommendation system follows these steps:
1. Load student profiles and project topics.
2. Combine student interests, skills, and career goals.
3. Combine project title, description, domain, and skills.
4. Apply NLP preprocessing to the text.
5. Convert the processed text into TF-IDF vectors.
6. Calculate Cosine Similarity between the student profile and project topics.
7. Apply optional domain and difficulty filters.
8. Sort projects according to similarity score.
9. Display the Top-N recommended projects.

## NLP Preprocessing

The system performs the following preprocessing steps:
- Converts text to lowercase
- Removes special characters and numbers
- Removes English stopwords
- Applies lemmatization

NLTK is used for text preprocessing.

## Recommendation Method

### TF-IDF
TF-IDF (Term Frequency-Inverse Document Frequency) converts the processed text into numerical vectors based on the importance of words.

### Cosine Similarity
Cosine Similarity measures how similar the student's profile is to each project topic.
A higher similarity score indicates a more relevant project recommendation.

## Filtering

Users can filter recommendations by domain and difficulty.

### Available Domains
- Machine Learning
- Data Analytics
- Artificial Intelligence
- Computer Vision
- NLP
- Mobile Development
- Web Development

Users can select **All** to disable domain filtering.

### Available Difficulties
- Beginner
- Intermediate
- Advanced

Users can select **All** to disable difficulty filtering.

## Project Topics

The system contains 12 sample project topics:
1. Student Performance Prediction
2. Customer Churn Prediction
3. Sales Data Analytics Dashboard
4. Movie Recommendation System
5. Face Recognition System
6. AI Chatbot
7. Disease Prediction System
8. Fake News Detection
9. Android Expense Tracker
10. E-Commerce Website
11. Object Detection System
12. Personalized Learning Recommendation

## Project Structure

```text
AI Project Topic Recommender/
│
├── data.py
├── preprocessing.py
├── recommender.py
├── requirements.txt
└── README.md
```

## Installation

Make sure Python is installed on your system.
Install the required libraries using:
```bash
pip install -r requirements.txt
```

## How to Run
Run the recommendation system using:
```bash
python recommender.py
```

The program will ask the user to enter:
1. Student ID
2. Domain preference
3. Difficulty preference
4. Number of recommendations

The system will then display the recommended project topics along with their similarity scores.

## Sample Recommendation

For student `S005 - Karan` with:
- Career Goal: Android Developer
- Interests: Mobile application development and Android
- Skills: Java, Android, Kotlin
- Domain: Mobile Development
- Difficulty: All

The system recommends:
```text
Project ID   : P009
Title        : Android Expense Tracker
Domain       : Mobile Development
Difficulty   : Beginner
Similarity   : 62.14%
Description  : Develop an Android application for recording and analyzing personal expenses.
```

## Error Handling

The system validates user input and handles:
- Invalid Student IDs
- Invalid domain choices
- Invalid difficulty choices
- Invalid Top-N values
- No projects available for selected filters
- No relevant project recommendations

For example, if no relevant projects are found, the system displays:

```text
No relevant project recommendations found.
Please try another domain or review your profile.
```

## Sample Student Profiles

The project contains five sample student profiles:

| Student ID | Name | Career Goal |
|------------|------|-------------|
| S001 | Aarav | AI Engineer |
| S002 | Priya | Software Developer |
| S003 | Rahul | Data Analyst |
| S004 | Neha | Computer Vision Engineer |
| S005 | Karan | Android Developer |

## Testing

The recommendation system was tested with different:
- Student IDs
- Domains
- Difficulty levels
- Top-N values
- Invalid inputs
- No-result filter combinations

The system successfully provides relevant recommendations and handles invalid or unavailable selections without crashing.

## Project Objective
The objective of this project is to develop a project topic recommendation system that helps students discover suitable project ideas based on their interests, existing skills, and career goals.

## Conclusion

The AI Project Topic Recommender provides personalized project suggestions using Natural Language Processing and machine learning techniques.
By combining NLP preprocessing, TF-IDF vectorization, and Cosine Similarity, the system matches student profiles with relevant project topics. Domain and difficulty filters provide additional control over the recommendations.
This project demonstrates the practical use of NLP and machine learning concepts in a student-focused recommendation system.

### Demo Video


## 👩‍💻 Author

**Aarti**
B.Tech – Computer Science & Engineering (Artificial Intelligence)
