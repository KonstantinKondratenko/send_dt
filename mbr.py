rect = cv2.minAreaRect(cnt)
(x, y), (w, h), angle = rect

if angle < -45:
    angle += 90
else:
    angle -= 90

rotation_matrix = cv2.getRotationMatrix2D((x, y), angle, 1.0)
height, width = img.shape[:2]
cos_angle = np.abs(rotation_matrix[0, 0])
sin_angle = np.abs(rotation_matrix[0, 1])
new_width = int(height * sin_angle + width * cos_angle)
new_height = int(height * cos_angle + width * sin_angle)
rotation_matrix[0, 2] += (new_width / 2) - x
rotation_matrix[1, 2] += (new_height / 2) - y
img = cv2.warpAffine(img, rotation_matrix, (new_width, new_height))

x1 = int(x + w/2)
y1 = int(y - h/2)
x2 = int(x + w/2)
y2 = int(y + h/2)

cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
