import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import random

# st.title('калькулятор индекса массы тела')

# weight = st.number_input('Введите ваш вес ')

# status = st.radio('Укажите единицы измерения роста: ', ('см', 'м', 'футы'))

# if (status== 'см'):
#     height = st.number_input('Сантимерты')
    
#     try:
#         bmi = weight / (height ** 2)
#     except:
#         height = st.number_input('Футы')

#         try:
#             bmi = weight / ((height / 3.28) ** 2)
#         except:
#             st.text('Введите ваш рост')


# if (st.button('Расчитать ИМТ')):

#     st.text(f'Ваш ИМТ равен {bmi:.2f}')

#     if (bmi < 16):
#         st.error('Выраженный дефицит массы тела')
#     elif (bmi >= 16 and bmi < 18.5):
#         st.warning('Недлостаточная масса тела')
#     elif (bmi >= 18.5 and bmi < 25):
#         st.success('Норма')
#     elif(bmi >= 25 and bmi < 30):
#         st.warning('Избыточная масса тела')
#     elif (bmi > 30):
#         st.error('Любитель вкусняшек')

#заголовок
st.title(':green[Домашнее задание #10]')


#загрузка файлов на сервер
upload_file = st.file_uploader(':orange[Загрузите файл чтобы отобразить его]')

if upload_file:
    progress_text = ":violet[Загрузка и отображение файла. Пожалуйста подождите.]"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    #отображние датафрейма
    st.write('Вывод вашего файла')
    df = pd.read_csv('appstore_instagram_reviews_anonymized.csv')
    st.dataframe(df)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Создаем гистограмму
    plt.hist(df['score'])
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.title('гистограмма оценок')
    st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False) 
data = np.random.randn(1000)
# Создаем гистограмму
plt.hist(data)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('')
st.pyplot()

#введите текст
txt = st.text_input(':rainbow[Введите ваше Имя]')
if txt:
    st.text(f'ПРИВЕТ {txt}')

st.write('Привет!')

#какое настроение ?
status = st.radio(':rainbow[Какое у Вас сегодня настроение? ]: ', ('отличное', 'хорошее', 'нормальное', 'плохое'))
if status == 'отличное':
    st.write('Супер Пупер !!!🥳')
elif status == 'хорошее':
    st.write('Вот и правильно !!')
elif status == 'нормальное':
    st.write('Всё нормально !😐')
elif status == 'плохое':
    st.write('Не грусти!😔! А то Мозг не будет расти!😂')

#мини калькулятор
nums = st.text_input('Введите две цифры через пробел для сложения')
if nums:
    nums = list(map(int, nums.split()))
    st.write(nums[0] + nums[1])
    st.text('Отлично!')

st.image('photo-1548407260-da850faa41e3.jpg', 'Просто красивая картинка для созерцания')

#game
random.seed(42)
number = random.randint(1, 10)
select = st.radio(':blue[Выбери число: ]', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
# st.write(str(number))
if select:
    if select == str(number):
        st.write('Сегодня Ваш День!!! Можете покупать билет в лотерею...🥳🥳🥳🥳🥳')
    else:
        st.write('Непруха, попробуй еще !')