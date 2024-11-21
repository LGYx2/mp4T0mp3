from pydub import AudioSegment
import os

def convert_mp4_to_mp3(input_file, output_dir=None):
    """
    Convert a single MP4 file to MP3.
    
    :param input_file: Path to the MP4 file.
    :param output_dir: Directory where the MP3 file will be saved.
    """
    try:
        # Load the MP4 file
        audio = AudioSegment.from_file(input_file, format="mp4")

        # Determine output directory
        if not output_dir:
            output_dir = os.path.dirname(input_file)  # Use input file's directory

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Create the output file path
        output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + ".mp3")

        # Export as MP3
        audio.export(output_file, format="mp3")
        print(f"Converted: {input_file} -> {output_file}")

    except Exception as e:
        print(f"Failed to convert {input_file}: {e}")


def convert_folder(input_folder, output_dir=None):
    """
    Convert all MP4 files in a folder to MP3.
    
    :param input_folder: Path to the folder containing MP4 files.
    :param output_dir: Directory where MP3 files will be saved.
    """
    try:
        # Get all MP4 files in the folder
        mp4_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith(".mp4")]

        if not mp4_files:
            print(f"No MP4 files found in folder: {input_folder}")
            return

        # Convert each file
        for mp4_file in mp4_files:
            convert_mp4_to_mp3(mp4_file, output_dir)

    except Exception as e:
        print(f"Error processing folder {input_folder}: {e}")


if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing MP4 files: ").strip().replace("\\", "/")
    output_directory = input("Enter the output directory (leave blank to save in the same folder as the MP4 files): ").strip().replace("\\", "/")

    if not os.path.isdir(input_folder):
        print(f"Invalid folder path: {input_folder}")
    else:
        if not output_directory:
            output_directory = None  # Use default behavior
        convert_folder(input_folder, output_directory)
