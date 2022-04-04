from screeninfo import get_monitors

def get_resolution(x=0, y=0):
    for monitor in get_monitors(): (x, y) = int(monitor.width), int(monitor.height) if monitor.is_primary else (int(1280), int(720))
    return x, y
