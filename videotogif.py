"""
Module: video_to_gif_converter

This module provides functionality to convert a video file to a GIF using the moviepy library.
"""

from moviepy.editor import VideoFileClip

def convert_to_gif(video_path, gif_path):
    """
    Convert a video file to a GIF.

    Parameters:
        video_path (str): Path to the input video file.
        gif_path (str): Path to save the output GIF file.

    Returns:
        None
    """
    clip = VideoFileClip(video_path)
    clip.write_gif(gif_path)

# Example usage:
# convert_to_gif('input_video.mp4', 'output.gif')

