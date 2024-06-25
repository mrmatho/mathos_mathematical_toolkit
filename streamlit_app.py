import streamlit as st
import matplotlib.pyplot as plt
import io

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

# JavaScript to copy to clipboard
copy_button = st.button("Copy LaTeX to clipboard")
if copy_button:
    st.code(
        """
        <script>
        function copyToClipboard(text) {
            const textarea = document.createElement('textarea');
            textarea.value = text;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            alert('LaTeX code copied to clipboard!');
        }
        copyToClipboard(`""" + latex_code.replace("`", "\\`") + """`);
        </script>
        """,
        language='html',
    )

# Convert LaTeX to image and download
st.write("Download LaTeX as Image")
img_buffer = io.BytesIO()
fig, ax = plt.subplots(figsize=(2, 2))
ax.text(0.5, 0.5, f"${latex_code}$", horizontalalignment='center', verticalalignment='center', fontsize=12)
ax.axis('off')
plt.savefig(img_buffer, format='png')
plt.close(fig)
st.download_button(label="Download Image", data=img_buffer, file_name="matrix.png", mime="image/png")
