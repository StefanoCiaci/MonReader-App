# MonReader-App: Revolutionizing Document Digitization
MonReader-App transforms the task of document digitization into a seamless, effortless process. The innovative harnesses the power of cutting-edge technology to deliver a comprehensive suite of features designed to optimize every aspect of document digitization.

## Core Features:
- Page Detection: Leveraging the capabilities of a low-resolution camera preview, MonReader expertly detects page turns, ensuring a smooth digitization process from start to finish.

- High-Resolution Capture: Immediately after a page is turned, our system automatically captures a high-resolution photo, preserving every detail with crystal-clear quality.

- Corner Recognition & Cropping: With advanced corner recognition algorithms, MonReader accurately identifies the corners of each document, enabling precise cropping and ensuring that only the relevant parts of the document are digitized.

- Image Dewarping: Our sophisticated dewarping technology adjusts the cropped image to a bird's-eye view, eliminating any distortions and presenting the document in its true form.

- Contrast Enhancement: We enhance the contrast between text and background, sharpening the text to improve readability and ensuring that every word is crystal clear.

- Text Recognition: Our system not only recognizes text but also maintains the original formatting, thanks to our machine learning-powered corrections. This results in unparalleled accuracy and readability of the digitized documents.

## Project Objective:
The primary goal of this project is to develop a Convolutional Neural Network (CNN) model that implements a highly reliable Page Detection system. This system is crucial for automating the initial step of the digitization process, ensuring efficiency and accuracy from the outset.

## Model Performance Highlights:
- Exceptional Precision: Our model demonstrates a remarkable precision rate of **99.5%** in detecting page turns based on a single frame analysis. This indicates almost perfect reliability when analyzing multiple frames, showcasing the model's ability to effectively distinguish between relevant elements (such as hands and books) and irrelevant background noise.

- Insightful Interpretation: By visualizing the feature map, we gain valuable insights into the model's operational mechanics. This visualization reveals how the model differentiates between essential elements and background distractions, further affirming its efficiency and reliability.

![Alt text](/Pictures/flip_feature_map.png?raw=true)
![Alt text](/Pictures/not_flip_feature_map.png?raw=true)
