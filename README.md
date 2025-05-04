# 🧠 AI Resume Screener

A simple AI-powered tool to screen resumes against a given job description using keyword-based similarity. Built with **Python**, **Streamlit**, and **scikit-learn**, it ranks uploaded resumes (PDFs) based on how closely they match the job description.

---
## Screenshot:
![image](https://github.com/user-attachments/assets/7649c014-4218-4e5e-8f65-e23558c873fc)

---
## 🚀 Features

- ✅ Upload multiple resumes (PDF format)
- 📄 Paste any job description
- 🔍 Calculates similarity using bag-of-words and cosine similarity
- 📊 Ranks resumes from best to worst match
- 🖥️ Clean and interactive web interface (Streamlit)

---

## 📁 Project Structure

ai_resume_screener/  
├── main.py # Streamlit app  
├── requirements.txt # Python dependencies  
└── README.md # Project documentation  

---

## 🔧 Installation  

1. **Clone the repo:**

git clone https://github.com/Pavan-Kumar-Mallela/Ai-resum--screener.git
cd Ai-resum--screener

2. **Install dependencies:**

pip install -r requirements.txt

3. **Run the app:**

streamlit run main.py

---

📌**Example Usage**  
->Copy a Job Description from LinkedIn, Naukri, etc.

->Upload multiple Resume PDFs

->Click "Evaluate"

->See ranked resumes with match percentage

---

💡 **Future Improvements**  
->Use NLP techniques (NER, skill extraction) with spaCy

->Add BERT or GloVe-based semantic matching

->Export results to Excel/CSV

->Add candidate detail extraction (email, phone, experience, etc.)

---

##🙋‍♂️ Author  
Pavan Kumar Mallela  
📍 Visakhapatnam, India  
📧 pavankumarmallela0211@gmail.com  

---

##📜 License  
This project is open-source and free to use under the MIT License.
