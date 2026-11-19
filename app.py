import streamlit as st

st.set_page_config(page_title="FieldMitra AI", layout="wide")
st.title("FieldMitra AI - Field Officer Helper")
st.write("Officer adigithe, evaru loan kattaro cheppe app.")

name = st.text_input("Customer peru rayandi - Ex: Kavitha")
months_paid = st.slider("Last 6 months lo enni sarlu kattaru?", 0, 6, 5)
late_count = st.slider("Enni sarlu late chesaru?", 0, 6, 0)

if st.button("Check Chey"):
    score = (months_paid * 12) - (late_count * 8) + 20
    if score > 100:
        score = 100
    if score < 0:
        score = 0

    st.subheader(f"{name} - Trust Score: {score}/100")

    if score >= 80:
        st.success("SAFE - Malli loan ivvochu")
        st.write("Ee customer correct ga kattaru. Nammachu.")
    elif score >= 50:
        st.warning("REVIEW - Velli matladali")
        st.write("Konchem careful ga undandi. Velli oka sari adagandi.")
    else:
        st.error("RISK - Ippudu loan vaddu")
        st.write("Ippudu loan ivvakandi. Konni rojulu aagi chudandi.")

    st.divider()
    st.subheader("Ee Roju Collection Route")
    st.write("1. Kavitha garu - Nellore - Rs 2,500")
    st.write("2. Suresh garu - Kovur - Rs 3,000")
    st.write("3. Lakshmi garu - Gudur - Rs 1,800")
    st.write("Total today: Rs 7,300 collect avvochu")
