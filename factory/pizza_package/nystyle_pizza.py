from factory.pizza_package.pizza import Pizza

class NYStyleCheesePizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self.name = "ニューヨークスタイルのソース&チーズピザ"
    self.dough = "薄いクラフト生地"
    self.sauce = "マリナラソース"
    
    self.toppings.append("粉レッジャーノチーズ")