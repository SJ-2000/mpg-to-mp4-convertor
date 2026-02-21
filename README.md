# MPG to MP4 Converter

Simple Python script to convert MPG files to MP4 using FFmpeg.

**Prerequisites:**
- Python 3.8 or newer
- FFmpeg installed and added to your PATH (required)
- Optional Python libraries if the script uses them: `moviepy`, `ffmpeg-python`

**Install FFmpeg (Windows)**
1. Download a build from https://ffmpeg.org/download.html or https://www.gyan.dev/ffmpeg/builds/
2. Extract and add the `bin` folder to your system `PATH`.

**Create a Python virtual environment (recommended)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Install Python dependencies (optional)**
If the script requires Python packages, create a `requirements.txt` with the packages you need, for example:

```
moviepy==1.0.3
ffmpeg-python==0.2.0
```

Then run:

```powershell
pip install -r requirements.txt
```

**Run the converter**

From the repository root run:

```powershell
# Example: convert a single file (if supported by the script)
python convertor.py input.mpg output.mp4

# Example: run with no args (if script processes the working directory)
python convertor.py
```

Adjust the command to match how `convertor.py` accepts input and output paths.

**Troubleshooting**
- If you see "ffmpeg: command not found", ensure FFmpeg is installed and on your PATH.
- If Python cannot find a library, install it with `pip install <package>` or use the `requirements.txt` approach above.

**Notes**
- This repository contains `convertor.py`; inspect it to confirm required arguments or dependencies.
- Add a `requirements.txt` if you want reproducible installs.

**License**
This project has no license declared. Add one if you plan to publish the code.
