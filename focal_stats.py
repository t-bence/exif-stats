import os
from PIL import Image
import matplotlib.pyplot as plt
from numpy import asarray

f = []
t = []
focus = []

for root, dirs, files in os.walk("D:\Documents\Photos"):
# root = "D:\Documents\Photos\\2017\Elso_kepek"
    for file in files:

        # print name
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

                    if 'PENTAX' in name:
                        time = exif_data[0x829A]
                        stop = exif_data[0x829D]
                        fd = exif_data[37386]
                        f.append(stop[0]/float(stop[1]))
                        t.append(time[0]/float(time[1]))
                        focus.append(fd[0]/float(fd[1]))
                except KeyError:
                    pass


print len(t)

# x = np.asarray([f for f in focus if f <= 55])
x = np.asarray(focus)
plt.hist(x, normed=False, bins=20)
plt.ylabel('Number of photos');
plt.xlabel('Focal distance, mm');
plt.savefig('focal_distances.png')

            