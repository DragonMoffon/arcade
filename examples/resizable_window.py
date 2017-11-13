"""
Example showing how handle screen resizing.
"""
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
START = 0
END = 2000
STEP = 50


class MyApplication(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height, title="Resizing Window Example", resizable=True)

        arcade.set_background_color(arcade.color.WHITE)

    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        print(f"Window resized to: {width}, {height}")

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()

        # Draw the y labels
        i = 0
        for y in range(START, END, STEP):
            arcade.draw_point(0, y, arcade.color.BLUE, 5)
            arcade.draw_text(f"{y}", 5, y, arcade.color.BLACK, 12, anchor_x="left", anchor_y="bottom")
            i += 1

        # Draw the x labels.
        i = 1
        for x in range(START + STEP, END, STEP):
            arcade.draw_point(x, 0, arcade.color.BLUE, 5)
            arcade.draw_text(f"{x}", x, 5, arcade.color.BLACK, 12, anchor_x="left", anchor_y="bottom")
            i += 1


def main():
    MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
