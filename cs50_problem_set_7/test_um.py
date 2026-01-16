from um import count

def test_one():
  assert count("Um, thanks for the album.") == 1
  assert count("Um, thanks, um...") == 2
  assert count("Um?") == 1
  assert count("Um") == 1
  assert count("yummy") == 0