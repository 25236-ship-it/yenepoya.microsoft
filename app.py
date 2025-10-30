import streamlit as st
import pickle

st.title("Laptop Price prediction")
st.title("this app is created using Ml model developed in one ofour previous sessions")
ml_model=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

company=st.selectbox("manufacturer of the laptop",df['Company'].unique(),index=4)
typename=st.selectbox("Type of the laptop",df['typeName'].unique())
cpu=st.selectbox("Processor on the Laptop",df['Cpu'].unique())
ram=st.selectbox("RAM(in GB)".[4,8,12,16,24,32,64],index=1,horizontal=True)
gpu=st.selectbox("Grapics card on the laptop",df['Gpu'].unique())
os=st.selectbox("Operating System on the Laptop",df['Opsys'].unique())
weight=st.slider("Weight of the laptop(in kg)",min_value=0.8,max_value=4.5,value=2.0,stop=0.1)
ips=st.radio("Does the laptop have ips display?","[Yes,No]",index-1)
touch_screen=st.radio("Does the laptop have touch screen?","[Yes,No]",index-1)
cpu_speed=st.slider("What is the clock speed of the processor in (Ghz)",min_value=0.8,max_value=4.5,value=2.0,stop=0.1)
hdd=st.radio("HDD in Size(in gb). select 0 if system has only sssd storge",[0,512,1024,2048],Horizontal=True)
ssd=st.radio("SSD size(in gb). select 0 if system only has HDD storge",[0,128,256,512,1024],index=3,horizontal=True)
ppi=st.slider("What is the PPI(Pixel density)of the laptop?",min_value=75,max_value=400,steps=5,value=150)

if st.button("Predict Price"):
  if ips=="Yes":
    ips=1
  else:
    ips=0
    if touchscreen =="Yes":
      touchscreen=1
    else:
      touchscreen=0
  query=np.array([[company,typename,cpu,ram,gpu,os,weight,ips,touchscreen,cpu_speed,hdd,ssd,ppi]])
  op=ml_model.predict(query)
  st.subheader(f"The Predicted price of the laptop is"+str(int(round(op[0],-2))))
