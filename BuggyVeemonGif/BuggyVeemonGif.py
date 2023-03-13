import imageio

filenames = [ 'insert', 'files', 'names', 'here']
images = []

for file in filenames:
    images.append(imageio.imread(file))
    # The .imread() method loads an image based on the file path. So now, our images variable has all the images!
    imageio.mimsave('BuggyVeemon.gif', images, duration = 0.5)
    # This takes in three arguments:
        # 'team.gif': The new file name
        # images: The list of image data
        # duration = 0.5: The number of seconds

    