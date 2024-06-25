import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

st.title("LaTeX Matrix Generator and Image Exporter")

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

# Convert LaTeX to image
def latex_to_image(latex_code):
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.text(0.5, 0.5, f"${latex_code}$", horizontalalignment='center', verticalalignment='center', fontsize=20)
    ax.axis('off')
    
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)
    plt.close(fig)
    return buf

# Generate and download image
if st.button("Generate and Download Image"):
    image_buf = latex_to_image(latex_code)
    st.download_button(label="Download Image", data=image_buf, file_name="matrix.png", mime="image/png")
    
    # Display image
    image = Image.open(image_buf)
    st.image(image, caption="Generated Matrix Image")
