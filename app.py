import streamlit as st

st.title("GPA Calculator - BIOtech 2025 batch")
st.write("Enter your marks for 100 and get your CGPA")

# Get mark 
mark_BTB101 =st.number_input("Enter Total mark [BTB 101]:")
mark_BTB102 =st.number_input("Enter Total mark [BTB 102]:")
mark_BTB103 =st.number_input("Enter Total mark [BTB 103]:")
mark_GPB111 =st.number_input("Enter Total mark [GPB 111]:")
mark_MAT101 =st.number_input("Enter Total mark [MAT 101]:")
mark_AGR101 =st.number_input("Enter Total mark [AGR 101]:")
mark_AEX101 =st.number_input("Enter Total mark [AEX 101]:")
mark_SECTAM121ENG121 =st.number_input("Enter Total mark [SEC 1 TAM or ENG]:")
mark_SECPTC =st.number_input("Enter Total mark [SEC 2 PTC]:")

# Divide by 10 and get grade point
GP_BTB101 = mark_BTB101/10
GP_BTB102 = mark_BTB102/10
GP_BTB103 = mark_BTB103/10
GP_GPB111 = mark_GPB111/10
GP_MAT101 = mark_MAT101/10
GP_AGR101 = mark_AGR101/10
GP_AEX101 = mark_AEX101/10
GP_SECTAM121ENG121 = mark_SECTAM121ENG121/10
GP_SECPTC = mark_SECPTC/10
 

 # multiply grade point and credits and get credit point
CP_BTB101 = GP_BTB101*2
CP_BTB102 = GP_BTB102*3
CP_BTB103 = GP_BTB103*2
CP_GPB111 = GP_GPB111*3
CP_MAT101 = GP_MAT101*1
CP_AGR101 = GP_AGR101*3
CP_AEX101 = GP_AEX101*2
CP_SECTAM121ENG121 = GP_SECTAM121ENG121*2
CP_SECPTC = GP_SECPTC*2


raw_CPS =[CP_BTB101,CP_BTB102,CP_BTB103,CP_GPB111,CP_MAT101,CP_AGR101,CP_AEX101,CP_SECTAM121ENG121,CP_SECPTC]
CPS = [round (x,2) for x in raw_CPS]

# add all Credit points 
CCPS = sum(CPS)

#create total Cumulative credits
CC =float(20)

#Calculate GPA
if st.button("Calculate GPA",type="primary"):
GPA = round(CCPS/CC,2)
st.info(f"Credit Points list: {CPS}")
st.info(f"Cumaltive credit point:{CCPS}")
st.metric(label="GPA", value=f"{GPA} / 10.0")




