# 🐔 PoultryDetect – AI-Powered Poultry Disease Classification

**PoultryDetect** is a smart AI-powered web application that leverages deep learning to help poultry farmers and veterinarians detect diseases in chickens through image analysis.

> 🎯 **Mission:** Empower poultry owners with fast, reliable, and accessible disease detection using technology.

---

## 📸 How It Works

1. 🖼️ Users upload an image of a chicken.
2. 🤖 The AI model classifies the image as:

   * Healthy
   * Coccidiosis
   * Salmonella
   * Newcastle Disease
3. ✅ Instant prediction result helps guide timely treatment.

---

## ⚙️ Technologies Used

| Component       | Technology                   |
| --------------- | ---------------------------- |
| Programming     | Python                       |
| Backend         | Flask (Web Framework)        |
| AI/ML Framework | PyTorch                      |
| Frontend        | HTML, CSS, JavaScript        |
| UI Framework    | Bootstrap                    |
| Model Handling  | Downloaded from Hugging Face |

---

## 🌟 Benefits

* 🔍 **Early Disease Detection** – Identify issues before they spread
* 💰 **Cost-Effective** – Reduces dependency on lab testing
* ❤️ **Lower Mortality** – Improve poultry health outcomes
* 🌾 **Agri-AI Showcase** – Bridges AI with real-world farming

---

## 🧠 Project Structure

```
poultry_disease_app/
├── app.py                  # Main Flask app (downloads model from Hugging Face)
├── static/                 # CSS, JS, images
├── templates/              # HTML templates
├── uploads/                # Uploaded images
├── requirements.txt        # Project dependencies
├── .gitignore
└── README.md               # Project overview
```

---

## 🚀 Getting Started

### 📦 Clone the Repo

```bash
git clone https://github.com/Hemanagu/Poultry_Disease_Classification.git
cd Poultry_Disease_Classification
```

### 🔧 Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ⬇️ Model Download

No need to install Git LFS.
The model will be **automatically downloaded from Hugging Face** during app startup via `app.py`.

Ensure internet connectivity when launching the app for the first time.

### ▶️ Run the Application

```bash
python app.py
```

Then open your browser and visit: [http://localhost:5000](http://localhost:5000)

---

## 👤 Author

| Name                | Role                                         |
| ------------------- | -------------------------------------------- |
| **Bharath Chilaka** | 💡 Project Developer, Main Lead & Full-stack |

---

## 👥 Team Members

| Name                         | Role                               |
| ---------------------------- | ---------------------------------- |
| **Bharath Chilaka**          | Project Development & Architecture |
| **Donda Nagamma**            | UI/UX Design & Team Coordination   |
| **Battula BenarjiBabu**      | Project Support                    |
| **Banavath SaiKishore Naik** | Project Support                    |

---

## 📫 Contact

* 📧 Email: [smartinternz44653@gmail.com](mailto:smartinternz44653@gmail.com)
* 📍 Location: Andhra Pradesh, India

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* Hugging Face for model hosting
* PyTorch for AI model development
* Flask for backend development
* Bootstrap for responsive UI
* Farmers & researchers who inspired this application

---
