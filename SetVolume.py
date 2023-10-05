import ctypes
import math
# Constants from the Windows API
WAVE_OUTPUT = 0x2

# Function to set the system volume level
def set_volume(volume_level):
    # Convert volume level from [0.0, 1.0] to a range of -65,535 to 0
    volume = int((volume_level ** (1 / 1.5)) * -65535.0)

    # Set the volume using the Windows API
    ctypes.windll.WINMM.waveOutSetVolume(WAVE_OUTPUT, volume)

def main():
    try:
        # Prompt the user to input a volume level
        volume_input = float(input("Enter the desired volume level (0.0 to 1.0): "))
        
        # Ensure the input is within the valid range
        volume_level = max(0.0, min(1.0, volume_input))
        
        set_volume(volume_level)
        print("Volume set successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()