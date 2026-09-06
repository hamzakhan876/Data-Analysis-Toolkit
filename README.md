# 📊 Data Analysis Toolkit

A beginner-friendly **Streamlit data analysis application** that allows users to upload CSV datasets, explore their data, filter records, view statistical summaries, and create interactive visualizations.

The project was built as part of my learning journey in **Python, Data Analysis, and Generative AI engineering**.

## 🚀 Features

* 📂 Upload CSV datasets directly through the web interface
* 🔎 Filter dataset values interactively
* 📋 Preview uploaded data
* 📊 View dataset information including rows, columns, and missing values
* 📈 Generate interactive charts
* 📉 Create Bar, Line, Scatter, and Histogram visualizations
* 📐 View statistical summaries using Pandas
* 💾 Download the processed dataset as a CSV file
* ⚠️ Basic error handling for invalid CSV files and datasets without suitable numeric columns

## 🛠️ Technologies Used

* **Python** — Main programming language
* **Pandas** — Data loading, manipulation, and statistical analysis
* **NumPy** — Numerical computing foundation
* **Streamlit** — Web application interface
* **Plotly** — Interactive data visualization
* **Git & GitHub** — Version control and project management

## 📁 Project Structure

```text
Data-Analysis-Toolkit/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .devcontainer/
│   └── devcontainer.json
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/hamzakhan876/Data-Analysis-Toolkit.git
```

### 2. Open the project folder

```bash
cd Data-Analysis-Toolkit
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will provide a local URL where the application can be opened in your browser.

## 📊 How It Works

1. Launch the application.
2. Upload a CSV dataset.
3. The application reads the dataset using Pandas.
4. Dataset information and a data preview are displayed.
5. Users can filter the dataset.
6. Statistical summaries are generated.
7. Users can select a chart type and create an interactive visualization.
8. The processed dataset can be downloaded as a CSV file.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Working with CSV datasets
* Data cleaning and exploration
* Pandas DataFrames
* Numerical data handling
* Data visualization
* Building interactive applications with Streamlit
* Using Plotly for charts
* Handling user-uploaded files
* Basic error handling
* Managing Python dependencies
* Using Git and GitHub for project development

## 🔮 Future Improvements

Possible future improvements include:

* Adding more advanced statistical analysis
* Supporting additional file formats
* Adding correlation heatmaps
* Adding automatic data-quality reports
* Improving dashboard customization
* Adding more visualization options

## 👨‍💻 Author

**Hamza Ahmed Khan**

HND Computing Student
Python • Data Analysis • Generative AI
