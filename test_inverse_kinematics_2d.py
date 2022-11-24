from lib import vec2d, mat2d, mat2dt, \
    TkCircle, TkLine, \
    Scene, Component, VertexBody
import tkinter as tk, math, json


if __name__ == "__main__":
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 400
    canvas_invert = mat2dt.reflection(False, True)
    canvas_shift = mat2dt.translation(CANVAS_WIDTH / 2, CANVAS_HEIGHT - 50)
    canvas_basis = mat2dt.compile(canvas_shift, canvas_invert)

    window = tk.Tk()
    canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    rotation_speed = 1
    fps = 24
    frames = fps * rotation_speed
    rotate = mat2dt.rotation(2 * math.pi / frames)
    delay = int(1000 * 1/fps)

    origin = vec2d.new(0, 0)
    vector = vec2d.new(0, 100)

    link1 = Component(
        vec2d.zero_vector(),
        mat2dt.identity_matrix(),
        [VertexBody(vec2d.zero_vector(), mat2dt.identity_matrix(), [vector])],
        []
        )
    scene = Scene(vec2d.zero_vector(), mat2dt.identity_matrix(), [link1])

    circle = TkCircle(canvas, vec2d.zero_vector(), 12, fill="red")
    line = TkLine(canvas, circle.origin_reference(), vector, fill="blue")
    end = TkCircle(canvas, vec2d.zero_vector(), 8, fill="", outline="blue")

    line.draw()
    end.draw()
    circle.draw()

    def rotate_line():
        mat2dt.itransform_vector(rotate, vector)
        (*mat2dt.transform_into_vectors(
            canvas_shift,
            [vector, origin],
            [end.origin_reference(), circle.origin_reference()]
            ),)
        circle.update()
        end.update()
        line.update()
        window.after(delay, rotate_line)

    window.after(delay, rotate_line)
    # window.mainloop()
