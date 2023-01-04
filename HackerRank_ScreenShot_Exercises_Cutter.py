import matplotlib.image as mpimg
import os

# e.g. /home/hardli/python/HackerRank
op_path = '/home/hardli/python/HackerRank'
img_lst = [i for i in os.listdir(op_path) if i.endswith('png') and not i.endswith('cut.png')]
img_lst.sort()


stop = False
while stop == False:
    
    print(img_lst)
    # select images
    img_name = input("Give the name of the image to be cut: ")
    img = mpimg.imread(op_path + '/' + img_name)
    # screenshot size: H=1080, W=1920, C=4
    H,W,C = img.shape
    # print(H,W)
    # plt.imshow(img)

    # cut images
    cut_img = img[130:1020,150:650,:]
    # plt.imshow(cut_img)

    # output images
    output_path = op_path + '/' + img_name[:-4] + '_cut.png'
    mpimg.imsave(output_path, arr = cut_img)

    # remove current image
    img_lst.remove(img_name)

    # stop or not
    stop_order = input("Stop or not? y/n: ")
    if stop_order == 'y':
        stop = True
    elif stop_order == 'n':
        stop = False