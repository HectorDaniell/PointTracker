import cv2
import numpy as np
from PIL import Image, ImageSequence

def load_gif_frames(gif_path, scale=2.5, skip_frames=3):
    gif = Image.open(gif_path)
    frames = []
    w, h = gif.size
    new_size = (int(w * scale), int(h * scale))
    count = 0
    for frame in ImageSequence.Iterator(gif):
        if count % skip_frames == 0:
            canvas = Image.new("RGBA", gif.size, (0, 0, 0, 255))
            canvas.paste(frame.convert("RGBA"), (0, 0), frame.convert("RGBA"))
            
            final_frame = canvas.convert("RGB").resize(new_size, Image.Resampling.NEAREST)
            frame_cv = cv2.cvtColor(np.array(final_frame), cv2.COLOR_RGB2BGR)
            frames.append(frame_cv)
        count += 1
        
    return frames