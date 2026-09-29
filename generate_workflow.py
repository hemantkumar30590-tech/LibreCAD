# generate_workflow.py - Generation to Home SLD
import matplotlib.pyplot as plt

stages = [
    "1. GENERATION\n11kV\nPower Plant",
    "2. STEP-UP\n11kV -> 132kV\nPower Tr.",
    "3. TRANSMISSION\n132kV Line",
    "4. GRID S/S\n132kV -> 33kV",
    "5. DISTRIBUTION\n33kV -> 11kV",
    "6. D.T.\n11kV -> 440V",
    "7. HOME\nMeter -> MCB"
]

fig, ax = plt.subplots(figsize=(14, 2.5))
for i, stage in enumerate(stages):
    color = "lightyellow" if i%2==0 else "lightblue"
    ax.text(i*2, 0.5, stage, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.5", facecolor=color), fontsize=9, fontweight='bold')
    if i < len(stages)-1:
        ax.arrow(i*2+0.7, 0.5, 0.5, 0, head_width=0.07, head_length=0.1, fc='red', ec='red')

ax.set_xlim(-1, 13)
ax.set_ylim(0, 1)
ax.axis('off')
plt.title("GENERATION TO HOME - POWER FLOW", fontweight='bold')
plt.savefig("generation_to_home_workflow.png", dpi=300, bbox_inches='tight')
print("Done")
