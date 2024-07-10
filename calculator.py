import streamlit as st

def calculator():
    st.title("Calculator App")

    option = st.selectbox(
        "Select operation",
        ("Addition", "Subtraction", "Multiplication", "Division", "Modulus")
    )

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")

    result = None
    if option == "Addition":
        result = a + b
    elif option == "Subtraction":
        result = a - b
    elif option == "Multiplication":
        result = a * b
    elif option == "Division":
        if b != 0:
            result = a / b
        else:
            st.error("Error: Division by zero!")
    elif option == "Modulus":
        result = a % b if b != 0 else None

    if result is not None:
        st.success(f"{option} of {a} and {b} = {result}")

if __name__ == "__main__":
    calculator()
