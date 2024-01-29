from pydub import AudioSegment

# scan all *.mp3 files in the directory
import os

# get the current directory
current_dir = os.getcwd()
print(current_dir)

# def join_mp3_files_with_silence(files, output_file):
#     # Load each MP3 file
#     segments = [AudioSegment.from_file(file, format="mp3") for file in files]

#     # Create 1-second silent gap
#     silent_gap = AudioSegment.silent(duration=1000)  # 1000 milliseconds = 1 second

#     # Concatenate the segments with the silent gap
#     final_segment = silent_gap.join(segments)

#     # Export the result to the output file
#     final_segment.export(output_file, format="mp3")

# if __name__ == "__main__":
#     # List of MP3 files to join
#     mp3_files = ["file1.mp3", "file2.mp3", "file3.mp3"]

#     # Output file name
#     output_file = "output.mp3"

#     # Join MP3 files with 1-second silent gaps
#     join_mp3_files_with_silence(mp3_files, output_file)

#     print(f"MP3 files joined successfully. Output file: {output_file}")
