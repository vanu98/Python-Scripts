#Author: Varnesh Gawde
#Date 9/9/2023
#Auto mouse move
import pyautogui
import time

def keep_moving(interval=3, move_distance=100):
    """
    Keep moving the mouse cursor back and forth to prevent system inactivity.
    
    Parameters:
    - interval: Time in seconds after which the mouse will be moved.
    - move_distance: Distance in pixels to move the mouse.
    """
    
    while True:
        # Move the mouse to a location
        pyautogui.moveRel(move_distance, 0, duration=0.5)
        
        # Wait for the specified interval
        time.sleep(interval)
        
        # Move the mouse back to the original location
        pyautogui.moveRel(-move_distance, 0, duration=0.5)
        
        # Wait for the specified interval again
        time.sleep(interval)

if __name__ == "__main__":
    keep_moving()