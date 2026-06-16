import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to handle button presses
def press(value):
    st.session_state.expression += value

# CSS Styling
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 70px;
    font-size: 28px;
    font-weight: bold;
    border-radius: 15px;
    background-color: #2E86C1;
    color: white;
}

div.stButton > button:hover {
    background-color: #1B4F72;
    color: white;
}

input {
    text-align: right !important;
    font-size: 32px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Calculator")

# Display
st.text_input("", value=st.session_state.expression, disabled=True)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    cols = st.columns(4)
    for i, button in enumerate(row):
        with cols[i]:
            if st.button(button):
                if button == "=":
                    try:
                        st.session_state.expression = str(
                            eval(st.session_state.expression)
                        )
                    except:
                        st.session_state.expression = "Error"
                else:
                    press(button)

if st.button("C", use_container_width=True):
    st.session_state.expression = ""
