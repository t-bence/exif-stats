import os
from PIL import Image
import matplotlib.pyplot as plt
from numpy import asarray, logspace, log10
from sys import argv

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0][1:]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def process_images(path, camera_type):
    f = []
    t = []
    focus = []

    for root, dirs, files in os.walk(path):
        for file in files:

            if file.lower().endswith('.jpg'):
                filename = os.path.join(root, file)

                try:
                    img = Image.open(filename, 'r')
                    exif_data = img._getexif()
                except:
                    img.close()
                    print('Error opening image {}, exiting'.format(filename))
                    pass
                img.close()

                if exif_data is not None:
                    try:
                        name = exif_data[271]
                        if (camera_type is None) or (camera_type.lower() in name.lower()):
                            time = exif_data[0x829A]
                            stop = exif_data[0x829D]
                            fd = exif_data[37386]
                            f.append(stop[0]/float(stop[1]))
                            t.append(time[0]/float(time[1]))
                            focus.append(fd[0]/float(fd[1]))
                    except KeyError:
                        print('Error while reading EXIF data in image {}'.format(filename))
                        pass


    print('Number of photos: {}'.format(len(t)))

    if focus:
        # x = np.asarray([f for f in focus if f <= 55])
        plt.figure()
        plt.hist(asarray(focus), normed=False, bins=30)
        plt.ylabel('Number of photos');
        plt.xlabel('Focal distance, mm');
        plt.savefig('focal_distance.png')

    if f:
        plt.figure()
        plt.hist(asarray(f), normed=False, bins=30)
        plt.ylabel('Number of photos');
        plt.xlabel('f number, mm');
        plt.savefig('f_number.png')

    if t:
        plt.figure()
        plt.hist(asarray(t), normed=False, bins=logspace(log10(min(t)), log10(max(t)), 30))
        plt.ylabel('Number of photos');
        plt.xlabel('Shutter speed, s');
        plt.gca().set_xscale("log")
        plt.savefig('shutter_speed.png')
        
    return (f, t, focus)


if __name__ == '__main__':
    args = getopts(argv)
    if 'path' not in args:
        args['path'] = '.'
    if 'type' not in args:
        args['type'] = None

    process_images(args['path'], args['type'])
    
    


