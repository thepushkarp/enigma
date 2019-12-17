"""
Takes in all the 21 plots and creates a looping gif
to see how the function changes with changing w
"""
from PIL import Image

def create_gif():
    # Create the frames
    FRAMES = []
    for i in range(20 + 1):
        img = 'csv{0:0>2d}/plot{0:0>2d}.png'.format(i)
        new_frame = Image.open(img)
        FRAMES.append(new_frame)

    # Save into a GIF file that loops forever
    FRAMES[0].save('plot.gif', format='GIF',
                   append_images=FRAMES[1:],
                   save_all=True,
                   duration=300, loop=0)
    print('gif saved as plot.gif')

if __name__ == "__main__":
    pass
