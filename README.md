# lb130-lightsync

Small script to update the hue, lightness and saturation of the LB130 bulb using the average brightness and color of your computer screen. Very rudimentary. Some part is Mac only.

Usage: python3 lightsync.py lightIP

Libraries used:

* [tp-link LB130 Smart Wi-Fi Bulb Python Control](https://github.com/briandorey/tp-link-LB130-Smart-Wi-Fi-Bulb)
* [Code to determine average screen color from Screenbloom](https://github.com/kershner/screenBloom/blob/d89d3cf9655ee4b10cd1151d8b307665f69a88b2/app/modules/img_proc.py#L103)
* [Command-line brightness tool for Mac](https://github.com/nriley/brightness)