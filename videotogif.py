from moviepy.editor import VideoFileClip
import random
import os

def convert_to_gif(video_path, gif_path, fps=5, optimize=True, fuzz=2):
    """
    Convert a random 20-second segment of a video file to a GIF with the smallest and most stable size.

    Parameters:
        video_path (str): Path to the input video file.
        gif_path (str): Path to save the output GIF file.
        fps (int, optional): Frames per second of the GIF. Lower values reduce file size. Default is 5.
        optimize (bool, optional): Whether to apply GIF optimization. Default is True.
        fuzz (int, optional): Parameter to control dithering. Lower values produce smoother colors. Default is 2.

    Returns:
        None
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"The video file '{video_path}' does not exist.")
    
    clip = VideoFileClip(video_path)
    total_duration = clip.duration
    
    if total_duration < 20:
        raise ValueError("The video duration is less than 20 seconds.")
    
    # Generate a random starting point within the video duration
    start_time = random.uniform(0, total_duration - 20)  # Ensure at least 20 seconds left after the start point
    
    # Extract 20 seconds starting from the randomly chosen start point
    sub_clip = clip.subclip(start_time, start_time + 20)
    
    # Write the extracted clip as a GIF with optimized parameters
    sub_clip.write_gif(gif_path, fps=fps, opt=optimize, fuzz=fuzz)
