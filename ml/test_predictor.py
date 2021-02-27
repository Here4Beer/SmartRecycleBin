from ml.predict import SmartBinPredictor
import os


def main():
    predictor = SmartBinPredictor('models/model1.pt')
    path = '/home/traceur/Insync/shared/Hack4future/data/test/'
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.jpg'):
                continue

            image = os.path.join(root, file)
            prediction = predictor.predict(image)
            result = root.split('/')[-1] == predictor.class_names[prediction]
            results.append(result)

            if not result:
                print(image)

    positives = results.count(True)
    negatives = results.count(False)

    print(positives / len(results))


if __name__ == '__main__':
    main()
