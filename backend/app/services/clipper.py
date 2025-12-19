import subprocess
import os
import tempfile

def create_vertical_clip(input_path, output_path, start, duration):
    cmd = [
        "ffmpeg",
        "-y",
        "-ss", str(start),
        "-i", input_path,
        "-t", str(duration),
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-preset", "fast",
        "-movflags", "+faststart",
        output_path
    ]
    subprocess.run(cmd, check=True)


def create_reel_from_chunks(input_path, output_path, highlights):
    temp_files = []

    try:
        # Cut chunks
        for i, h in enumerate(highlights):
            temp_clip = tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp4"
            ).name

            create_vertical_clip(
                input_path=input_path,
                output_path=temp_clip,
                start=h["start"],
                duration=h["duration"]
            )

            temp_files.append(temp_clip)

        # Create concat file
        concat_file = tempfile.NamedTemporaryFile(
            delete=False, suffix=".txt", mode="w"
        )

        for f in temp_files:
            concat_file.write(f"file '{f}'\n")

        concat_file.close()

        # Concatenate
        cmd = [
            "ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_file.name,
            "-c", "copy",
            output_path
        ]
        subprocess.run(cmd, check=True)

    finally:
        # Cleanup temp files
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)
