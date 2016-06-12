from abc import ABCMeta

class Veggie(metaclass=ABCMeta):
  pass

class Garlic(Veggie):
  def __init__(self):
    return "にんにく"
  
class Onion(Veggie):
  def __init__(self):
    return "たまねぎ"
  
class Mushroom(Veggie):
  def __init__(self):
    return "マッシュルーム "
  
class RedPepper(Veggie):
  def __init__(self):
    return "赤トウガラシ"
  
class GreenPepper(Veggie):
  def __init__(self):
    return "ピーマン"