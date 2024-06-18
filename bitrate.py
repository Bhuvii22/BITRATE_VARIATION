import argparse
import subprocess

def process_ip_camera(input_url, output_url, bitrate_mode=None, bitrate=None, duration=None,preset=None,crf=None):
    cmd = ['ffmpeg','-rtsp_transport', 'tcp', '-i', input_url]

    # if fps:
    #     if fps_mode == 'increase_fps':
    #         cmd.extend(['-r', str(fps)])  # Increase FPS using -r
    #     elif fps_mode == 'decrease_fps':
    #         cmd.extend(['-filter:v', f'fps=fps={fps}'])  # Decrease FPS using -filter:v

    if bitrate:
        if bitrate_mode == 'increase_bitrate':
            
            increased_bitrate = str(int(bitrate.rstrip('k')) * 2) + 'k'
            cmd.extend(['-b:v', increased_bitrate])
        elif bitrate_mode == 'decrease_bitrate':
            
            decreased_bitrate = str(int(bitrate.rstrip('k')) // 2) + 'k'
            cmd.extend(['-b:v', decreased_bitrate])
       
    # if resolution:
    #     cmd.extend(['-s', resolution])
    
    if duration:
        cmd.extend(['-t', duration])
    cmd.extend(['-c:v', 'libx264'])

    if preset:
        cmd.extend(['-preset',preset])
    
    if crf:
        cmd.extend(['-crf',crf])
    
    cmd.append(output_url)
    subprocess.run(cmd)

def main():
    parser = argparse.ArgumentParser(description='Video Processing Script with FFmpeg')
    # parser.add_argument('--fps_mode', choices=['increase_fps', 'decrease_fps'], help='Mode for adjusting FPS')
    parser.add_argument('--bitrate_mode', choices=['increase_bitrate', 'decrease_bitrate'], help='Mode for adjusting bitrate')
    parser.add_argument('--input', required=True, help='Input source (URL or file)')
    parser.add_argument('--output', required=True, help='Output file or URL')
    # parser.add_argument('--fps', type=int, help='Frames per second')
    parser.add_argument('--bitrate', help='Bitrate (e.g., 500k, 2M)')
    # parser.add_argument('--resolution', help='Resolution (e.g., 1280x720)')
    parser.add_argument('--duration', help='Duration of the output video (e.g., 10, 00:01:00 for 1 minute)')
    parser.add_argument('--preset', help='preset values (e.g.,small,medium)')
    parser.add_argument('--crf', help='constant rate factor (e.g., 40)')
    args = parser.parse_args()
    process_ip_camera(args.input, args.output,  args.bitrate_mode,args.bitrate, args.duration,args.preset,args.crf)

if __name__ == '__main__':
    main()
