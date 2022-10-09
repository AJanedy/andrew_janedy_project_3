# Andrew Janedy

import arcade

# redo text like this
# inside of start render and finish render
# my_text = arcade.Text("sample text", start x, start y, color, font size)
# my_text.draw()

new_window = arcade.open_window(1000, 700, "Andrew Janedy")
arcade.set_background_color(arcade.color.PERIWINKLE)
arcade.start_render()

# dock base
arcade.draw_parabola_filled(0, -100, 1000, 100, arcade.color.GRAY)

# pycharm app
arcade.draw_rectangle_filled(500, 55, 80, 80, arcade.color.BLACK)
arcade.draw_line(469, 25, 515, 25, arcade.color.WHITE, 3)
my_text = arcade.Text("PC", 466, 65, arcade.color.WHITE, 24)
my_text.draw()
arcade.draw_circle_filled(500, 10, 2, arcade.color.LIGHT_GRAY)

# pycharm text
arcade.draw_rectangle_filled(500, 125, 86, 20, arcade.color.SLATE_GRAY)
arcade.draw_triangle_filled(495, 115, 505, 115, 500, 107, arcade.color.SLATE_GRAY)
my_text = arcade.Text("PyCharm", 475, 120, arcade.color.WHITE, 10)
my_text.draw()

# cursor
arcade.draw_triangle_filled(538, 13, 545, 15, 538, 25, arcade.color.WHITE)
arcade.draw_line(541, 15, 543, 11, arcade.color.WHITE, 3)
arcade.draw_triangle_filled(539, 14, 543, 16, 539, 22, arcade.color.BLACK)
arcade.draw_line(541, 15, 542.5, 12, arcade.color.BLACK, 2)

# mail app
arcade.draw_rectangle_filled(410, 50, 68, 68, arcade.color.BLUE)
arcade.draw_rectangle_filled(410, 50, 50, 30, arcade.color.WHITE)
arcade.draw_line(385, 65, 410, 45, arcade.color.GRAY)
arcade.draw_line(410, 45, 435, 65, arcade.color.GRAY)

# safari app
arcade.draw_rectangle_filled(590, 50, 68, 68, arcade.color.WHITE)
arcade.draw_circle_filled(590, 50, 25, arcade.color.BLUE)
arcade.draw_triangle_filled(587, 53, 593, 47, 605, 68, arcade.color.RED)
arcade.draw_triangle_filled(587, 53, 593, 47, 575, 32, arcade.color.WHITE)

# eclipse app
arcade.draw_circle_filled(665, 40, 26, arcade.color.ORANGE_PEEL)
arcade.draw_circle_filled(670, 40, 26, arcade.color.VIOLET)
arcade.draw_line(644, 40, 696, 40, arcade.color.WHITE, 3)
arcade.draw_line(645, 46, 695, 46, arcade.color.WHITE, 3)
arcade.draw_line(644, 34, 695, 34, arcade.color.WHITE, 3)

# app store
arcade.draw_rectangle_filled(730, 35, 35, 35, arcade.color.BLUE)
arcade.draw_line(719, 23, 733, 46, arcade.color.WHITE, 3)
arcade.draw_line(727, 46, 741, 23, arcade.color.WHITE, 3)
arcade.draw_line(717, 28, 743 ,28, arcade.color.WHITE, 3)

# music app
arcade.draw_rectangle_filled(332, 40, 52, 52, arcade.color.RED)
arcade.draw_circle_filled(320, 30, 5, arcade.color.WHITE)
arcade.draw_circle_filled(340, 35, 5, arcade.color.WHITE)
arcade.draw_line(344, 35, 344, 55, arcade.color.WHITE, 2)
arcade.draw_line(324, 30, 324, 50, arcade.color.WHITE, 2)
arcade.draw_line(323, 47, 344, 52, arcade.color.WHITE, 6)

