import glob                            
import moviepy.editor as mpy  
from natsort import natsorted

def makeclip(frameps):
    gif_name = 'analysed_sst' + '_' + str(frameps) + 'fps'
    file_list = glob.glob('PNG/*.png')
    lsorted = natsorted(file_list)
    clip = mpy.ImageSequenceClip(lsorted, fps=frameps)
    clip.write_gif('GIFF/{}.gif'.format(gif_name), fps=frameps)