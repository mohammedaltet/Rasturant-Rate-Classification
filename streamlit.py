import pickle
import streamlit as st
import pandas as pd

# Loading the Classification model we created
model = pickle.load(open('KNNClassifierModel.pkl', 'rb'))
Area_dic = pickle.load(open('Area_dic.pkl', 'rb'))
rest_type_dic = pickle.load(open('rest_type_dic.pkl', 'rb'))

# Define the prediction function
def predict(online_order, book_table, rest_type, multiple_types, total_cuisines, Area, approx_cost):
    # Transforming categorical input to numeric values
    online_order = 1 if online_order == 'Yes' else 0
    book_table = 1 if book_table == 'Yes' else 0
    
    rest_type = rest_type_dic.get(rest_type, 'The rest type Not Found')
    Area = Area_dic.get(Area, 'The Area Not Found')

    # Predicting the success of the restaurant
    prediction = model.predict(pd.DataFrame([[online_order, book_table, rest_type, multiple_types, total_cuisines, Area, approx_cost]], columns=['online_order', 'book_table', 'rest_type', 'multiple_types', 'total_cuisines', 'Area', 'approx_cost']))
    return prediction[0]

st.title('Zomato Success Restaurant Predictor')
st.image("https://techstory.in/wp-content/uploads/2022/02/Zomato.jpg")
st.header('Enter the restaurant details:')

online_order = st.selectbox('Online Order:', ['Yes', 'No'])
book_table = st.selectbox('Book Table:', ['Yes', 'No'])
multiple_types = st.number_input('Number Of Restaurant Type:', min_value=1, max_value=2, value=1)
total_cuisines = st.number_input('Number Of Food Styles:', min_value=1, max_value=8, value=1)
approx_cost = st.number_input('The Approximate Cost For Meal For Two People:', min_value=40, max_value=6000)
Area = st.selectbox('Area:', list(Area_dic.keys()))
rest_type = st.selectbox('Restaurant Type:', list(rest_type_dic.keys()))

if st.button('Will the restaurant succeed or not?'):
    prediction = predict(online_order, book_table, rest_type, multiple_types, total_cuisines, Area, approx_cost)
    result = 'Yes' if prediction == 1 else 'No'
    st.success(f'The predicted success of the restaurant is {result}')
