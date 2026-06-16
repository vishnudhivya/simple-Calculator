import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Calculator")

# Initialize display
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display screen
st.text_input(
    "Display",
    value=st.session_state.expression,
    disabled=True
)

# Function for button clicks
def press(value):
    st.session_state.expression += value

# Row 1
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7"):
        press("7")
with col2:
    if st.button("8"):
        press("8")
with col3:
    if st.button("9"):
        press("9")
with col4:
    if st.button("/"):
        press("/")

# Row 2
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("4"):
        press("4")
with col2:
    if st.button("5"):
        press("5")
with col3:
    if st.button("6"):
        press("6")
with col4:
    if st.button("*"):
        press("*")

# Row 3
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("1"):
        press("1")
with col2:
    if st.button("2"):
        press("2")
with col3:
    if st.button("3"):
        press("3")
with col4:
    if st.button("-"):
        press("-")

# Row 4
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("0"):
        press("0")
with col2:
    if st.button("."):
        press(".")
with col3:
    if st.button("="):
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
with col4:
    if st.button("+"):
        press("+")

# Clear button
if st.button("C", use_container_width=True):
    st.session_state.expression = ""
