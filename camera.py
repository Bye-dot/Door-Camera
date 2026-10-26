from machine import Pin as PIN

cam = PIN(5, PIN.IN);

def cam_stat():
    return cam.value()