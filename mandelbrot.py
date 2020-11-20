import numpy as np
import matplotlib.pyplot as plt


def to_rgb(argb_int):
    blue =  argb_int & 255
    green = (argb_int >> 8) & 255
    red =   (argb_int >> 16) & 255
    return (red, green, blue)


def main():
	image_height = 10
	image_width = 10
	refresh_rate = 0.5	# in seconds
	max_iter = 100

	fig = plt.gcf()
	fig.show()
	fig.canvas.draw()
	img = np.zeros((image_height, image_width, 3), np.uint8)

	for i in range(image_height):
		for j in range(image_width):
			print(i, j)
			x0 = (1 - (-2.5)) * (i / (image_height - 1)) + (-2.5)
			y0 = (1 - (-1)) * (j / (image_width - 2)) + (-1)
			x = 0
			y = 0
			iter = 0
			while (((x**2) + (y**2) <= 2**2) and iter < max_iter):
				xtemp = x**2 - y**2 + x0
				y = 2*x*y + y0
				x = xtemp
				iter += 1
			img[i, j] = to_rgb(iter)
			plt.imshow(img)
			plt.pause(refresh_rate)
			fig.canvas.draw()


if __name__ == '__main__':
	main()