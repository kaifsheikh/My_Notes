import matplotlib.pyplot as plt

# Data
students = ["Ali", "Ahmed", "Kaif", "Bilal"]
marks = [70, 85, 90, 95]

# Figure size (professional look)
plt.figure(figsize=(8,5))

# Bar chart
bars = plt.bar(
    students,
    marks,
    color="skyblue",
    edgecolor="black"
)

# Title + labels
plt.title("Students Marks Report")
plt.xlabel("Students")
plt.ylabel("Marks")

# Grid (sirf Y-axis)
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Values on bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        str(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.show()