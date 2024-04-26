import numpy as np

current_position = np.array([x1, y1])
target_position = np.array([x2, y2])
displacement_vector = target_position - current_position


heading_angle_rad = np.radians(heading_angle)
heading_vector = np.array([np.cos(heading_angle_rad), np.sin(heading_angle_rad)])


tangential_component = np.dot(displacement_vector, heading_vector) * heading_vector


normal_vector = np.array([-heading_vector[1], heading_vector[0]])
normal_component = np.dot(displacement_vector, normal_vector) * normal_vector

tangential_acceleration = tangential_component / some_time_interval
normal_acceleration = normal_component / some_time_interval
