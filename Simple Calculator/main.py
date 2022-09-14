from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

# LINK TO CONNECT WITH KV FILE
Builder.load_file('calculator.kv')

# DEFAULT WINDOWS SIZE
Window.size = (300, 500)


class MyLayout(Widget):
    def clear(self):
        self.ids.current_operand.text = ""
        self.ids.previous_operand.text = ""

    def delete(self):
        current_value = self.ids.current_operand.text[:-1]
        self.ids.current_operand.text = current_value

    def square(self):
        try:
            number = float(self.ids.current_operand.text)
            answer = number ** 2
            self.ids.previous_operand.text = f'Square({str(number)})'
            self.ids.current_operand.text = str(answer)
        except:
            self.ids.previous_operand.text = ""
            self.ids.current_operand.text = "Maths Error!!!"

    def plus_minus(self):
        try:
            previous_number = float(self.ids.current_operand.text)
            new_number = -1 * previous_number
            self.ids.current_operand.text = str(new_number)
        except:
            self.ids.previous_operand.text = ""
            self.ids.current_operand.text = "Maths Error!!!"

    def divide(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "/"

    def multiplication(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "*"

    def addition(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "+"

    def subtraction(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "-"

    def equals(self):
        try:
            self.ids.previous_operand.text = self.ids.current_operand.text + " = "
            equation = self.ids.current_operand.text
            answer = eval(equation)
            self.ids.current_operand.text = str(answer)
        except:
            self.ids.previous_operand.text = ""
            self.ids.current_operand.text = "Maths Error!!!"

    def decimal(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "."

    def zero(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "0"

    def one(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "1"

    def two(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "2"

    def three(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "3"

    def four(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "4"

    def five(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "5"

    def six(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "6"

    def seven(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "7"

    def eight(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "8"

    def nine(self):
        self.ids.current_operand.text = self.ids.current_operand.text + "9"


class SimpleCalculator(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    SimpleCalculator().run()
