import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data import load_students, load_project_topics
from preprocessing import preprocess_text


def create_profile_text(student):
    """
    Combine student interests, skills and career goal
    into one text profile.
    """

    return (
        student["interests"] + " "
        + student["skills"] + " "
        + student["career_goal"]
    )


def create_project_text(project):
    """
    Combine project description, domain and required skills
    into one project profile.
    """

    return (
        project["title"] + " "
        + project["description"] + " "
        + project["domain"] + " "
        + project["skills"]
    )


def calculate_similarity(student, projects):
    """
    Calculate TF-IDF cosine similarity between
    one student profile and all project topics.
    """

    student_text = create_profile_text(student)

    project_texts = [
        create_project_text(project)
        for _, project in projects.iterrows()
    ]

    # Preprocess student profile
    student_text = preprocess_text(student_text)

    # Preprocess project topics
    project_texts = [
        preprocess_text(text)
        for text in project_texts
    ]

    # Combine student and project text
    all_texts = [student_text] + project_texts

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Student vector
    student_vector = tfidf_matrix[0]

    # Project vectors
    project_vectors = tfidf_matrix[1:]

    # Cosine similarity
    similarity_scores = cosine_similarity(
        student_vector,
        project_vectors
    ).flatten()

    return similarity_scores


def recommend_projects(student_id, top_n=5,domain=None, difficulty=None):

    students = load_students()
    projects = load_project_topics()

    # Find student
    student_data = students[
        students["student_id"] == student_id
    ]

    if student_data.empty:
        print("\nStudent ID not found!")
        return

    student = student_data.iloc[0]
    
    # Apply domain filter
    if domain:
        projects = projects[
            projects["domain"].str.lower() == domain.lower()
        ]

    # Apply difficulty filter
    if difficulty:
        projects = projects[
            projects["difficulty"].str.lower() == difficulty.lower()
        ]

    if projects.empty:
        print("\nNo projects found for the selected filters.")
        print("Please try another domain or difficulty combination.")
        return

    # Calculate similarity
    similarity_scores = calculate_similarity(
        student,
        projects
    )

    # Add scores to project dataframe
    recommendations = projects.copy()

    recommendations["similarity_score"] = similarity_scores

    # Sort by highest similarity
    recommendations = recommendations.sort_values(
        by="similarity_score",
        ascending=False
    )
    if recommendations["similarity_score"].max() == 0:
        print("\nNo relevant project recommendations found.")
        print("Please try another domain or review your profile.")
        return

    # Select Top-N
    recommendations = recommendations.head(top_n)

    print("\n==============================================")
    print("        PROJECT TOPIC RECOMMENDATIONS")
    print("==============================================")

    print(f"\nStudent: {student['name']}")
    print(f"Career Goal: {student['career_goal']}")

    print("\nInterests:")
    print(student["interests"])

    print("\nSkills:")
    print(student["skills"])

    print("\n----------------------------------------------")
    print(f"Top {top_n} Recommended Projects")
    print("----------------------------------------------")

    for index, project in recommendations.iterrows():

        score = project["similarity_score"] * 100

        print(f"\nProject ID   : {project['project_id']}")
        print(f"Title        : {project['title']}")
        print(f"Domain       : {project['domain']}")
        print(f"Difficulty   : {project['difficulty']}")
        print(f"Similarity   : {score:.2f}%")
        print(f"Description  : {project['description']}")


if __name__ == "__main__":

    print("\n==============================================")
    print("      AI PROJECT TOPIC RECOMMENDER")
    print("==============================================")

    print("\nAvailable Student IDs:")
    print("S001 - Aarav")
    print("S002 - Priya")
    print("S003 - Rahul")
    print("S004 - Neha")
    print("S005 - Karan")

    student_id = input("\nEnter Student ID: ").strip().upper()
    valid_student_ids = ["S001", "S002", "S003", "S004", "S005"]
    
    if student_id not in valid_student_ids:
        print("\nInvalid Student ID!")
        print("Please enter a valid Student ID.")
        exit()
        
    print("\nAvailable Domains:")
    print("1. All")
    print("2. Machine Learning")
    print("3. Data Analytics")
    print("4. Artificial Intelligence")
    print("5. Computer Vision")
    print("6. NLP")
    print("7. Mobile Development")
    print("8. Web Development")

    domain_choice = input("\nEnter domain choice (1-8): ").strip()

    domains = {
        "1": None,
        "2": "Machine Learning",
        "3": "Data Analytics",
        "4": "Artificial Intelligence",
        "5": "Computer Vision",
        "6": "NLP",
        "7": "Mobile Development",
        "8": "Web Development"
    }

    domain = domains.get(domain_choice)
    if domain_choice not in domains:
        print("\nInvalid domain choice!")
        print("Please select a number from 1 to 8.")
        exit()
        
    domain = domains[domain_choice]

    print("\nAvailable Difficulties:")
    print("1. All")
    print("2. Beginner")
    print("3. Intermediate")
    print("4. Advanced")

    difficulty_choice = input("\nEnter difficulty choice (1-4): ").strip()

    difficulties = {
        "1": None,
        "2": "Beginner",
        "3": "Intermediate",
        "4": "Advanced"
    }

    difficulty = difficulties.get(difficulty_choice)
    if difficulty_choice not in difficulties:
        print("\nInvalid difficulty choice!")
        print("Please select a number from 1 to 4.")
        exit()

    difficulty = difficulties[difficulty_choice]

    top_n = input("\nHow many recommendations do you want? [Default: 5]: ").strip()

    if top_n == "":
        top_n = 5
    elif not top_n.isdigit() or int(top_n) <= 0:
        print("\nInvalid number!")
        print("Please enter a positive number.")
        exit()
    else:
        top_n = int(top_n)

    recommend_projects(
        student_id,
        top_n=top_n,
        domain=domain,
        difficulty=difficulty
    )