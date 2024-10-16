import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Streamlit Title
st.title("Interactive Linear Regression Simulator")

# Step 1: User Input for coefficients using sliders
st.sidebar.header("Adjust the Linear Equation")
slope = st.sidebar.slider("Slope (m)", min_value=-10.0, max_value=10.0, value=2.5, step=0.1)
intercept = st.sidebar.slider("Intercept (b)", min_value=-10.0, max_value=10.0, value=5.0, step=0.1)
noise_level = st.sidebar.slider("Noise Level", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

# Step 2: Generate Random Data (X, Y) based on user input
np.random.seed(42)  # For reproducibility
X = np.random.rand(100, 1) * 10  # Random X values between 0 and 10
noise = np.random.randn(100, 1) * noise_level  # Random noise scaled by user choice
Y = slope * X + intercept + noise  # Linear equation with noise

# Step 3: Perform Linear Regression (for visualization purposes)
model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

# Step 4: Plot the Data Points and the Regression Line
fig, ax = plt.subplots()
ax.scatter(X, Y, color='blue', label='Data Points')  # Scatter plot
ax.plot(X, Y_pred, color='red', label='Fitted Line')  # Fitted regression line
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title(f"Linear Regression: Y = {slope:.2f}X + {intercept:.2f}")
ax.legend()

# Step 5: Display the Plot in Streamlit
st.pyplot(fig)

# Step 6: Display the equation parameters
st.write(f"### Equation Parameters: Y = {slope:.2f}X + {intercept:.2f}")
st.write(f"### Noise Level: {noise_level}")
