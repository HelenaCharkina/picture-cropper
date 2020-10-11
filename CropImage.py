def crop_image(img, params):

    widthImg, heightImg = img.size

    x = widthImg * params["x"]
    y = widthImg * params["y"]
    width = widthImg * params["width"]
    height = widthImg * params["height"]

    area = (x, y, x + width, y + height)
    cropped_img = img.crop(area)
    cropped_img.show()
    cropped_img.save("saved_images/"+params["number"]+".png")