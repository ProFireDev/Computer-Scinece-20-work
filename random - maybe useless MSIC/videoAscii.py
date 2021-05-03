import time
from moviepy.editor import *
import sys
from PIL import Image
import os

def play_video(ascii_list, frame_size, frame_rate):
    os.system(f'mode {frame_size[0]}, {frame_size[1]}')
    for frame in ascii_list:
        sys.stdout.write("\r" + frame)
        time.sleep(1/frame_rate)

# Extract frames from video
def extract_transform_generate(video_path, frame_size=[128,72], frame_rate=24, ascii_chars=["#", "@", ".", " "], resize=True):
    with VideoFileClip(video_path, audio=False, target_resolution=(frame_size[1], frame_size[0])) as clip:
        clip = clip.set_fps(frame_rate)
        number_of_frames = len(list(clip.iter_frames()))
        ascii_list = []
        for i, image_frame in enumerate(clip.iter_frames()):
            image = Image.fromarray(image_frame)
            if resize:
                image = resize_for_terminal(image, frame_size)
            ascii_characters = pixels_to_ascii(greyscale(image), ascii_chars)
            pixel_count = len(ascii_characters)
            ascii_image = "\n".join(
                [ascii_characters[index:(index + frame_size[0])] for index in range(0, pixel_count, frame_size[0])])
            ascii_list.append(ascii_image)
            #progress bar
            progress_bar(i+1, number_of_frames)
    return ascii_list

# Progress bar code is courtesy of StackOverflow user: Aravind Voggu.
# Link to thread: https://stackoverflow.com/questions/6169217/replace-console-output-in-python
def progress_bar(current, total, barLength=30):
    progress = float(current) * 100 / total
    arrow = '#' * int(progress / 100 * barLength - 1)
    spaces = ' ' * (barLength - len(arrow))
    sys.stdout.write('\rProgress: [%s%s] %d%% Frame %d of %d frames' % (arrow, spaces, progress, current, total))

# Resize image
def resize_for_terminal(image_frame, frame_size):
    width, height = image_frame.size
    aspect_ratio = (height / float(width * 2))  # modifier to offset vertical scaling
    new_height = int(aspect_ratio * frame_size[0])
    resized_image = image_frame.resize((frame_size[0], new_height))
    return resized_image

# Greyscale
def greyscale(image_frame):
    return image_frame.convert("L")

# Convert pixels to ascii
def pixels_to_ascii(image_frame, ascii_chars:list):
    pixels = image_frame.getdata()
    characters = "".join([ascii_chars[pixel // 64] for pixel in pixels])
    return characters

def main(frame_size, frame_rate, ascii_chars):
    sys.stdout.write('==============================================================\n')
    path = str(input("Please enter the video file name (file must be in root!): "))
    if os.path.exists(path):
        path_to_video = path.strip()
        start_time = time.time()
        sys.stdout.write('Beginning ASCII generation...\n')
        ascii_list = extract_transform_generate(path_to_video, frame_size, frame_rate, ascii_chars)
        execution_time = time.time() - start_time
        sys.stdout.write('ASCII generation completed! ASCII generation time: ' + str(execution_time))
    else:
        sys.stdout.write('Warning file not found!\n')

    play_video(ascii_list, frame_size, frame_rate)

def video2ascii(path, frame_size, frame_rate, ascii_chars):
    if os.path.exists(path):
        return extract_transform_generate(path, frame_size=frame_size, frame_rate=frame_rate, ascii_chars=ascii_chars, resize=False)
    else:
        raise FileNotFoundError()

if __name__ == '__main__':
    main(frame_size=[128,72], frame_rate=24, ascii_chars=["#", "@", ".", " "])
