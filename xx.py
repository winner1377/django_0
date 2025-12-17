import matplotlib.pyplot as plt
import numpy as np

def generate_chaotic_heart(n_max):
    # Initialize arrays with 0. Size is n_max + 1 to use 1-based indexing easily.
    Q = np.zeros(n_max + 1, dtype=int)
    a = np.zeros(n_max + 1, dtype=int)

    # --- Initial Conditions ---
    # Q sequence: 2, 2, 1
    Q[1] = 2
    Q[2] = 2
    Q[3] = 1

    # a sequence: 1, 1, 2
    a[1] = 1
    a[2] = 1
    a[3] = 2

    # --- Generate Sequences ---
    for n in range(4, n_max + 1):
        # Q(n) = Q(n - Q(n-1)) + Q(n - Q(n-2))
        try:
            idx_q1 = n - Q[n-1]
            idx_q2 = n - Q[n-2]
            Q[n] = Q[idx_q1] + Q[idx_q2]
        except IndexError:
            Q[n] = 0 

        # a(n) = a(a(n-1)) + a(n - a(n-1))
        try:
            idx_a1 = a[n-1]
            idx_a2 = n - a[n-1]
            a[n] = a[idx_a1] + a[idx_a2]
        except IndexError:
            a[n] = 0

    return a[1:], Q[1:]

# Configuration
N = 2_800_000 
print(f"Generating sequences up to N={N}. This may take a few seconds...")

# Generate data
a_seq, q_seq = generate_chaotic_heart(N)
x = np.arange(1, N + 1)
y = a_seq - q_seq

# --- Plotting ---
fig, ax = plt.subplots(figsize=(12, 12), dpi=100)

# Colors
bg_color = '#F2EFE9' # Beige/Off-white
point_color = '#D1557D' # Raspberry pink

# Set background
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# Scatter plot
ax.scatter(x, y, s=0.05, c=point_color, alpha=0.6, marker='.')

# Labels and Title
ax.set_title(r"The Hofstadter Chaotic Heart Sequence $a(n) - Q(n)$", fontsize=22, fontfamily='serif', pad=20)
ax.set_xlabel(r"$n$", fontsize=18, fontfamily='serif')
ax.set_ylabel(r"$a(n) - Q(n)$", fontsize=18, fontfamily='serif')

# --- Simplified Text Definitions (Fixed for compatibility) ---
# We use standard strings instead of LaTeX environments to avoid parser errors.

q_text = (
    "Q(n) = {\n"
    "  2   if n = 1\n"
    "  2   if n = 2\n"
    "  1   if n = 3\n"
    "  Q(n - Q(n-1)) + Q(n - Q(n-2))   if n ≥ 4"
)

a_text = (
    "a(n) = {\n"
    "  1   if n = 1\n"
    "  1   if n = 2\n"
    "  2   if n = 3\n"
    "  a(a(n-1)) + a(n - a(n-1))   if n ≥ 4"
)

# Place text on plot using a monospace font to align the layout manually
ax.text(0.05, 0.88, q_text, transform=ax.transAxes, fontsize=11, 
        verticalalignment='top', fontfamily='monospace', alpha=0.8, linespacing=1.6)

ax.text(0.05, 0.72, a_text, transform=ax.transAxes, fontsize=11, 
        verticalalignment='top', fontfamily='monospace', alpha=0.8, linespacing=1.6)

# Add credit
ax.text(0.98, 0.02, "Simone Conradi, 2025 (Reproduction)", transform=ax.transAxes, 
        fontsize=10, horizontalalignment='right', fontfamily='serif', alpha=0.7)

# Adjust axes limits
ax.set_xlim(0, N)
ax.set_ylim(-100000, 180000)

plt.tight_layout()
plt.show()