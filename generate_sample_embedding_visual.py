"""
The below code has been generated entirely by an LLM.
"""

import matplotlib.pyplot as plt

# Original embeddings (0 to 1 scale)
embeddings = {
    'Mouse': (0.1, 0.2),   # Mostly terrestrial and small
    'Lion': (0.2, 0.7),    # Terrestrial and big
    'Whale': (0.9, 0.9),   # Aquatic and big
    'Fish': (0.9, 0.2),    # Aquatic and small
    'Shark': (0.7, 0.6)    # Aquatic with a size leaning big
}

# Flip the x-axis so that positive x (Terrestrial) and negative x (Aquatic)
# For x: use 1 - (coords[0]*2) and for y: use coords[1]*2 - 1 (so positive y remains Big)
transformed_embeddings = {
    word: (1 - (coords[0] * 2), coords[1] * 2 - 1)
    for word, coords in embeddings.items()
}

# Extract transformed coordinates
words = list(transformed_embeddings.keys())
x_vals = [transformed_embeddings[word][0] for word in words]
y_vals = [transformed_embeddings[word][1] for word in words]

plt.figure(figsize=(8,8))

# Define a list of colors for the vectors (and points)
colors = ['red', 'green', 'blue', 'orange', 'purple']

# Plot individual scatter points with matching vector colors
for i, word in enumerate(words):
    plt.scatter(x_vals[i], y_vals[i], color=colors[i])

# Draw arrows (vectors) from origin (0,0) to each point, with arrow heads that finish at the point
for i, word in enumerate(words):
    plt.arrow(0, 0, x_vals[i]*0.98, y_vals[i]*0.98,
              head_width=0.03, head_length=0.03, fc=colors[i], ec=colors[i], length_includes_head=True)

# Annotate the points, using a computed offset so that labels do not overlap the arrow head
for i, word in enumerate(words):
    # Compute an offset based on the sign of x and y values
    offset_x = 0.07 if x_vals[i] >= 0 else -0.07
    offset_y = 0.07 if y_vals[i] >= 0 else -0.07
    plt.annotate(word, (x_vals[i] + offset_x, y_vals[i] + offset_y), fontsize=12, color=colors[i])

# Draw x and y axis lines (center axes)
plt.axhline(0, color='black', linewidth=1.2)
plt.axvline(0, color='black', linewidth=1.2)

# Remove the surrounding box/spines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Set axis limits and customized ticks for a clear Cartesian plane
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.xticks([-1, -0.5, 0, 0.5, 1], ["Aquatic", "", "0", "", "Terrestrial"])
plt.yticks([-1, -0.5, 0, 0.5, 1], ["Small", "", "0", "", "Big"])

plt.xlabel("Terrestrial", fontsize=14)
plt.ylabel("Big", fontsize=14)
plt.title("Word Embeddings", fontsize=16)
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig("embedding_example.png", dpi=300, bbox_inches='tight')
plt.show()
