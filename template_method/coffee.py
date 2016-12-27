'''
Created on 2016/12/27

@author: yu-suke
'''
from template_method.caffeine_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    '''
    Coffee class
    '''

    def brew(self):
        print("brew a cup of coffee")

    def add_condiments(self):
        print("add sugar and milk")

    def customer_wants_condiments(self):
        answer = self.get_user_input()

        if(answer.lower()[0] == "y"):
            return True
        else:
            return False

    def get_user_input(self):
        answer = None

        print("Do you put milk and sugar in your coffee?")

        answer = input()
        if(answer is None or answer == ""):
            return "no"
        return answer


if __name__ == "__main__":
    coffee = Coffee()
    coffee.prepare_recipe()
