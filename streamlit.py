import pickle
import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
 

#Loading up the Classification model we created
model = pickle.load(open('KNNClassifierModel.pkl', 'rb'))
Area_dic = pickle.load(open('Area_dic.pkl', 'rb'))
rest_type_dic = pickle.load(open('rest_type_dic.pkl', 'rb'))

# Define the prediction function
def predict(online_order, book_table, rest_type, multiple_types, total_cuisines, Area, approx_cost):
    
    #Predicting the price of the carat
    if online_order == 'Yes':
        online_order = 1
        return online_order
    elif online_order == 'No':
        online_order = 0
        return online_order
##############################
    if book_table == 'Yes':
        book_table = 1
        return book_table
    elif book_table == 'No':
        book_table = 0
        return book_table
##############################
    if Type in rest_type_dic:
        rest_type = rest_type_dic[Type]
        return rest_type
    else :
        rest_type = 'The rest type Not Found'
        return rest_type 
########################################
    if Area in Area_dic:
        Area = Area_dic[Area]
        return Area
    else :
        Area = 'The Area Not Found'
        return Area
    
    prediction = model.predict(pd.DataFrame([[online_order, book_table, rest_type, multiple_types, total_cuisines, Area, approx_cost]], columns=['online_order', 'book_table', 'rest_type', 'multiple_types', 'total_cuisines', 'Area', 'approx_cost']))
    return prediction


st.title('Zomato Success Restaurant Predictor')
st.image("""https://techstory.in/wp-content/uploads/2022/02/Zomato.jpg""")
st.header('Enter the restaurant details:')

online_order = st.selectbox('Online Order:', ['Yes','No'])
book_table = st.selectbox('Book Table:', ['Yes','No'])
multiple_types = st.number_input('Number Of Restaurant Type He Give:', min_value=1, max_value=2, value=1)
total_cuisines = st.number_input('Number Of Food Styles:', min_value=1, max_value=8, value=1)
approx_cost = st.number_input('Contains The Approximate CCost For Meal For Two People:', min_value=40, max_value=6000)
Area = st.selectbox('Area:', list(Area_dic.keys()))
rest_type = st.selectbox('Restaurant Type:', list(rest_type_dic.keys()))

if st.button('Will the restaurant succeed or not?'):
    price = predict(online_order, book_table, rest_type, multiple_types, total_cuisines, Area, approx_cost)
    if price == 1:
        price = 'Yes'
    elif price == 0:
        price = 'No'
    st.success(f'The predicted of the restaurant succeed is : {price}')
