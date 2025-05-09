TITLE
RBFN-CSMP: High Resolution Image Reconstruction using Radial Basis Function Networks and Compressed Sensing Matching Pursuit Algorithms


INTRODUCTION
This project implements a deep learning-based compressed sensing framework for high-resolution image reconstruction, particularly useful in biomedical imaging. 
It introduces the RBFN-CSMP method, which combines Radial Basis Function Networks (RBFNs) and Compressed Sensing Matching Pursuit (CSMP) for efficient, accurate, and fast image reconstruction from compressed measurements.

DESCRIPTIONS
The proposed model integrates a comprehensive deep learning-based pipeline that begins with multilayer subsampling of input images to reduce dimensionality while preserving critical features. 
It then reconstructs high-resolution representations using a trained deep learning network. 
Classification is performed using Radial Basis Function Networks (RBFNs), which effectively capture non-linear relationships in the data. 
To ensure efficient sparse signal representation, the Compressed Sensing Matching Pursuit (CSMP) algorithm is employed for optimization. 
This framework is tailored for diverse image types, including retinal images, chest X-rays, and brain MRI scans, and demonstrates superior performance in terms of PSNR, F1-score, and execution time when compared to conventional reconstruction techniques such as ReconNet and ISTA-Net.


DATASET
The project utilizes a combined dataset comprising images from the DRIVE and STARE retinal datasets, the Chest X-ray dataset, and the IXI brain MRI dataset. 
All images are resized to a uniform 128×128×3 RGB format and undergo preprocessing steps such as normalization and data augmentation. 
Augmentation techniques include rotation, flipping, and Contrast-Limited Adaptive Histogram Equalization (CLAHE) to enhance feature diversity and improve model generalization.


CODE INFORMATION
The project is organized into modular Python scripts, each serving a specific role in the reconstruction pipeline:
data_preprocessing.py: Handles normalization, image resizing to 128×128, vectorization into flattened blocks, and dataset splitting.
rbfn_model.py: Defines the architecture and forward pass of the Radial Basis Function Network (RBFN) for classification.
csmp.py: Implements the Compressed Sensing Matching Pursuit (CSMP) algorithm for sparse reconstruction optimization.
train.py: Contains the training loop, optimizer settings, loss functions, and PSNR tracking during model learning.
evaluate.py: Calculates evaluation metrics such as accuracy, precision, recall, F1-score, and PSNR on test data.
utils/: A directory containing helper functions for performance plotting, data loaders, and metric computation.


REQUIREMENTS
Python 3.8+
NumPy
OpenCV
PyTorch
Matplotlib
Scikit-learn
tqdm


CITATIONS
https://www.kaggle.com/datasets/andrewmvd/drive-digital-retinal-images-for-vessel-extraction
https://www.kaggle.com/datasets/vidheeshnacode/stare-dataset
Mooney, P.: Chest X-ray image dataset. https://www.kaggle.com/ paultimothymooney/chest-xray-pneumonia/







