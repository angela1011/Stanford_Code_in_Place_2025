from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!
    polygon = canvas.create_polygon(
   10, 10, 20, 20, 10, 20,
   color="red",
)
    

if __name__ == '__main__':
    main()