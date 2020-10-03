import face_recognition
import time
import glob
import pickle

def encode():
    knownEncodings = []
    knownNames = []
    photos_list = glob.glob("id/*")
    total_images = len(photos_list)
    s = time.time()
    for i in range(total_images):
        st = time.time()
        people_name = (photos_list[i].split("\\")[-1]).split("_")[0]
        people_id = int(((photos_list[i].split("\\")[-1]).split("_")[1]).split(".")[0])
        # Load a sample picture and learn how to recognize it.
        people_image = face_recognition.load_image_file(photos_list[i])
        people_face_encoding = face_recognition.face_encodings(people_image)[0]
        print("People {0} named {1} with id {2} done in {3}".format(i+1,people_name,people_id,str(round(time.time()-st,2))))
        knownEncodings.append(people_face_encoding)
        knownNames.append(people_name)
    print("total time for traning:", str(round(time.time()-s, 2)))
    data = {"encodings": knownEncodings, "names": knownNames}
    path_to_encoding = "encodings.pickle"
    f = open(path_to_encoding, "wb")
    f.write(pickle.dumps(data))
    f.close()

encode()
