import os

imdir = 'data/parking_spaces'
if not os.path.isdir(imdir):
        os.mkdir(imdir)

parking_folders = [os.path.join('images', folder) for folder in os.listdir('./images') if 'parking' in folder]

n = 0
for folder in parking_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
        n += 1
