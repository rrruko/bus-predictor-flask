#  class Polyline:
#    def __init__(self, points):
#      self.points = points
#
#    def closest_segment(self, point):

from collections import namedtuple

NearestPoint = namedtuple('NearestPoint', 'point t')

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, point):
    return Point(self.x + point.x, self.y + point.y)

  def __sub__(self, point):
    return Point(self.x - point.x, self.y - point.y)

  def dot(self, point):
    return self.x * point.x + self.y * point.y

  def scale(self, c):
    return Point(self.x * c, self.y * c)

  def distance_to(self, point):
    dx = self.x - point.x
    dy = self.y - point.y
    return (dx * dx + dy * dy) ** 0.5

class Segment:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def nearest_point(self, point):
    v = self.end - self.start
    u = self.start - point
    t = - (v.dot(u) / v.dot(v))
    return NearestPoint(point = self.start + v.scale(t), t = t)

  def distance_to(self, point):
    nearest = self.nearest_point(point)
    return nearest.point.distance_to(point)