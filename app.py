import pywebio
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio.platform.tornado_http import start_server

def bmi():
    put_markdown('''# BMI Calculator''')
    put_markdown('made with ❤️ by [om pramod](https://www.linkedin.com/in/omkar-h-7944a4202)')
    put_text(" ")
    put_markdown("""[Body mass index](https://en.wikipedia.org/wiki/Body_mass_index) (BMI) is a measure of body fat based on height and weight that applies to adult men and women.""")
    
    put_table([["Severely underweight" , "BMI<14.9" ],
    ["Underweight","14.9≤BMI<18.4 "],
    ["Normal","18.4≤BMI<22.9"],
    ["Overweight","22.9≤BMI<27.5"],
    ["Moderately obese","27.5≤BMI<40"],
    ["Severely obese","BMI≥40 "]],header=["Category","BMI"])

    info = input_group('BMI calculation', [
    input("Your Height(cm)", name="height", type=FLOAT,required=True),
    input("Your Weight(kg)", name="weight", type=FLOAT,required=True)])

    BMI = info['weight'] / (info['height'] / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    put_info("Your BMI is :",BMI)

    if(BMI>0):
            if BMI <= 18.4:
                put_error("You are underweight.")
            elif BMI <= 24.9:
                put_error("You are healthy.")
            elif BMI <= 29.9:
                put_error("You are over weight.")
            elif BMI <= 34.9:
                put_error("You are severely over weight.")
            elif BMI <= 39.9:
                put_error("You are obese.")
            else:
                put_error("You are severely obese.")
    else:
        put_warning("enter valid details")
        
def short():
    try:
        bmi()
    except TypeError:
        put_warning("enter valid details") 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(short, port=args.port)
