import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import json 
import plotly.express as px




app_title="Phonepe Pulse"

app_sub_title="All India"


# [theme]
# primaryColor="#c874b2"
# backgroundColor="#210535"
# secondaryBackgroundColor="#430d4b"
# textColor="#f5d5e0"



st.set_page_config(app_title)
st.title(app_title)
st.header('Data Visualization and Exploration:')
st.subheader(app_sub_title)


     
col1, col2 ,col3 = st.columns(3)

with col1:
    option1 = st.selectbox( 
        '', 
        ('Transactions', 'Users'))
    st.write('You selected:', option1)

with col2:
    option2 = st.selectbox(
        'Year',
        ('2018','2019','2020','2021','2022'))

    st.write('You selected:', option2)

with col3:
    option3 = st.selectbox(
        'Month',
        ('Q1(Jan-Mar)','Q2(Apr-Jun)','Q3(Jul-Sep)','Q4(Oct-Dec)'))

    st.write('You selected:', option3)

if option1 =='Transactions':

    if option2 == '2018': 
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2018/1.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2018/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2018/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2018/2.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2018/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2018/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2018/3.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2018/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2018/3.json') 
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2018/4.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2018/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2018/4.json')
    if option2 == '2019':
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2019/1.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2019/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2019/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2019/2.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2019/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2019/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2019/3.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2019/3.json') 
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2019/3.json')
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2019/4.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2019/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2019/4.json')
    if option2 == '2020':
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2020/1.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2020/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2020/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2020/2.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2020/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2020/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('//Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2020/3.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2020/3.json') 
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2020/3.json')
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2020/4.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2020/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2020/4.json')
    if option2 == '2021':
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2021/1.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2021/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2021/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2021/2.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2021/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2021/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2021/3.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2021/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2021/3.json') 
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2021/4.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2021/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2021/4.json')

    if option2 == '2022':  
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2022/1.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2022/1.json')
            dmap=pd.read_json('//Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2022/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2022/2.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2022/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2022/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2022/3.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2022/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2022/3.json') 
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/aggregated/transaction/country/india/2022/4.json')
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2022/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/transaction/hover/country/india/2022/4.json')
      
        
        







    fg=df['data']['transactionData']
            
    fg1=pd.json_normalize(fg)
                
    fgs=fg1['paymentInstruments']
    f1=pd.DataFrame(fgs[0],index=[0])
    f2=pd.DataFrame(fgs[1],index=[1])
    f3=pd.DataFrame(fgs[2],index=[2])
    f4=pd.DataFrame(fgs[3],index=[3])
    f5=pd.DataFrame(fgs[4],index=[4])


    fs=[f1,f2,f3,f4,f5]
    re=pd.concat(fs)
                
    co2=fg1['name']
    co2_1=pd.DataFrame(co2)

    det=co2_1.join(re)

                
    st.subheader('Categories:')
    st.write(det)



    dmap=dmap['data']['hoverDataList']
    dmap=pd.json_normalize(dmap)
    a=dmap['name']

    fx=[]

    for x in range(len(dmap['metric'])):
        fx.append(dmap['metric'][x][0])
        
        

        
    dfma=pd.DataFrame(fx)

    dfma['country_name']=a
    #print(type(df))
    dfma['country_name'][9]='dadara & nagar havelli'
    dfma['country_name'][11]='andaman & nicobar island'
    dfma.drop(14,axis=0,inplace=True)
    dfma['country_name'][33]='arunanchal pradesh'
    dfma.drop(34,axis=0,inplace=True)

    india_states= json.load(open("/Users/kesavakumarpommu/Downloads/states_india.geojson","r"))

    state_id_map = {}
    for feature in india_states['features']:
        feature['id']=feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']]=feature['id']

    new_dict = dict((k.lower(), v) for k, v in state_id_map.items()) 

    dfma['id']=dfma['country_name'].apply(lambda x: new_dict[x])

    fig=px.choropleth(dfma, 
                    locations='id',
                    geojson=india_states,
                    color='count',
                    hover_name='country_name',
                    hover_data=['amount'],
                    title='Transactions')
    fig.update_geos(fitbounds='locations',visible=False)





