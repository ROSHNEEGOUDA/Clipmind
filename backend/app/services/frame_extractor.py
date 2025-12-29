import os
import subprocess

def extract_frames(
    video_path: str,
    output_dir: str,
    fps: float = 0.02
):
    """
    Extract key frames from video using FFmpeg.
    """

    os.makedirs(output_dir, exist_ok=True)

    output_pattern = os.path.join(output_dir, "frame_%03d.jpg")

    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "error",
        "-i", video_path,
        "-vf", f"fps={fps}",
        output_pattern
    ]

    subprocess.run(cmd, check=True)

    return [
        os.path.join(output_dir, f)
        for f in sorted(os.listdir(output_dir))
        if f.endswith(".jpg")
    ]