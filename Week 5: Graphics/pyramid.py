from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels
BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base
# CANVAS_WIDTH = BRICK_WIDTH*BRICKS_IN_BASE
# left_x = 0
# left_x_1LAYER = BRICK_WIDTH/2
# left_x_2LAYER = BRICK_WIDTH
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    total_layers = 14
    for layer in range(total_layers):
        bricks_in_layer = total_layers - layer
        total_layer_width = bricks_in_layer * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - total_layer_width) // 2
        y_top = CANVAS_HEIGHT - BRICK_HEIGHT * (layer + 1)
        
        for i in range(bricks_in_layer):
            x = start_x + i * BRICK_WIDTH
            draw_brick(canvas, x, y_top)

def draw_brick(canvas, left_x, top_y):
    right_x = left_x + BRICK_WIDTH
    bottom_y = top_y + BRICK_HEIGHT
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "yellow", "black")

# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     for i in range(14):
#         draw_BRICK_BASE(canvas, 0 + BRICK_WIDTH*i, 0)
#     for i in range(13):
#         draw_BRICK_1LAYER(canvas, left_x_1LAYER + BRICK_WIDTH*i, 0)
#     for i in range(12):
#         draw_BRICK_2LAYER(canvas, left_x_2LAYER + BRICK_WIDTH*i, 0)
    
# def draw_BRICK_BASE(canvas, left_x, top_y):
#     top_y=CANVAS_HEIGHT-BRICK_HEIGHT
#     bottom_y=BRICK_HEIGHT+top_y
#     right_x = BRICK_WIDTH+left_x
#     canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "yellow", "black")

# def draw_BRICK_1LAYER(canvas, left_x_1LAYER, top_y_1LAYER):
#     top_y_1LAYER = CANVAS_HEIGHT - BRICK_HEIGHT*2
#     bottom_y_1LAYER = BRICK_HEIGHT + top_y_1LAYER
#     right_x_1LAYER = BRICK_WIDTH + left_x_1LAYER
#     canvas.create_rectangle(left_x_1LAYER, top_y_1LAYER, right_x_1LAYER, bottom_y_1LAYER, "yellow", "black")

# def draw_BRICK_2LAYER(canvas, left_x_2LAYER, top_y_2LAYER):
#     top_y_2LAYER = CANVAS_HEIGHT - BRICK_HEIGHT*3
#     bottom_y_2LAYER = BRICK_HEIGHT + top_y_2LAYER
#     right_x_2LAYER = BRICK_WIDTH + left_x_2LAYER
#     canvas.create_rectangle(left_x_2LAYER, top_y_2LAYER, right_x_2LAYER, bottom_y_2LAYER, "yellow", "black")

if __name__ == '__main__':
    main()
