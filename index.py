import streamlit as st
import pickle


#to open file in read mode
file1=open("model1.pkl","rb")
file2=open("scale1.pkl","rb")


#to read data from file (file1 and file2)
model=pickle.load(file1)   #load()  inbuilt method of pickle,to read data from file
scale=pickle.load(file2)
#model and scale both are user defined object

st.title("Insurance Claim Prediction")

#st.number_input() : to accept numeric data from user on UI page
age=st.number_input('Age',format='%2d',value=0)
#age = st.slider("Age", 18, 70, 25)
sex=st.number_input('Gender : 1-Male / 0-Female',format='%d',value=0)
#gender = st.radio("Gender", ('Male', 'Female'))
bmi=st.number_input('BMI',format='%2d')
children=st.number_input('children 0-5',format='%1d',value=0)
smoker=st.number_input('smoker 1-yes/0-no',format='%d',value=0)
region=st.number_input('region 0-3',format='%d',value=0)
charges=st.number_input('Charges',format='%2d')
                       
#create a list X and hold all inputs in this list according to sequence of given dataset
X=[age,sex,bmi,children,smoker,region,charges]
                       
if st.button('predict'):
         #To change list in numpy array (2D)
         import numpy as np
         X=np.array([X]) #[[]] means 2D
         #Apply StandardScaler n input exp
         X=scale.transform(X)

         #predict whether customer claim for insurance or not
         Y_pred=model.predict(X)[0]
         
         if Y_pred==0:
            st.success("customer will not claim for insurance")
            #ans="customer will not claim for insurance"
         else:
            st.error("customer will claim for insurance")
            #ans='customer will claim for insurance'
         #st.write(ans)
         #write() inbuilt method of streamlit,to show output on UI page             
         #input() inbuilt input method of streamlit,bydefault string value 
         #number_input() : to aacept numeric type data(float type) ,if int type ,the use format ='%d' bydefault float       
        # Reset button to clear input values
#if st.button("Reset Values"):
# Reset user input values
   # age =" "
    #sex = ' '
   # bmi = " "
    # Add other relevant features...
   
#if st.button("Delete Values"):
  #      # Delete user input values
     #   X = []
