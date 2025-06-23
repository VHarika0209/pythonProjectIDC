from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class TempConverter(BoxLayout):
    result = StringProperty("")

    def convert_temp(self, temp_input, convert_to):
        try:
            temp = float(temp_input)
            if convert_to == "to_fahrenheit":
                converted = (temp * 9/5) + 32
                self.result = f"{converted:.2f} °F"
            elif convert_to == "to_celsius":
                converted = (temp - 32) * 5/9
                self.result = f"{converted:.2f} °C"
            else:
                self.result = "Invalid conversion"
        except ValueError:
            self.result = "Please enter a valid number"

class TempConverterApp(App):
    def build(self):
        return TempConverter()

if __name__ == "__main__":
    TempConverterApp().run()

