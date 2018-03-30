import os
from PIL import Image
import matplotlib.pyplot as plt
from numpy import asarray

path = 'D:\\Documents\\Photos\\2018'
CAMERA_TYPE = 'pentax' # lowercase

f = []
t = []
focus = []

for root, dirs, files in os.walk(path):
    for file in files:

        if file.lower().endswith('.jpg'):
            filename = os.path.join(root, file)

            try:
                img = Image.open(filename, "r")
                exif_data = img._getexif()
            except:
                img.close()
                pass
            img.close()

            if exif_data is not None:
                try:
                    name = exif_data[271]

                    if CAMERA_TYPE in name.lower():
                        time = exif_data[0x829A]
                        stop = exif_data[0x829D]
                        fd = exif_data[37386]
                        f.append(stop[0]/float(stop[1]))
                        t.append(time[0]/float(time[1]))
                        focus.append(fd[0]/float(fd[1]))
                except KeyError:
                    pass


print('Number of photos: {}'.format(len(t)))

# x = np.asarray([f for f in focus if f <= 55])
plt.figure()
plt.hist(asarray(focus), normed=False, bins=20)
plt.ylabel('Number of photos');
plt.xlabel('Focal distance, mm');
plt.savefig('focal_distance.png')

plt.figure()
plt.hist(asarray(f), normed=False, bins=20)
plt.ylabel('Number of photos');
plt.xlabel('f number, mm');
plt.savefig('f_number.png')

plt.figure()
plt.hist(asarray(t), normed=False, bins=20)
plt.ylabel('Number of photos');
plt.xlabel('Shutter speed, s');
plt.savefig('shutter_speed.png')
