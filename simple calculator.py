import streamlit as st

# Title
st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Calculate button
if st.button("Calculate"):

    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (×)":
        result = num1 * num2

    else:  # Division
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
        else:
            result = num1 / num2

    if not (operation == "Division (÷)" and num2 == 0):
        st.success(f"✅ Result: {result}")
        st.balloons()