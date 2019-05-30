from PIL import Image
import struct


def read_image(filename): #读取并且保存mnist图片
	f = open(filename, 'rb')

	index = 0
	buf = f.read()

	f.close()

	magic, images, rows, columns = struct.unpack_from('>IIII', buf, index)
	index += struct.calcsize('>IIII')

	for i in range(images):
		image = Image.new('L', (columns, rows))

		for x in range(rows):
			for y in range(columns):
				image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
				index += struct.calcsize('>B')
		print('save', str(i), 'image')
		image.save('/home/song-ruyang/PhuPythonClub/MiniProject/CNN/mnist/images/' + str(i) + '.png')


def read_label(filename, saveFilename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()

    f.close()

    magic, labels = struct.unpack_from('>II', buf, index)
    index += struct.calcsize('>II')

    labelArr = [0] * labels
    # labelArr = [0] * 2000

    for x in range(labels):  # 嫌太大可改成小一点的数字如2000
        labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
        index += struct.calcsize('>B')

    save = open(saveFilename, 'w')

    save.write(','.join(map(lambda x: str(x), labelArr)))
    save.write('\n')

    save.close()
    print('save labels success')


def test():
	read_image('/home/song-ruyang/PhuPythonClub/MiniProject/CNN/mnist/data/train-images.idx3-ubyte')
	read_label('/home/song-ruyang/PhuPythonClub/MiniProject/CNN/mnist/data/train-labels.idx1-ubyte', 
			   '/home/song-ruyang/PhuPythonClub/MiniProject/CNN/mnist/labels.txt')


if __name__ == "__main__":
	test()
	