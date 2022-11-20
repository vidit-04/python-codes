def findAngle(hr, mn):
    hr = hr % 12
    h = (hr * 360) // 12 + (mn * 360) // (12 * 60)
    m = (mn * 360) // (60)
    angle = abs(h - m)
    if angle > 180:
        angle = 360 - angle
    return angle
 
hr=int(input('Hour: '))
mn=int(input('Minutes: '))
print(findAngle(hr, mn))        