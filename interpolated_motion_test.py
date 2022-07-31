from lib import CubicHermiteSpline, CubicBezierCurve
import tkinter as tk, datetime, time


if __name__ == "__main__":
    canvas_width = 600
    canvas_height = 400
    ball_diameter = 50
    ball_radius = ball_diameter / 2
    ball_color = "red"

    start_x = 200
    start_y = 100

    x_distance = canvas_width - 2 * start_x
    y_distance = canvas_height - 2 * start_y
    seconds = 0.3
    fps = 48
    steps = int(seconds * fps)
    spf = 1 / fps
    x_velocity = x_distance / steps
    y_velocity = y_distance / steps

    window = tk.Tk()
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()
    ball = canvas.create_oval(
        start_x - ball_radius, start_y - ball_radius,
        start_x + ball_radius, start_y + ball_radius,
        fill=ball_color
        )
    direction_var = tk.IntVar(window, 1)
    execute_button = tk.Button(window, text="Push")
    execute_button.pack()

    Curve = CubicHermiteSpline
    x_curve = Curve.new(-3.0, -3.0)
    y_curve = Curve.new(0.0, 0.0)
    def execute(*args):
        direction = direction_var.get()
        x_locations = tuple(Curve.explicit_derivative_generator(x_curve, steps))
        y_locations = tuple(Curve.explicit_derivative_generator(y_curve, steps))
        for i in range(steps):
            t = datetime.datetime.now()
            x_shift = direction * x_velocity * y_locations[i]
            y_shift = direction * y_velocity * x_locations[i]
            x1, y1, x2, y2 = canvas.coords(ball)
            canvas.coords(
                ball, x1 + x_shift, y1 + y_shift, x2 + x_shift, y2 + y_shift
                )
            canvas.update()
            t_delta = (datetime.datetime.now() - t).total_seconds()
            time.sleep(spf - t_delta if spf > t_delta else 0)
        direction_var.set(direction * -1)

    execute_button.config(command=execute)

    window.mainloop()
