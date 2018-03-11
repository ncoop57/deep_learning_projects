import os
import cv2
from lxml import etree
import xml.etree.cElementTree as et

def write_xml(folder, img, objects, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    height, width, depth = image.shape

    annotation = et.Element('annotation')
    et.SubElement(annotation, 'folder').text = folder
    et.SubElement(annotation, 'filename').text = img.name
    et.SubElement(annotation, 'segmented').text = '0'

    size = et.SubElement(annotation, 'size')
    et.SubElement(size, 'width').text = str(width)
    et.SubElement(size, 'height').text = str(height)
    et.SubElement(size, 'depth').text = str(depth)

    for obj, topl, botr in zip(objects, tl, br):
        ob = et.SubElement(annotation, 'object')
        et.SubElement(ob, 'name').text = obj
        et.SubElement(ob, 'pose').text = 'Unspecified'
        et.SubElement(ob, 'truncated').text = '0'
        et.SubElement(ob, 'difficult').text = '0'

        bbox = et.SubElement(ob, 'bndbox')
        et.SubElement(bbox, 'xmin').text = str(topl[0])
        et.SubElement(bbox, 'ymin').text = str(topl[1])
        et.SubElement(bbox, 'xmax').text = str(botr[0])
        et.SubElement(bbox, 'ymax').text = str(botr[1])

    xml_str = et.tostring(annotation)
    root = etree.fromstring(xml_str)

    xml_str = etree.tostring(root, pretty_print = True)
    save_path = os.path.join(savedir, img.name.replace('png', 'xml'));
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str);


if __name__ == '__main__':
    folder = 'images_folder'
    img = [ im for im in os.scandir('data/parking_spaces') if '000001' in im.name][0]

    objects = ['parking_space']
    tl = [(10, 10)]
    br = [(100, 100)]
    savedir = 'annotations'
    write_xml(folder, img, objects, tl, br, savedir)