if option1 =='Users':   

    if option2 == '2018': 
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2018/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2018/1.json')

        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2018/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2018/2.json')
            
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2018/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2018/3.json')
              
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2018/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2018/4.json')
    
    if option2 == '2019':
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2019/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2019/1.json')
           
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2019/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2019/2.json')
            
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2019/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2019/3.json')
              
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2019/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2019/4.json')
    
    if option2 == '2020':
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2020/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2020/1.json')
           
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2020/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2020/2.json')
            
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2020/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2020/3.json')
              
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2020/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2020/4.json')
    
    if option2 == '2021':
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2021/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2021/1.json')
           
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2021/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2021/2.json')
            
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2021/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2021/3.json')
              
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2021/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2021/4.json')
    

    if option2 == '2022':  
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2022/1.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2022/1.json')
           
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2022/2.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2022/2.json')
            
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2022/3.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2022/3.json')
              
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/user/country/india/2022/4.json')
            dmap=pd.read_json('/Users/kesavakumarpommu/Downloads/pulse-master/data/map/user/hover/country/india/2022/4.json')

    dmap=dmap['data']['hoverData']

    l1=list(dmap.keys())
    l1=pd.DataFrame(l1)

    l2=list(dmap.values())
    l2=pd.DataFrame(l2)  

    dfm=pd.concat([l1,l2],axis=1)  
    dfm.rename({0:'state_name'},axis=1,inplace=True) 

    dfm['state_name'][9]='dadara & nagar havelli'
    dfm['state_name'][11]='andaman & nicobar island'
    dfm.drop(14,axis=0,inplace=True)
    dfm['state_name'][33]='arunanchal pradesh'
    dfm.drop(34,axis=0,inplace=True)     

    india_states= json.load(open("/Users/kesavakumarpommu/Downloads/states_india.geojson","r"))

    state_id_map = {}
    for feature in india_states['features']:
        feature['id']=feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']]=feature['id']
        
    # state_id_map

    # my_dict = {'KEY1': "Hello", 'Key2': "World"} 
    new_dict = dict((k.lower(), v) for k, v in state_id_map.items()) 
    dfm['id']=dfm['state_name'].apply(lambda x: new_dict[x])

    fig=px.choropleth(
        dfm, 
        locations='id',
        geojson=india_states,
        color='registeredUsers',
        hover_name='state_name',
        hover_data=['appOpens'],
        title='Users',
     )
    fig.update_geos(fitbounds='locations',visible=False)








st.subheader('Top 10')
col1,col2,= st.columns(2)

with col1:
        
        if st.button('States'):
            if option1 == 'Users':
       
                df1=dfs['data']['states']
                pd.DataFrame(df1)
                st.table(df1)

            if option1 =='Transactions':
                df1=dfs['data']['states']
                fg1=pd.json_normalize(df1)
                fg1


with col2:
        if st.button('Districts'):
            if option1 == 'Users':
                df1=dfs['data']['districts']
                pd.DataFrame(df1)
                st.table(df1)

            if option1 =='Transactions':
                df1=dfs['data']['districts']
                fg1=pd.json_normalize(df1)
                fg1       



if st.button('Pincodes'):
        if option1 == 'Users':
                df1=dfs['data']['pincodes']
                pd.DataFrame(df1)
                st.table(df1)


        if option1 =='Transactions':
                df1=dfs['data']['pincodes']
                fg1=pd.json_normalize(df1)
                fg1 
        

st.plotly_chart(fig)









# with open('/Users/kesavakumarpommu/Downloads/pulse-master/data/top/transaction/country/india/2018/1.json') as file:
#     data=json.load(file)
    
# df1=data['data']['states']
# df=pd.json_normalize(df1)
# table_name = 'Top'



# conn = sqlite3.connect('mydb.sqlite')
# query = f'Create table if not Exists {table_name} (Name text, Type text, Count real, Amount real)'
# conn.execute(query)
# df.to_sql(table_name,conn,if_exists='replace',index=False)
# conn.commit()


# r_df = pd.read_sql("select * from Top",conn)
# display(r_df)

