def compare_images(imageA, imageB, title):
    # https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
    ### As of Verion 0.14 - ``skimage.measure.structural_similarity`` has been removed. Use ``skimage.measure.compare_ssim`` instead.
	### As of Version 0.18 - skimage.measure.compare_ssim has been moved to skimage.metrics.structural_similarity
    # Pre-requisites
    ### pip3 install scikit-image numpy matplotlib opencv-python

    from skimage.metrics import structural_similarity as ssim
    import matplotlib.pyplot as plt
    import numpy as np
    import cv2    # opencv-python

#    imageA = cv2.imread(imageAfile)
#    imageB = cv2.imread(imageBfile)

    def mse(imageA, imageB):
#        import cv2
#        imageA = cv2.imread(imageAfile)
#        imageB = cv2.imread(imageBfile)

        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        
        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err


    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()


##################################################

#capture_Screenshot()
#compare_images1( "out_qima.png", "qima.png" )

from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2    # opencv-python


# load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("qima.png")
contrast = cv2.imread("qima.png")
shopped = cv2.imread("qima.png")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# initialize the figure
#fig = plt.figure("Images")
#images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)

# loop over the images
#for (i, (name, image)) in enumerate(images):
    # show the image
#    ax = fig.add_subplot(1, 3, i + 1)
#    ax.set_title(name)
#    plt.imshow(image, cmap = plt.cm.gray)
#    plt.axis("off")

# show the figure
#plt.show()

# compare the images
compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
compare_images(original, shopped, "Original vs. Photoshopped")


#####

readme = """
It’s important to note that a value of 0 for MSE indicates perfect similarity. 
A value greater than one implies less similarity and will continue to grow as the 
average difference between pixel intensities increases as well.

In order to remedy some of the issues associated with MSE for image comparison, we 
have the Structural Similarity Index, developed by Wang et al.:

The SSIM method is clearly more involved than the MSE method, but the gist is that 
SSIM attempts to model the perceived change in the structural information of the 
image, whereas MSE is actually estimating the perceived errors. There is a subtle 
difference between the two, but the results are dramatic.

Furthermore, the equation in Equation 2 is used to compare two windows (i.e. small
sub-samples) rather than the entire image as in MSE. Doing this leads to a more 
robust approach that is able to account for changes in the structure of the image, 
rather than just the perceived change.

The parameters to Equation 2 include the (x, y) location of the N x N window in 
each image, the mean of the pixel intensities in the x and y direction, the 
variance of intensities in the x and y direction, along with the covariance.

Unlike MSE, the SSIM value can vary between -1 and 1, where 1 indicates perfect 
similarity.
"""
