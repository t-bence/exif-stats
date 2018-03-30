# exif-stats
Get focal length and shutter speed distribution from photos

# Summary
This is a simple script that gathers all JPEG photos from a specified folder, reads their EXIF data and displays
the distribution of focal length, shutter speed and aperture f-number as histograms. 
These diagrams are saved as PNG images. The function also returns the data as variables.
It can also filter and only list those photos created with a specified camera model.

# Usage:
```
python focal_stats.py -path 'D:\Documents\Photos' -type 'Pentax'
```
or simply:
```
python focal_stats.py
```
In this case, the current directory is applied and all photos are considered.

If you have any problems or requests, feel free to contact me!
