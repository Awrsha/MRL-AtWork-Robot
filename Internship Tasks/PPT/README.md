# Precision Placement Tables (PPT)

## Challenges
- Dealing with similar cavity shapes but different sizes.
- Integration with Realsense sensors.
- Fusion of Depth and RGB data.

## Algorithm Sequence Order
1. Configure color filters only.
2. Add post-processing techniques.
3. Align depth and color images.
4. Calculate weight on Regions of Interest (ROIs).

## Accomplishments
- Created a dataset of images of cavities classified into 10 classes.
- Preprocessed the dataset by performing operations like resizing, normalization, and data augmentation.
- Split the dataset into training and testing sets.
- Utilized TensorFlow's deep learning models like Convolutional Neural Networks (CNNs) or Transfer Learning models such as ResNet, Inception, or VGG to train on the dataset.
- Evaluated the models' performance by predicting labels for the test set and computing accuracy, precision, recall, F1 scores, and confusion matrix.
- Fine-tuned the model by adjusting hyperparameters like learning rate, batch size, number of epochs, optimizer, and regularization.
- Utilized OpenCV to load and preprocess new images, and then passed them to the trained model for classification.

## Result Analysis

### Bounding Box Detector (v.1): /bbox_classification/boundingBox_detector_ros.py

| Model | Example | 16-04-2023_17-59-15.h5 | classification_VGG16.h5 | EfficientNetV2B0_v1.h5 | EfficientNetV2B0_v2.h5 | MobileNetV2_v2.h5 | Pretrained_EfficientNetB0.h5 | VGG16_v1.h5 | VGG16_v2.h5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **F20_20_horizontal**| ![F20_20_horizontal](../dataset/PPT/cavity_images_100perCavity/F20_20_horizontal/F20_20_h_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |
| **M20_30_horizontal**| ![M20_30_horizontal](../dataset/PPT/cavity_images_100perCavity/M20_30_horizontal/M20_h_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |
| **M20_30_vertical**| ![M20_30_vertical](../dataset/PPT/cavity_images_100perCavity/M20_30_vertical/M20_M30_v_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |
| **M20_100_horizontal**| ![M20_100_horizontal](../dataset/PPT/cavity_images_100perCavity/M20_100_horizontal/M20_100_h_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |
| **R20_horizontal**| ![R20_horizontal](../dataset/PPT/cavity_images_100perCavity/R20_horizontal/R20_h_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |
| **R20_vertical**| ![R20_vertical](../dataset/PPT/cavity_images_100perCavity/R20_vertical/R20_v_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |
| **S40_40_horizontal**| ![S40_40_horizontal](../dataset/PPT/cavity_images_100perCavity/S40_40_horizontal/S40_40_h_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |
| **S40_40_vertical**| ![S40_40_vertical](../dataset/PPT/cavity_images_100perCavity/S40_40_vertical/S40_40_v_001.jpg) | NA | NA | NA | NA | NA | NA | NA | NA |

---

To run the boundingBox_detector_ros.py script:
```bash
python3 boundingBox_detector_ros.py -i ../../dataset/PPT/BAG/183847/20230315_183847.bag -m models/MobileNetV2_v2.h5
```

### Results Analysis
- **Model Performance Evaluation**: The table provides an overview of the performance of various models tested on different cavity images.
- **Visual Inspection**: Example images are provided for each cavity type to visually inspect the performance of the models.
