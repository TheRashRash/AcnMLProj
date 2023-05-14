import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

# Create the main window
window = tk.Tk()
window.title("Machine Learning Graph")

def import_dataset():
    # Open a file dialog to select the dataset file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    # Process the dataset file

# Create the import button
import_button = tk.Button(window, text="Import Dataset", command=import_dataset)
import_button.pack()

def plot_graph():
    # Plot the graph
    plt.scatter(x_data, y_data)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Data Points")
    plt.show()

# Create the plot button
plot_button = tk.Button(window, text="Plot Graph", command=plot_graph)
plot_button.pack()


def select_model():
    selected_model = model_var.get()
    # Perform actions based on the selected model

# Create the model selection radio buttons
model_var = tk.StringVar()

linearReg_radio = tk.Radiobutton(window, text="Linear Regression", variable=model_var, value="linearReg")
linearReg_radio.pack()

logisticReg_radio = tk.Radiobutton(window, text="Logistic Regression", variable=model_var, value="logisticReg")
logisticReg_radio.pack()

polynomReg_radio = tk.Radiobutton(window, text="Polynomial Regression", variable=model_var, value="polynomReg")
polynomReg_radio.pack()

# Create the select button
select_button = tk.Button(window, text="Select Model", command=select_model)
select_button.pack()

window.mainloop()