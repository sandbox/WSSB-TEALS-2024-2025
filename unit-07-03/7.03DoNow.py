class Time(object):
  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second

time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)

print(time1)
print(time2)
