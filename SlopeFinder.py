import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import fire

def calculate_length(points):
    """Calculates the Euclidean distance between two points."""
    return np.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)

def draw_line_on_image(image_path, x_length : int = 0, y_length : int = 0):
    """Draws lines between points clicked by the user on an image, computes slope or length based on the line sequence."""
    image = plt.imread(image_path)
    fig, ax = plt.subplots()
    ax.imshow(image)

    # Collect the first two clicks for the first line
    first_two_points = plt.ginput(2, timeout=-1)  
    first_two_points = np.array(first_two_points)
    dx = first_two_points[1][0] - first_two_points[0][0]
    dy = first_two_points[1][1] - first_two_points[0][1]
    slope = -dy / dx if dx != 0 else float('inf')  # Avoid division by zero
    ax.plot(first_two_points[:, 0], first_two_points[:, 1], 'ro-')
    ax.text(np.mean(first_two_points[:, 0]), np.mean(first_two_points[:, 1]),
            f'Slope: {slope:.2f}', fontsize=12, color='black',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='square,pad=0.3'))

    # Collect the third click for the second line
    third_fourth_points = plt.ginput(2, timeout=-1) 
    third_fourth_points = np.array(third_fourth_points)
    second_line = np.vstack([third_fourth_points[0], third_fourth_points[1]])
    length_second_line = calculate_length(second_line)
    ax.plot(second_line[:, 0], second_line[:, 1], 'go-')
    ax.text(np.mean(second_line[:, 0]), np.mean(second_line[:, 1]),
            f'Length: {length_second_line:.2f}px', fontsize=12, color='black',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='square,pad=0.3'))

    # Collect the fourth click for the third line
    fifth_point = plt.ginput(1, timeout=-1)

    # change the y of the fifth point to the y of the fourth point
    fifth_point = list(fifth_point[0])
    fifth_point[1] = third_fourth_points[1][1]

    if len(fifth_point) < 1:
        print("Not enough points clicked.")
        plt.show()
        return
    fifth_point = np.array(fifth_point)
    third_line = np.vstack([third_fourth_points[1], fifth_point])
    length_third_line = calculate_length(third_line)
    ax.plot(third_line[:, 0], third_line[:, 1], 'bo-')
    ax.text(np.mean(third_line[:, 0]), np.mean(third_line[:, 1]),
            f'Length: {length_third_line:.2f}px', fontsize=12, color='black',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='square,pad=0.3'))
    
    # Draw a small square at the fifth point
    square_side = 6  # Define the side length of the square
    square = patches.Rectangle((third_fourth_points[1][0], third_fourth_points[1][1]), square_side, -square_side,
                            linewidth=6, edgecolor='red', facecolor='none')
    ax.add_patch(square)
    
    # print text to top left of the image:
    plot_height=length_second_line
    plot_width=length_third_line

    plot_y=y_length
    plot_x=x_length

    x_ratio=plot_width/plot_x
    y_ratio=plot_height/plot_y

    true_slope = x_ratio * slope / y_ratio

    # print the coords of the first click
    x_distance = -(np.mean(second_line[:, 0]) - first_two_points[0][0])/x_ratio
    y_distance = (np.mean(third_line[:, 1]) - first_two_points[0][1])/y_ratio
    ax.text(first_two_points[0][0], first_two_points[0][1]-10, f'({x_distance:.2f}, {y_distance:.2f})', fontsize=12, color='black',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='square,pad=0.3'))

    # print the coords of the second click
    x_distance = -(np.mean(second_line[:, 0]) - first_two_points[1][0])/x_ratio
    y_distance = (np.mean(third_line[:, 1]) - first_two_points[1][1])/y_ratio
    ax.text(first_two_points[1][0], first_two_points[1][1]+10, f'({x_distance:.2f}, {y_distance:.2f})', fontsize=12, color='black',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='square,pad=0.3'))

    # print the true slope
    x_distance = -(np.mean(second_line[:, 0]) - np.mean([first_two_points[0][0], first_two_points[1][0]]))/x_ratio
    y_distance = (np.mean(third_line[:, 1]) - np.mean([first_two_points[0][1], first_two_points[1][1]]))/y_ratio
    y_intercept = y_distance - true_slope * x_distance
    x_intercept = x_distance - (y_distance / true_slope)
    ax.text(0, 0, f'True slope: {true_slope:.2f}\nY-intercept: {y_intercept:.2f}\nX-intercept: {x_intercept:.2f}', fontsize=20, color='black',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='square,pad=0.3'))

    plt.show()

def main(image_path, x_length : int = 0, y_length : int = 0):
    draw_line_on_image(image_path, x_length, y_length)

if __name__ == '__main__':
    fire.Fire(main)
