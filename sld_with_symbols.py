import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(15, 4))
ax.set_xlim(0, 14)
ax.set_ylim(0, 2)
ax.axis('off')

def line(x1,x2,y=1):
    ax.plot([x1,x2],[y,y],'k-',lw=2)

# 1. GENERATOR
c = patches.Circle((0.7,1),0.35, fill=False, lw=2.5)
ax.add_patch(c)
ax.text(0.7,1,'G', ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(0.7,0.15,'GENERATION\n11kV', ha='center', fontsize=8, fontweight='bold')
line(1.05,1.8)

# 2. STEP-UP TRANSFORMER (2 coil)
ax.add_patch(patches.Circle((2.0,1),0.22, fill=False, lw=2))
ax.add_patch(patches.Circle((2.45,1),0.22, fill=False, lw=2))
ax.text(2.22,0.15,'STEP-UP Tr\n11/132kV', ha='center', fontsize=8, fontweight='bold')
line(2.67,3.3)

# 3. TRANSMISSION TOWER
ax.plot([3.7,3.7],[0.5,1.5],'k-',lw=2.5)
ax.plot([3.5,3.9],[1.3,1.3],'k-',lw=2)
ax.plot([3.5,3.9],[1.1,1.1],'k-',lw=2)
ax.text(3.7,0.15,'TRANSMISSION\n132kV Tower', ha='center', fontsize=8, fontweight='bold')
line(3.9,4.6)

# 4. GRID SUBSTATION
ax.add_patch(patches.Circle((4.9,1),0.22, fill=False, lw=2))
ax.add_patch(patches.Circle((5.35,1),0.22, fill=False, lw=2))
ax.text(5.12,0.15,'GRID S/S\n132/33kV', ha='center', fontsize=8, fontweight='bold')
line(5.57,6.3)

# 5. 11kV FEEDER + BREAKER
ax.add_patch(patches.Rectangle((6.5,0.85),0.3,0.3, fill=False, lw=2))
ax.text(6.65,1,'CB', ha='center', va='center', fontsize=7, fontweight='bold')
ax.text(6.65,0.15,'11kV FEEDER', ha='center', fontsize=8, fontweight='bold')
line(6.8,7.5)

# 6. DISTRIBUTION TRANSFORMER
ax.add_patch(patches.Circle((7.8,1),0.22, fill=False, lw=2))
ax.add_patch(patches.Circle((8.25,1),0.22, fill=False, lw=2))
ax.text(8.02,0.15,'D.T.\n11kV/440V', ha='center', fontsize=8, fontweight='bold')
line(8.47,9.2)

# 7. METER + MCB + HOME
ax.add_patch(patches.Rectangle((9.4,0.8),0.4,0.4, fill=False, lw=2))
ax.text(9.6,1,'M', ha='center', va='center', fontweight='bold')
ax.add_patch(patches.Rectangle((10.2,0.85),0.3,0.3, fill=False, lw=2))
ax.text(10.35,1,'MCB', ha='center', va='center', fontsize=6)
# Home symbol
ax.add_patch(patches.Rectangle((11,0.7),0.7,0.6, fill=False, lw=2))
ax.plot([11,11.35,11.7],[1.3,1.6,1.3],'k-',lw=2)
ax.text(9.6,0.15,'METER', ha='center', fontsize=8, fontweight='bold')
ax.text(11.35,0.15,'HOME\n230V Load', ha='center', fontsize=8, fontweight='bold')

plt.title("GENERATION TO HOME - IS Standard SLD with Generator & Transformer Symbols", fontweight='bold', fontsize=11)
plt.savefig("sld_with_symbols.png", dpi=300, bbox_inches='tight')
print("SLD with symbols created")
