import matplotlib.pyplot as plt
import numpy as np

def draw_fractal(ax, x, y, angle, depth, length):
    if depth == 0:
        return
    x_end = x + np.cos(angle) * length
    y_end = y + np.sin(angle) * length
    ax.plot([x, x_end], [y, y_end], color='white', lw=1)
    draw_fractal(ax, x_end, y_end, angle - np.pi/6, depth - 1, length * 0.7)
    draw_fractal(ax, x_end, y_end, angle + np.pi/6, depth - 1, length * 0.7)

def generate_fractal_image(depth=5):
    fig, ax = plt.subplots(figsize=(4, 6), dpi=100)
    ax.set_facecolor("black")
    ax.axis("off")
    ax.set_xlim(-150, 150)  # set fixed limits to avoid rendering nothing
    ax.set_ylim(0, 300)
    draw_fractal(ax, 0, 0, np.pi / 2, depth, 100)
    fig.tight_layout(pad=0)
    return fig