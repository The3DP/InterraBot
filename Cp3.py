# Get user input with basic validation
while True:
    age = input("What is your age? ")
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    else:
        print("Please enter a valid positive number for age.")

job_category = input("What category of job are you interested in? (e.g., Healthcare, Technology, Education, Finance, Arts, etc.) ")

expected_income = input("What is your expected income? ")
# You can expand this later to validate currency format or numeric ranges

while True:
    years_ = input("How many years of experience do you have? ")
    if years_.isdigit() and int(years_) >= 0:
        years_ = int(years_)
        break
    else:
        print("Please enter a valid non-negative number for years of experience.")

# Define job categories with specific jobs
job_categories = {
    "healthcare": ["Doctor", "Nurse", "Pharmacist", "Physical Therapist", "Surgeon"],
    "technology": ["Software Engineer", "Data Scientist", "Web Developer", "Network Administrator", "IT Support Specialist"],
    "education": ["Teacher", "Professor", "School Counselor", "Librarian", "Special Education Teacher"],
    "finance": ["Accountant", "Financial Analyst", "Investment Banker", "Financial Planner", "Auditor"],
    "arts": ["Graphic Designer", "Musician", "Painter", "Photographer", "Actor"]
}

job_category_lower = job_category.lower()
jobs = job_categories.get(job_category_lower)

# Output results
print("\n--- Career Overview ---")
print(f"You are {age} years old.")
print(f"Your desired job category is: {job_category.capitalize()}")

if jobs:
    print(f"Some jobs in the {job_category.capitalize()} category are: {', '.join(jobs)}")
else:
    print("Invalid job category. Please choose from: Healthcare, Technology, Education, Finance, Arts.")
    jobs = []  # to avoid further logic errors if needed

print(f"Your expected income is: {expected_income}")
print(f"You have {years_} years of experience.")

# Provide additional suggestions based on experience
if jobs:
    if years_ < 2:
        advice = "You're likely suited for entry-level roles or internships."
    elif years_ < 5:
        advice = "You may qualify for mid-level positions or junior specialist roles."
    else:
        advice = "You could be a candidate for senior positions or management roles."

    print("\n--- Career Advice ---")
    print(advice)

# Optionally, you could suggest top 3 roles
    print("You might explore roles such as:")
    for job in jobs[:3]:
        print(f"- {job}")

