# MonReader-App
MonReader simplifies document digitization into an effortless process:

1. Page Detection: Utilizes a low-res camera preview to detect when a page is turned.
2. High-Res Capture: Automatically captures a high-res photo post-flip.
3. Corner Recognition & Cropping: Identifies document corners for precise cropping.
4. Dewarping: Adjusts the cropped image to a bird's-eye view for clarity.
5. Contrast Enhancement: Sharpens text-background contrast for better readability.
6. Text Recognition: Maintains formatting while recognizing text, with ML-powered corrections for unparalleled accuracy.

The aim of the current project is build a CNN model to implement a reliable Page Detection system

## Model Performance

The model showcases an outstanding precision of **99.5%** at detecting when a page is being turned by looking at only one frame, hence its reliability over multiple frames becomes virtually perfect. Additionally, the model is interpreted via visualizing its feature map.

![Alt text](/Pictures/flip_feature_map.png?raw=true)
![Alt text](/Pictures/not_flip_feature_map.png?raw=true)

It is clear that the model is able to distinguish elements such as hands and books from other non relevant source of noise.
