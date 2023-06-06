
def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    mindist, ans = float("inf"), -1
    for i, (a, b) in enumerate(points):
        if a == x or b == y:
            dist = abs(a - x) + abs(b - y)
            if dist < mindist:
                ans, mindist = i, dist
    return ans