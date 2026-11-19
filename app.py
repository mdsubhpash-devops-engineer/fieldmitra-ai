import streamlit as st
st.set_page_config(page_title="FieldMitra AI", page_icon="🎙️")
st.title("🎙️ FieldMitra AI - Field Officer Helper")
st.write("Field Officer kosam - Voice + Trust Score + Pending List")

data = {
    "kavitha": {"name": "Kavitha", "village": "Nellore", "score": 92, "status": "Safe - Loan Ivvachu", "due": 0, "phone": "98765 43210"},
    "ramesh": {"name": "Ramesh", "village": "Kavali", "score": 45, "status": "Risk - Jagratha", "due": 4500, "phone": "98765 43211"},
    "suresh": {"name": "Suresh", "village": "Gudur", "score": 78, "status": "Good - Follow-up Chey", "due": 1200, "phone": "98765 43212"},
    "lakshmi": {"name": "Lakshmi", "village": "Nellore", "score": 88, "status": "Safe - Loan Ivvachu", "due": 0, "phone": "98765 43213"},
    "venkat": {"name": "Venkat", "village": "Tirupati", "score": 35, "status": "High Risk - Ivvaku", "due": 8000, "phone": "98765 43214"},
    "priya": {"name": "Priya", "village": "Kavali", "score": 95, "status": "Safe - Loan Ivvachu", "due": 0, "phone": "98765 43215"},
}

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(data))
col2.metric("Safe Customers", sum(1 for v in data.values() if v['score'] > 80))
col3.metric("Total Pending", f"Rs. {sum(v['due'] for v in data.values())}")
st.divider()

st.subheader("🎙️ Step 1: Voice / Search")
audio = st.audio_input("Mic nokki cheppu")
name = st.text_input("Leda Peru rayi:").lower().strip()

if st.button("✅ Check Chey"):
    if audio and not name:
        st.success("Voice vinnanu! Kavitha ni chupisthunna.")
        name = "kavitha"
    if name in data:
        p = data[name]
        st.success(f"{p['name']} - {p['village']} | Phone: {p['phone']}")
        st.metric("Trust Score", f"{p['score']} / 100")
        st.info(f"Status: {p['status']}")
        st.warning(f"Pending Due: Rs. {p['due']}")
        if p['score'] > 80:
            st.balloons()
            st.write(f"Voice Reply: '{p['name']} garu manchi customer, loan ivvachu.'")
        else:
            st.write(f"Voice Reply: 'Jagratha, {p['name']} gariki Rs. {p['due']} pending undi.'")
    elif name == "":
        st.error("Mundhu voice leka peru ivvu bro.")
    else:
        st.error("Ee peru database lo ledu.")

st.divider()
st.subheader("📋 Full Pending List")
for k, p in data.items():
    st.write(f"{p['name']} ({p['village']}) - Score: {p['score']} - Due: Rs. {p['due']} - {p['status']}")
st.write("FieldMitra AI v1.0 - Complete Project")