import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Eve"],
    "Age": [23, 25, 22, 24]
}

temp = pd.DataFrame(data)
print(temp)

temp.to_csv("stud.csv", index=False)


class student:
    def __init__(self, name):
        self.name = name

    def hi(self):
        print(self.name)



s1 = student("Wangchuk")
s1.hi()
print(s1.name)



import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Eve"],
    "Age": [23, 25, 22, 24]
}

temp = pd.DataFrame(data)

print(temp)

# Save as CSV
temp.to_csv("stud.csv", index=False)

# Save as JSON
temp.to_json("stud.json", orient="records", indent=4)

# Save as Excel
temp.to_excel("stud.xlsx", index=False)

print("All files created successfully!")

