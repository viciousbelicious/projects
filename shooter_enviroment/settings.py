import math

##game settings
res = width, height = 1300, 700
half_width = width // 2
half_height = height // 2
fps = 0

player_pos = 1.5, 5 ##on minimap
player_angle = 0
player_speed = 0.004
player_rot_speed = 0.002
player_size_scale = 60

#mouse controls settings 00:22:56
mouse_sensitivity = 0.0003
mouse_max_rel = 40
mouse_border_left = 100
mouse_border_right = width - mouse_border_left


##raycasting settings
##per calcolare la distanza dal walls
##calcoliamo i delta angle e li sommiamo
##il delta angle sono il lato mancante del rettangolo che si forma con le intersezioni
##con la griglia del suolo (orizzontale e verticale)  o_|_|_|_|
##                                                     _|_|_|_|_
##                                                      | | | |_|
fov = math.pi / 3
half_fov = fov / 2
num_rays = width // 2
half_num_rays = num_rays // 2
delta_angle = fov / num_rays
max_depth = 20

screen_dist = half_width / math.tan(half_fov)
scale = width // num_rays

texture_size = 256
half_texture_size = texture_size // 2