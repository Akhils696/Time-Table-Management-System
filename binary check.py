import pickle

# Define the credentials dictionary
credentials = {
    "admin": "admin123",
    "student1": "studpass1",
    "student2": "studpass2",
    "teacher1": "teachpass1",
    "teacher2": "teachpass2"
}

# Save the credentials to a binary file
with open("credentials.bin", "wb") as file:
    pickle.dump(credentials, file) #pickle.dump

print("Credentials saved successfully to credentials.bin")
