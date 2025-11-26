import streamlit as st

st.title("⚡ Electricity Bill Calculator")

units = st.number_input("Enter Units Consumed", min_value=0, step=1)

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

gst = bill * 0.18
total = bill + gst

st.subheader("🧾 Bill Summary")
st.write(f"Units Consumed: **{units}**")
st.write(f"Bill Amount: **₹{bill:.2f}**")
st.write(f"GST (18%): **₹{gst:.2f}**")
st.write(f"Total Payable: **₹{total:.2f}**")

