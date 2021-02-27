from ml.predict import SmartBinPredictor
import os
import cv2


def main():
    predictor = SmartBinPredictor('models/model1.pt')
    path = '/home/traceur/Insync/shared/Hack4future/data/test/'
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.jpg'):
                continue

            image = os.path.join(root, file)
            prediction = predictor.predict(cv2.imread(image))
            print(root)
            print(prediction)


if __name__ == '__main__':
    main()
