def solution(h1, m1, s1, h2, m2, s2):
    def overlaps(h, m, s):
        angle_h = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360
        angle_m = (m * 6 + s * 0.1) % 360
        angle_s = (s * 6) % 360

        answer = (h * 60 + m) * 2 - h + (angle_s >= angle_m) + (angle_s >= angle_h)
        if h >= 12:
            answer -= 2

        return answer

    answer = overlaps(h2, m2, s2) - overlaps(h1, m1, s1)
    if h1 in (0, 12) and not m1 and not s1:
        answer += 1

    return answer
