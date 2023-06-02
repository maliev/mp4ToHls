import subprocess

def convert_to_hls(input_file, output_directory, output_file_prefix, quality_levels):
    # Generate a unique output file name for each quality level
    output_files = [f"{output_directory}/{output_file_prefix}_{i}.m3u8" for i in range(1, quality_levels + 1)]

    # Set the command to convert the video to HLS
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vf", "scale=w=-2:h=720",
        "-c:v", "h264",
        "-crf", "23",
        "-g", "48",
        "-keyint_min", "48",
        "-sc_threshold", "0",
        "-b:v", "1500k",
        "-maxrate", "1500k",
        "-bufsize", "1200k",
        "-hls_time", "10",
        "-hls_playlist_type", "vod",
        "-hls_segment_filename", f"{output_directory}/%v_%03d.ts",
        "-hls_flags", "split_by_time+append_list",
    ]

    # Append the output file names to the command
    command.extend(output_files)

    # Run the ffmpeg command
    subprocess.run(command)

    # Return the list of output file names
    return output_files

# Example usage
input_file = "input.mp4"
output_directory = "output"
output_file_prefix = "output"
quality_levels = 5

convert_to_hls(input_file, output_directory, output_file_prefix, quality_levels)
