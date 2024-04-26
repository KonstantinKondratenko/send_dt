import numpy as np

current_position = np.array([x1, y1])
target_position = np.array([x2, y2])
displacement_vector = target_position - current_position
heading_angle_rad = np.radians(heading_angle)
heading_vector = np.array([np.cos(heading_angle_rad), np.sin(heading_angle_rad)])
angle_between_vectors = np.arccos(np.dot(displacement_vector, heading_vector) / (np.linalg.norm(displacement_vector) * np.linalg.norm(heading_vector)))
distance_to_target = np.linalg.norm(displacement_vector)

time_interval = some_time_interval  

tangential_acceleration = (distance_to_target / time_interval ** 2) * np.cos(angle_between_vectors)

angular_acceleration = (angle_between_vectors / time_interval ** 2) * np.sign(np.cross(displacement_vector, heading_vector))
