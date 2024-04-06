"""
Module: video_to_gif_converter

This module provides functionality to convert a video file to a GIF using the moviepy library.
"""

from moviepy.editor import VideoFileClip
import random

def convert_to_gif(video_path, gif_path):
    """
    Convert a random 20-second segment of a video file to a GIF.

    Parameters:
        video_path (str): Path to the input video file.
        gif_path (str): Path to save the output GIF file.

    Returns:
        None
    """
    clip = VideoFileClip(video_path)
    total_duration = clip.duration
    
    # Generate a random starting point within the video duration
    start_time = random.uniform(0, total_duration - 20)  # Ensure at least 20 seconds left after the start point
    
    # Extract 20 seconds starting from the randomly chosen start point
    sub_clip = clip.subclip(start_time, start_time + 20)
    
    # Write the extracted clip as a GIF
    sub_clip.write_gif(gif_path)


