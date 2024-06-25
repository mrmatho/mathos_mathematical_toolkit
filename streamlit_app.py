import streamlit as st

st.title("LaTeX Matrix Generator")

# Get matrix dimensions from user
rows = st.number_input("Number of rows", min_value=1, max_value=10, value=2, step=1)
cols = st.number_input("Number of columns", min_value=1, max_value=10, value=2, step=1)

# Initialize matrix
matrix = []

st.write("Enter matrix elements:")

# Input matrix elements
for i in range(rows):
    row = []
    for j in range(cols):
        element = st.text_input(f"Element ({i+1}, {j+1})", key=f"{i}-{j}")
        row.append(element)
    matrix.append(row)

# Generate LaTeX code
latex_code = "\\begin{bmatrix}\n"
for row in matrix:
    latex_code += " & ".join(row) + " \\\\\n"
latex_code += "\\end{bmatrix}"

# Display and allow modification of LaTeX code
latex_code = st.text_area("Generated LaTeX code:", value=latex_code, height=200)

# Render LaTeX code
st.write("Rendered Matrix:")
st.latex(latex_code)