import pyautogui
import keyboard
import time
import psutil

def measure_network_download_rate(inf):
    """
    Measures current network download speed
    """
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_1 = net_stat.bytes_recv
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_2 = net_stat.bytes_recv
    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    print(f"Current net download: {net_in} MB/s")
    return net_in

def click_on_image(image_path):
    """
    Searches for an image on screen and clicks on it if found.
    """
    buttonloc = pyautogui.locateOnScreen(image_path)
    if buttonloc is None:
        print(f"Couldn't find the download button!")
    else:
        center = pyautogui.center(buttonloc)
        oldpos = pyautogui.position()
        print(f"Found the download button, clicking on [{center[0]}, {center[1]}].")
        pyautogui.click(x=center[0], y=center[1])
        pyautogui.moveTo(oldpos)

def main():
    inf = 'Ethernet'
    print(f"{inf} selected.")

    input('Move this console Window so that it doesn\'t obstruct the download button. Then press Enter.')
    
    while True:
        # Break loop when CTRL+SHIFT+E is pressed
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('e'):
            break
            
        # Measure current network download speed
        net_in = measure_network_download_rate(inf)

        # If download speed is less than 1 MB/s, search for a slow download button image and click on it
        if net_in < 1:        
            sleep_timer = 8
            print('Searching for an image ...')
            click_on_image('slow download button.png')
        # If download speed is greater than 1 MB/s, set a shorter sleep timer to start over
        else:
            sleep_timer = 0.5

        # Sleep and start over
        print('Sleeping now. You can end this script by holding CTRL+SHIFT+E.')
        time.sleep(sleep_timer)

if __name__ == "__main__":
    main()
