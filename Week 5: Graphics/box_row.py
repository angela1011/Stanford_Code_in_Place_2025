from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_BOXES):
        canvas.create_rectangle(i*80, 120, i*80+80, 200,"white","black")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
