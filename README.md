# README for Line Drawing and Measurement Tool

## Description

This Python script is designed to assist in the interactive drawing of lines on an image for the purpose of measuring geometrical properties such as slope and length. Users can manually select points on an image, and the script will calculate and display the slope of the line between the first two selected points and the lengths of subsequent lines formed by additional points. It also includes functionality to transform these measurements into real-world units based on user input for scaling.

## Requirements

    Python 3.x
    Matplotlib
    NumPy
    Fire (for command-line interface)

To ensure all dependencies are installed, run:

```bash
pip install matplotlib numpy fire
```

## Instructions

Starting the Script: Execute the script from the command line. You need to provide the path to the image file and optionally the graph length values corresponding to the axes of your image (for scaling purposes).

Example:

```bash
python SlopeFinder.py --image_path="path/to/image.jpg" --x_length=6 --y_length=100
```

![img](.\img\image.png)

Interacting with the Image:
    Click 1: Click on the image to mark the starting point of the slope line.
    Click 2: Click on the image to mark the ending point of the slope line. The script calculates and displays the slope between these two points.
    Click 3: Click on the image to mark the beginning of the second line, typically the left upper corner of the measurement frame.
    Click 4: Click on the image to mark the lower left corner of the graph, establishing the vertical measurement for scaling.
    Click 5: Click on the image to mark the lower right corner of the graph, establishing the horizontal measurement for scaling.

![img](.\img\image_result.png)

View Results: After the final click, the script calculates and displays:
    The lengths of the second and third lines based on the pixel distances between the points.
    The coordinates of each click in the transformed scale using the real-world dimensions provided.
    A true slope of the first line based on the scaled dimensions.
    Y-intercept and X-intercept of the line based on the true slope and scaled coordinates.

The tool provides a visual representation of each line with calculated values displayed directly on the image. This tool is helpful for analyzing images where precise geometric measurements are needed, such as in engineering, architecture, or data science visualizations.
