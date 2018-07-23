import sys, time, signal, shutil
import colorsys, subprocess

from tplight import LB130
from img_proc import screen_avg

def kill(signal, frame):
    # src: http://stackoverflow.com/questions/32922909/how-to-stop-an-infinite-loop-safely-in-python
    global quit_soon
    quit_soon = True

def main():
    assert len(sys.argv) == 2
    light_ip = sys.argv[1]
    assert "." in light_ip
    
    assert shutil.which("brightness") is not None
    
    signal.signal(signal.SIGINT, kill)
    global quit_soon
    quit_soon = False
    
    light = LB130(light_ip)
    #print(light.light_details())
    time.sleep(1)
    
    while True:
        if quit_soon:
            break
        
		# get output of screen brightness command
        output = subprocess.check_output(['brightness', '-l'])
        brightness = float(str(output).split('display 0: brightness ')[-1][:-3])
        
        # get avg RGB color of screen
        r, g, b = screen_avg()['rgb'] # 3-tuple
        hue, lightness, sat = colorsys.rgb_to_hls(r/255, g/255, b/255)
        
        # set new hue & sat
        avg_brightness = min((brightness + lightness) / 2 * 1.15, 1)
        light.hsb = (int(hue*360), int(sat*100), int(avg_brightness*100))

        break # testing purposes
        #time.sleep(5)

if __name__ == '__main__':
    main()