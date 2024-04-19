import numpy as np

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.intersection = False

    def is_intersecting(self, x3, y3, x4, y4):
        x12 = self.x1 - self.x2
        x34 = x3 - x4
        y12 = self.y1 - self.y2
        y34 = y3 - y4
        c = x12 * y34 - y12 * x34

        if abs(c) < 0.01:
            return False
        else:
            a = self.x1 * self.y2 - self.y1 * self.x2
            b = x3 * y4 - y3 * x4
            self.intersection = Vec(
                (a * x34 - b * x12) / c,
                (a * y34 - b * y12) / c
            )
            bbox_max_x = max(self.x1, self.x2)
            bbox_min_x = min(self.x1, self.x2)
            bbox_max_y = max(self.y1, self.y2)
            bbox_min_y = min(self.y1, self.y2)
            if (self.intersection.x >= bbox_min_x and self.intersection.x < bbox_max_x and
                self.intersection.y >= bbox_min_y and self.intersection.y < bbox_max_y):
                return True
            return False

class ProjectionSurface:
    def __init__(self, radius, n_boundaries):
        self.radius = radius
        self.boundaries = []
        angle = -np.pi/2
        x1 = radius * np.cos(angle)
        y1 = radius * np.sin(angle)
        for i in range(n_boundaries):
            angle += np.pi / n_boundaries
            x2 = radius * np.cos(angle)
            y2 = radius * np.sin(angle)
            self.boundaries.append(
                Boundary(x1, y1, x2, y2)
            )
            x1 = x2
            y1 = y2

class Ray:
    def __init__(self, viewer, ray_anchor, projection_surface):
        self.viewer = viewer
        self.ray_anchor = ray_anchor
        self.projection_surface = projection_surface
        self.projected_point = Vec(1, 1)

    def update(self):
        v = Vec(
            (self.ray_anchor.x - self.viewer.x) * 100,
            (self.ray_anchor.y - self.viewer.y) * 100
        )
        for b in self.projection_surface.boundaries:
            if (b.is_intersecting(v.x, v.y, self.ray_anchor.x, self.ray_anchor.y)):
                self.projected_point = b.intersection

    def get_projection_angle(self):
        return (np.arctan(self.projected_point.y / self.projected_point.x) + np.pi/2) / np.pi * 180