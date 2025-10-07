class LinkedList:
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color


cookie_one=LinkedList("Green")
cookie_two=LinkedList("Blue")
print(cookie_one.get_color())
print(cookie_two.get_color())
cookie_one.set_color("yellow")
print(cookie_one.get_color())
print(cookie_two.get_color())
