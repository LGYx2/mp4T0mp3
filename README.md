
```markdown
# MP4 to MP3 Converter

This Python script allows you to convert MP4 files into MP3 format. It can be used to convert a single MP4 file or all MP4 files in a folder. The script uses the `pydub` library to handle the conversion process.

## Requirements

Before running the script, make sure to install the necessary dependencies:

### Python Dependencies

- *pydub*: This library is used for handling audio file conversions, including converting MP4 to MP3.
- *ffmpeg* or *libav*: These are required by `pydub` to process audio files. They are essential for handling the media decoding and encoding processes.

### Install Dependencies

To install the required Python package, run the following command:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```text
pydub==0.25.1
```

### Install FFmpeg

`pydub` relies on FFmpeg for the actual audio conversion process. You will need to install FFmpeg on your system.

#### For Windows:
1. Download FFmpeg from the [official website](https://ffmpeg.org/download.html).
2. Extract the contents and add the `bin` folder to your system's `PATH` environment variable.

#### For macOS:
If you're using Homebrew, you can install FFmpeg by running:

```bash
brew install ffmpeg
```

#### For Linux (Ubuntu/Debian):
You can install FFmpeg using apt:

```bash
sudo apt update
sudo apt install ffmpeg
```

After setting up the dependencies, you're ready to run the script.

## Usage

The script can be run from the command line to convert MP4 files to MP3. You can convert a single file or all files in a directory.

### Convert a Single MP4 File to MP3

To convert a single MP4 file, run the following command:

```bash
python script.py "C:/path/to/your/file.mp4"
```

This will convert the specified MP4 file into an MP3 file and save it in the same directory.

### Convert All MP4 Files in a Folder

To convert all MP4 files within a folder, run the following command:

```bash
python script.py "C:/path/to/your/folder"
```

This will convert all MP4 files in the specified folder and save them as MP3 files in the same folder.

### Specify an Output Directory

You can specify an output directory where the MP3 files will be saved. Run the following command:

```bash
python script.py "C:/path/to/your/folder" "C:/path/to/output/folder"
```

This will convert all MP4 files in the input folder and save them as MP3 files in the specified output directory.

### Help Command

If you need help with the script or want to see the available commands, you can run the following:

```bash
python script.py --help
```

This will display a help message that provides an overview of the script's usage and arguments.

```
Usage:
    python script.py [--help] [input_folder] [output_directory]

Arguments:
    input_folder        Path to the folder containing MP4 files to convert to MP3.
    output_directory    Optional. Directory where MP3 files will be saved. Defaults to the same folder as the MP4 files.

Options:
    --help              Show this help message and exit.

Example:
    python script.py "C:/path/to/mp4/files" "C:/path/to/output/folder"
    python script.py "C:/path/to/mp4/files"  (will save MP3s in the same folder as the MP4 files)
```

## Script Details

### `convert_mp4_to_mp3(input_file, output_dir=None)`

This function is used to convert a single MP4 file to MP3.

- **input_file**: The path to the MP4 file that you want to convert.
- **output_dir**: The directory where the MP3 file will be saved. If not provided, the MP3 file will be saved in the same directory as the input file.

### `convert_folder(input_folder, output_dir=None)`

This function is used to convert all MP4 files in the specified folder to MP3.

- **input_folder**: The path to the folder containing MP4 files.
- **output_dir**: The directory where MP3 files will be saved. If not provided, the MP3 files will be saved in the same directory as the MP4 files.

## Example of Usage

1. **Convert a single MP4 file:**

   ```bash
   python script.py "C:/path/to/your/file.mp4"
   ```

   This converts `file.mp4` into `file.mp3` in the same folder.

2. **Convert all MP4 files in a folder:**

   ```bash
   python script.py "C:/path/to/your/folder"
   ```

   This converts all MP4 files in `folder` to MP3 and saves them in the same folder.

3. **Convert all MP4 files in a folder and save them to a different directory:**

   ```bash
   python script.py "C:/path/to/your/folder" "C:/path/to/output/folder"
   ```

   This converts all MP4 files in `folder` and saves the MP3 files to the `output/folder`.

## License

This script is provided as-is. You are free to use, modify, and distribute it under your own terms.

---

By using this script, you agree to the terms mentioned above. If you encounter any issues or need additional features, feel free to contribute by opening an issue or pull request.

## Additional Info

if you want a tool to be able to download yt MP4 files in a very simple way check out the [yt-dlp GitHub Repository](https://github.com/yt-dlp/yt-dlp)
```

