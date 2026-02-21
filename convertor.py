import os
import subprocess

# Folder containing your MPG videos
INPUT_FOLDER = r"D:\Kochi-Allappi 2026\digicam" # change this
OUTPUT_FOLDER = r"D:\Kochi-Allappi 2026\converted" # change this if needed

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(".mpg"):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_filename = os.path.splitext(filename)[0] + ".mp4"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        print(f"Converting: {filename}")

        command = [
            "ffmpeg",
            "-i", input_path,
            "-c:v", "libx264",   # H.264 video codec
            "-c:a", "aac",       # AAC audio codec
            "-preset", "medium",
            "-crf", "23",        # Quality (lower = better quality)
            output_path
        ]

        subprocess.run(command)

print("✅ All conversions completed.")