# spotify app
arcade.draw_circle_filled(275, 35, 20, arcade.color.GREEN)
arcade.draw_arc_outline(275, 38, 25, 10, arcade.color.BLACK, 0, 180, 5)
arcade.draw_arc_outline(275, 33, 20, 8, arcade.color.BLACK, 0, 180, 5)
arcade.draw_arc_outline(275, 28, 15, 6, arcade.color.BLACK, 0, 180, 5)

# small apps
# swiss cross
arcade.draw_rectangle_filled(232, 30, 25, 25, arcade.color.ALABAMA_CRIMSON)
arcade.draw_rectangle_filled(232, 30, 20, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(232, 30, 5, 20, arcade.color.GOLD)

# question mark
arcade.draw_circle_filled(195, 30, 14, arcade.color.WHITE)
my_text = arcade.Text("?", 188, 21, arcade.color.BLACK, 18)
my_text.draw()

# APP APP
arcade.draw_rectangle_filled(155, 30, 26, 26, arcade.color.BLUEBERRY)
my_text = arcade.Text("APP", 144, 21, arcade.color.BLACK_OLIVE, 8)
my_text.draw()

# target
arcade.draw_circle_filled(770, 30, 14, arcade.color.RED)
arcade.draw_circle_filled(770, 30, 8, arcade.color.WHITE)
arcade.draw_circle_filled(770, 30, 4, arcade.color.RED)

# terminal
arcade.draw_rectangle_filled(805, 30, 26, 26, arcade.color.SILVER)
arcade.draw_rectangle_filled(805, 30, 23, 23, arcade.color.BLACK)
arcade.draw_rectangle_filled(805, 30, 20, 20, arcade.color.CHARCOAL)
arcade.draw_line(797, 37, 802, 33, arcade.color.WHITE)
arcade.draw_line(802, 33, 797, 29, arcade.color.WHITE)
arcade.draw_line(804, 29, 812, 29, arcade.color.WHITE)

# calculator
arcade.draw_rectangle_filled(840, 30, 26, 26, arcade.color.SILVER)
arcade.draw_rectangle_outline(840, 30, 26, 26, arcade.color.BLACK)
arcade.draw_rectangle_filled(840, 30, 16, 20, arcade.color.BLACK)
arcade.draw_rectangle_filled(840, 36, 12, 4, arcade.color.GRAY)
arcade.draw_circle_filled(836, 31, 2, arcade.color.WHITE)
arcade.draw_circle_filled(840, 31, 2, arcade.color.WHITE)
arcade.draw_circle_filled(844, 31, 2, arcade.color.ORANGE)
arcade.draw_circle_filled(836, 27, 2, arcade.color.WHITE)
arcade.draw_circle_filled(840, 27, 2, arcade.color.WHITE)
arcade.draw_circle_filled(844, 27, 2, arcade.color.ORANGE)
arcade.draw_circle_filled(836, 23, 2, arcade.color.WHITE)
arcade.draw_circle_filled(840, 23, 2, arcade.color.WHITE)
arcade.draw_circle_filled(844, 23, 2, arcade.color.ORANGE)
arcade.draw_rectangle_filled(838, 23, 4, 3, arcade.color.WHITE)

# notes
arcade.draw_rectangle_filled(875, 30, 26, 26, arcade.color.YELLOW)
arcade.draw_line(865, 37, 882, 37, arcade.color.ORANGE_RED, 2)
arcade.draw_line(865, 33, 870, 33, arcade.color.ORANGE_RED, 2)
arcade.draw_line(872, 33, 880, 33, arcade.color.ORANGE_RED, 2)
arcade.draw_line(865, 29, 878, 29, arcade.color.ORANGE_RED, 2)

# trash
arcade.draw_rectangle_filled(910, 27, 26, 19, arcade.color.DARK_SLATE_GRAY)
arcade.draw_ellipse_filled(910, 35, 26, 13, arcade.color.BLACK)

# task bar
arcade.draw_lrtb_rectangle_filled(0, 1000, 700, 680, arcade.color.BLUEBERRY)

# search
arcade.draw_circle_outline(850, 692, 5, arcade.color.WHITE, 2)
arcade.draw_line(853, 689, 856, 686, arcade.color.WHITE, 2)

# battery
arcade.draw_rectangle_outline(828, 690, 14, 8, arcade.color.LIGHT_GRAY, 1)
arcade.draw_rectangle_filled(836, 690, 2, 2, arcade.color.LIGHT_GRAY)
arcade.draw_rectangle_filled(828, 690, 12, 6, arcade.color.WHITE)

# user
arcade.draw_circle_outline(808, 690, 6, arcade.color.WHITE)
arcade.draw_circle_filled(808, 691, 2.5, arcade.color.WHITE)
arcade.draw_ellipse_filled(808, 686, 9, 3, arcade.color.WHITE)

# wifi
arcade.draw_arc_outline(788, 692, 12, 4, arcade.color.WHITE, 0, 180, 4)
arcade.draw_arc_outline(788, 688, 6, 3, arcade.color.WHITE, 0, 180, 4)
arcade.draw_arc_outline(788, 684, 2, 2, arcade.color.WHITE, 0, 180, 4)

#task bar text
arcade.draw_text("TERMINAL    Shell   Edit   View   Window   Help", 45, 685, arcade.color.WHITE, 10)
arcade.draw_text("Tue, Oct 4    7:34 PM", 865, 685, arcade.color.WHITE, 10)

# apple logo
arcade.draw_circle_filled(10, 690, 5, arcade.color.WHITE)
arcade.draw_arc_outline(10, 699, 4, 5, arcade.color.WHITE, -90, 10, 2)
arcade.draw_parabola_filled(8, 682, 12, 3, arcade.color.BLUEBERRY)
arcade.draw_arc_filled(15, 690, 5, 5, arcade.color.BLUEBERRY, -90, 90, 180)
arcade.draw_arc_filled(10, 695, 3, 3, arcade.color.BLUEBERRY, -90, 90, 270)

# top folder
arcade.draw_lrtb_rectangle_filled(50, 150, 600, 525, arcade.color.BABY_BLUE)
arcade.draw_lrtb_rectangle_outline(50, 150, 600, 525, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(50, 150, 605, 600, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(50, 75, 610, 600, arcade.color.BLUE)
arcade.draw_text(" python_projects", 50, 510, arcade.color.BLACK, 10)

# middle folder
arcade.draw_lrtb_rectangle_filled(50, 150, 475, 400, arcade.color.BABY_BLUE)
arcade.draw_lrtb_rectangle_outline(50, 150, 475, 400, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(50, 150, 480, 475, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(50, 75, 485, 475, arcade.color.BLUE)
arcade.draw_text("  sample_packs", 50, 385, arcade.color.BLACK, 10)

#bottom folder
arcade.draw_lrtb_rectangle_filled(50, 150, 350, 275, arcade.color.BABY_BLUE)
arcade.draw_lrtb_rectangle_outline(50, 150, 350, 275, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(50, 150, 355, 350, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(50, 75, 360, 350, arcade.color.BLUE)
arcade.draw_text("  MPC Presets", 50, 260, arcade.color.BLACK, 10)

# terminal window
arcade.draw_lrtb_rectangle_filled(250, 800, 600, 200, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(250, 800, 600, 580, arcade.color.DARK_SLATE_GRAY)
arcade.draw_circle_filled(260, 590, 6, arcade.color.RED)
arcade.draw_circle_filled(275, 590, 6, arcade.color.YELLOW)
arcade.draw_circle_filled(290, 590, 6, arcade.color.GREEN)

# terminal text
arcade.draw_text("andrewjanedy - - zsh - 80x42", 425, 585, arcade.color.LIGHT_GRAY, 10)
arcade.draw_text("Last login: Thu Sep 29 08:25:29 on ttys000", 255, 565, arcade.color.WHITE, 10)
arcade.draw_text("andrewjanedy@Andrews-MacBook ~ % ", 255, 550, arcade.color.WHITE, 10)
arcade.draw_lrtb_rectangle_filled(490, 495, 560, 550, arcade.color.GRAY)



arcade.finish_render()
arcade.run()