import pandas as pd


def load_students():
    students = [
        {
            "student_id": "S001",
            "name": "Aarav",
            "interests": "artificial intelligence machine learning data science",
            "skills": "python pandas scikit-learn",
            "career_goal": "AI Engineer"
        },
        {
            "student_id": "S002",
            "name": "Priya",
            "interests": "web development software development",
            "skills": "java sql spring boot",
            "career_goal": "Software Developer"
        },
        {
            "student_id": "S003",
            "name": "Rahul",
            "interests": "data analysis machine learning",
            "skills": "python pandas power bi sql",
            "career_goal": "Data Analyst"
        },
        {
            "student_id": "S004",
            "name": "Neha",
            "interests": "computer vision deep learning artificial intelligence",
            "skills": "python tensorflow opencv",
            "career_goal": "Computer Vision Engineer"
        },
        {
            "student_id": "S005",
            "name": "Karan",
            "interests": "mobile application development android",
            "skills": "java android kotlin",
            "career_goal": "Android Developer"
        }
    ]

    return pd.DataFrame(students)


def load_project_topics():
    projects = [
        {
            "project_id": "P001",
            "title": "Student Performance Prediction",
            "description": "Build a machine learning system to predict student academic performance using student data.",
            "domain": "Machine Learning",
            "difficulty": "Intermediate",
            "skills": "python pandas scikit-learn"
        },
        {
            "project_id": "P002",
            "title": "Customer Churn Prediction",
            "description": "Develop a machine learning model to predict whether customers will leave a service.",
            "domain": "Machine Learning",
            "difficulty": "Intermediate",
            "skills": "python pandas machine learning"
        },
        {
            "project_id": "P003",
            "title": "Sales Data Analytics Dashboard",
            "description": "Create a data analytics project to analyze sales trends and generate business insights.",
            "domain": "Data Analytics",
            "difficulty": "Beginner",
            "skills": "python pandas sql power bi"
        },
        {
            "project_id": "P004",
            "title": "Movie Recommendation System",
            "description": "Create a recommendation system that suggests movies based on user preferences and ratings.",
            "domain": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "skills": "python pandas machine learning"
        },
        {
            "project_id": "P005",
            "title": "Face Recognition System",
            "description": "Develop a computer vision system that detects and recognizes faces from images or video.",
            "domain": "Computer Vision",
            "difficulty": "Advanced",
            "skills": "python opencv machine learning"
        },
        {
            "project_id": "P006",
            "title": "AI Chatbot",
            "description": "Build an intelligent chatbot using natural language processing and machine learning.",
            "domain": "NLP",
            "difficulty": "Intermediate",
            "skills": "python nltk machine learning"
        },
        {
            "project_id": "P007",
            "title": "Disease Prediction System",
            "description": "Develop a machine learning model that predicts possible diseases from medical symptoms.",
            "domain": "Machine Learning",
            "difficulty": "Advanced",
            "skills": "python pandas scikit-learn"
        },
        {
            "project_id": "P008",
            "title": "Fake News Detection",
            "description": "Build an NLP-based system to classify news articles as real or potentially fake.",
            "domain": "NLP",
            "difficulty": "Intermediate",
            "skills": "python nltk scikit-learn"
        },
        {
            "project_id": "P009",
            "title": "Android Expense Tracker",
            "description": "Develop an Android application for recording and analyzing personal expenses.",
            "domain": "Mobile Development",
            "difficulty": "Beginner",
            "skills": "java android kotlin"
        },
        {
            "project_id": "P010",
            "title": "E-Commerce Website",
            "description": "Create a web application with product listing, shopping cart and user management features.",
            "domain": "Web Development",
            "difficulty": "Intermediate",
            "skills": "java sql spring boot"
        },
        {
            "project_id": "P011",
            "title": "Object Detection System",
            "description": "Develop a computer vision application that detects objects in images and videos.",
            "domain": "Computer Vision",
            "difficulty": "Advanced",
            "skills": "python opencv machine learning"
        },
        {
            "project_id": "P012",
            "title": "Personalized Learning Recommendation",
            "description": "Build an AI system that recommends learning resources according to student interests and skills.",
            "domain": "Artificial Intelligence",
            "difficulty": "Advanced",
            "skills": "python pandas machine learning"
        }
    ]

    return pd.DataFrame(projects)


if __name__ == "__main__":
    students = load_students()
    projects = load_project_topics()

    print("\n========== STUDENT PROFILES ==========\n")
    print(students.to_string(index=False))
    print("*" * 150)

    print("\n========== PROJECT TOPICS ==========\n")
    print(projects.to_string(index=False))
    print("*" * 150)