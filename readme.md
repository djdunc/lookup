# Look Up

Thermal imaging, also known as infrared imaging, allows us to visualize and capture thermal energy emitted by objects in the form of heat. By detecting these temperature variations, thermal cameras provide a unique perspective that extends beyond what our naked eyes can perceive. This ability to see the invisible heat signatures makes thermal imaging invaluable across a multitude of industries and applications.

The Lepton FLIR camera is a compact and versatile thermal imaging solution that brings professional-grade thermal imaging capabilities to a broad range of consumer applications. The Lepton camera integrates an advanced microbolometer sensor that captures infrared radiation with remarkable precision and allows us to visualise the invisible.

Thermal demonstrates the capabilities of the [FLIR Lepton](https://www.flir.co.uk/products/lepton/) when connected to a low cost [Raspberry PI](https://www.raspberrypi.org) single board computer utilising the [pylepton library](https://github.com/groupgets/pylepton) to control the camera via [Python](https://www.python.org)

## How is the image generated?

The microbolometer sensor consists of an array of 80x60 tiny thermal detectors. These detectors can sense the infrared radiation emitted by objects in the form of heat which translates to a "pixel" value. Each "pixel" measures the temperature of the corresponding portion of the scene being captured. The temperature readings are converted into electrical signals proportional to the detected heat energy.
After some internal signal processing to amplifying, filter, and digitize the signal, algorithms reconstruct the "pixels" into a thermal image. 

Since thermal imaging captures temperature differences rather than colors, a color mapping scheme is applied to the thermal image to enhance its interpretability. This involves assigning different colors or color gradients to different temperature ranges, creating a [pseudo-color representation of the thermal data](https://www.flir.co.uk/discover/industrial/picking-a-thermal-color-palette/). The color mapping allows users to easily distinguish and analyze temperature variations within the scene. In this example we use the "White Hot" colour palette. 

![sample image](/output.png)

## What does the code do?

The simplest example to get started is `example_lepton_capture.py`. This opens the camera, takes a reading and then saves it as a file. The overview below describes what is happening.

We utlise the pylepton library so need to import it at the start.

    from pylepton import Lepton

`capture()` calls a read of the sensor which returns a tuple that includes an array of sensor values from and a unique frame ID. Lepton frames can update at ~27 Hz, but only unique ones are returned at ~9 Hz.


    with Lepton() as l:
      a,_ = l.capture()

We us a function from the computer vision library cv2 to normalise the range of values between the maximum and minumum values in the sensor array. This improves the contrast of the image since the coldest sensor value is set to black and the warmest set to white. This is also why the image looks more "grainy" when there is no one in the scene since the temperature variation in small.


    cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) 

Image data from `capture()` is 12-bit, in this next step we convert it to 8 bits and then write it to a file to save as an image.

    np.right_shift(a, 8, a) # fit data into 8 bits
    cv2.imwrite("output.jpg", np.uint8(a)) # write it!

## In this repository

- `exhibition_lepton.py` - code used in Testing Ground exhibtion at UCL East
- `example_xxx.py` - example code to test cameras
- `testing` folder - random examples 
