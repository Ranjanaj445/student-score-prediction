import pandas as pd
import matplotlib.pyplot as plt

print("Program Started")


data = {
    "Name": ["Arun", "Priya", "Rahul", "Ranjana", "Divya"],
    "Maths": [85, 92, 76, 88, 95],
    "Science": [78, 89, 82, 91, 94],
    "English": [90, 95, 75, 86, 92]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)


# ==============================
# 1. SCATTER PLOT
# ==============================

print("\nShowing Scatter Plot...")

plt.figure()
plt.scatter(df["Maths"], df["Science"])
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")
plt.title("Maths vs Science")
plt.grid()
plt.show()


# ==============================
# 2. BAR CHART
# ==============================

print("Showing Bar Chart...")

plt.figure()
plt.bar(df["Name"], df["Maths"])
plt.xlabel("Student Name")
plt.ylabel("Maths Marks")
plt.title("Student Maths Marks")
plt.show()


# ==============================
# 3. LINE CHART
# ==============================

print("Showing Line Chart...")

plt.figure()
plt.plot(df["Name"], df["English"], marker="o")
plt.xlabel("Student Name")
plt.ylabel("English Marks")
plt.title("Student English Marks")
plt.grid()
plt.show()


print("\nData Visualization Completed Successfully!")