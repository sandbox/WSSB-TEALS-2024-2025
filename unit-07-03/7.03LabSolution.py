class Time(object):
  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second

  def __str__(self):
    return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

  def __add__(self, other):
    second = self.second + other.second
    carry_minute = 1 if second >= 60 else 0
    minute = self.minute + other.minute + carry_minute
    carry_hour = 1 if minute >= 60 else 0
    hour = self.hour + other.hour + carry_hour
    return Time(hour, minute, second)

time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)

print(time1)
print(time2)
print(time1 + time2)


class Kangaroo:
  def __init__(self):
    self.pouch_contents = []

  def put_in_pouch(self, item):
    self.pouch_contents.append(item)

  def __str__(self):
    ret = "Kangaroo:\n"
    for item in self.pouch_contents:
      ret += str(item)
      ret += "\n"
    return ret

k = Kangaroo()
k.put_in_pouch(1)
k.put_in_pouch("two")
k.put_in_pouch(3)
k.put_in_pouch(43)
print(k)
