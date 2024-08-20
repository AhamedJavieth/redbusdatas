import mysql.connector
import pandas as pd
import streamlit as st
import pandas as pd

 
conn = mysql.connector.connect(

    host="localhost",

    user="root",

    port="3306",

    password="Javi@571998",

    database="redbus"

)

table_name='redbus'
database="redbus"
cursor = conn.cursor()

writer = cursor 

query = "SELECT * FROM redbus"

query2 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND TABLE_SCHEMA = '{database}' ORDER BY ORDINAL_POSITION"

writer.execute(query)

view = cursor.fetchall()

data=pd.DataFrame(view)

writer.execute(query2)
s=cursor.fetchall() 
data=pd.DataFrame(view)
flat_list = [item[0] for item in s]
#flat_list_1=['s_no','route-collected','name','type','arrival_time','departure_time','duration','price','seats_available','rating']
data.columns=flat_list
data=data.set_index('s_no')
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data['price']=data['price'].fillna(0)
data['price']=data['price'].astype('int64')




st.set_page_config(
    page_title="Red-Bus Details",
    page_icon=r"C:\Users\javie\OneDrive\Desktop\guvi 1st project\6197450101333540700.jpg",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)
a,b=st.columns([1,2])
with b:
    st.title(':red[Redbus:bus:]')





price_min=int(data['price'].min())
price_max=int(data['price'].max())
rating_min = float(data['rating'].min())
rating_max = float(data['rating'].max())
rating = st.sidebar.slider('rating for 2nd', float(rating_min), float(rating_max ), (rating_min, rating_max))

price=st.sidebar.slider('pricefor2nd',price_min,price_max,(price_min, price_max))
x=data['route-collected'].drop_duplicates()
route_collected=st.sidebar.selectbox('routefor2nd',x)
#filtered_df = data[(data['price'] >= price[0]) & (data['price'] <= price[1] ) & data["rating"]<=rating[0] & data['rating']>=rating[1]]
filtered_df = data[
    (data['price'] >= price[0]) & 
    (data['price'] <= price[1]) & 
    (data['rating'] >= rating[0]) & 
    (data['rating'] <= rating[1]) &
    (data['route-collected']==route_collected)
]


st.title(':red[_*myfilter*_]:bus:')
st.write(filtered_df) 
x=data['route-collected'].drop_duplicates()
route_collected=st.selectbox('route',x)
filter1=data[data['route-collected']==route_collected] 
st.write(filter1)


# Assuming route_collected is a string, modify the query like this:
query = f"SELECT * FROM redbus WHERE price BETWEEN {price[0]} AND {price[1]} AND rating BETWEEN {rating[0]} AND {rating[1]} "

# Then, execute the query
writer.execute(query)


view2=cursor.fetchall()
query2 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND TABLE_SCHEMA = '{database}' ORDER BY ORDINAL_POSITION"
a=pd.DataFrame(view2)
st.write(a)