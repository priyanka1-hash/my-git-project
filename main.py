# main.py

skills = ["python", "sql", "excel", "machine learning"]

resume = input("Enter your skills: ").lower()

found = [s for s in skills if s in resume]

score = len(found) / len(skills) * 100

print("Skills Found:", found)
print("Match Score:", score, "%")
print("Excellent")