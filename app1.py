#Импортируем необходимые библиотеки
import warnings
warnings.filterwarnings("ignore")

import streamlit as st    

# Реализуем интерфейс приложения

# Заголовок приложения
st.title("Sample Application for Demontration Purposes!")

st.markdown("""Welcome to the test page of the Sample Deploy page!
This application does a simple action you choose and returns the result - just to illustrate the deploy in the Streamlit environment. 

To use the application, you need:
1. Enter a number.
2. Enter another number.
3. Select an action between them.
4. Enjoy the result!
""")

# Вводим строку для ввода 1 числа
num1 = st.slider('Please, enter a number:',min_value=0, max_value=500)
num2 = st.slider('Please, enter another number:',min_value=1, max_value=500)
action = st.selectbox(label='Select an option for action:',options=['+',' - ', '*', '/'])
# action = input('Select action: +, -, *, /:')

if action =='+':
    output = num1 + num2
elif action ==' - ':
    output = num1 - num2
elif action =='*':
    output = num1 * num2
elif action =='/':
    output = num1 / num2
    
if output:
    #Выводим result
    st.markdown('The result: "{}"'.format(output))