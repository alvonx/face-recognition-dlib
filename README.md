# face-recognition-dlib
Here we will learn to use "dlib" library to train as well as recognize the face

- install dlib
  - windows
    - must have python 3.6
    - visit [here](https://pypi.org/simple/dlib) to get the link of dlib which suits your system
    - ![pypi](https://github.com/alvon-X/helpful-assets/blob/main/face-recognition-dlib%20readme-assets/pypi-link.jpg) 
    - right click on the link highlighted in green and copy link address
    - activate your python virtual environment
    - run the command `python -m pip install <pypi-link>` where **pypi-link** is the link address you copied

- running the code
  - add your picture (only one needed) in the id folder and name it as **your-name_id**
    - example: in my case **deepak_1**
    - if you want to train more than one the copy their photo in id folder and name them as following example:
      1. name_1
      2. name_2
      3. name_3
      4. and so on...
  - when you copied the photos in id folder just run the following command to **TRAIN(encode)** with the photos
    - ```python
      python encoding.py
      ```
    - this will create a **encodings.pickle** file which contains the 128-facial features
    - human can't read that pickle file
  - the last step i.e. **DETECTION** run the command given below in your terminal
    - ```python
      python detect.py
      ```

- thats it for the begineer level 