📓 Model Training & Testing Notebooks
This folder contains Notebooks used for training and testing the facial emotion recognition model.
You can run these notebooks directly on Google Colab.

📂 Files
train_model.ipynb → Model training notebook (CNN-based)
test_model.ipynb → Model testing & prediction notebook

📥 Dataset Requirement
This project uses the FER2013 dataset:
📦 Dataset name: fer2013.csv
📥 Download it from Kaggle: FER2013 Dataset on Kaggle

🚩 Important: Before Running the Notebooks
You must upload the fer2013.csv file to your Google Drive or Colab runtime.
✅ Change the CSV file path in the notebook — currently it points to my personal Google Drive.
Example:
# Change this line to your own path
df = pd.read_csv('/path/to/your/fer2013.csv')

🚀 Running on Google Colab
Open the notebook (e.g., train_model.ipynb)
Click "Open in Colab" (or upload it to your Colab)
Make sure to:
Upload the fer2013.csv dataset
Adjust the dataset path in code
Run all cells to train/test the model!

💾 Output
The trained model will be saved as .h5 file (e.g., model.h5)
You can use this saved model in the Streamlit app for real-time emotion detection.

🙏 Thank you!
For any issues, feel free to raise an issue or pull request.
