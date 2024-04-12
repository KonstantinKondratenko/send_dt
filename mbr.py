rect = cv2.minAreaRect(cnt)
(x, y), (w, h), angle = rect

pt1 = (x - w/2*np.cos(angle*np.pi/180) - h/2*np.sin(angle*np.pi/180),
       y - w/2*np.sin(angle*np.pi/180) + h/2*np.cos(angle*np.pi/180))
pt2 = (x + w/2*np.cos(angle*np.pi/180) - h/2*np.sin(angle*np.pi/180),
       y + w/2*np.sin(angle*np.pi/180) + h/2*np.cos(angle*np.pi/180))

if pt1[0] != pt2[0]:
    k = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
    b = pt1[1] - k * pt1[0]
else:
    k = np.inf
    b = pt1[0]

x1 = int(pt1[0])
y1 = int(pt1[1])
x2 = int(pt2[0])
y2 = int(pt2[1])

cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
