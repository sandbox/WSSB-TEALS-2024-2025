def make_me_cookie():
  return 'cookie'

# Did anything happen when this assert "passed"?
print("Trying the first: assert make_me_cookie() == 'cookie'")
assert make_me_cookie() == 'cookie'

# Did anything happen when this assert "passed"?
print("Trying the second: assert make_me_cookie() != 'dough'")
assert make_me_cookie() != 'dough'

# Did anything happen when the assert "failed"? What did you see?
print("Trying the third: assert make_me_cookie() != 'cookie'")
assert make_me_cookie() != 'cookie'
