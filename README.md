# 🔐 Password Generator (CLI)

A simple command-line **Password Generator** written in **Python**.  
This tool allows users to generate secure passwords with a custom length and character options such as numbers and symbols. Generated passwords can be saved locally for later reference.

---

## ✨ Features
- Generate passwords with custom length
- Choose whether to include:
  - Numbers (0–9)
  - Symbols (!@#$%^&* etc.)
- Automatically evaluates password strength
- Saves generated passwords locally in a text file
- Works on **Mac, Windows, and Linux**

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Khal3dfx/Password_Generator.git
cd Password_Generator
```
2. Run the program:
```bash
python3 Password_Generator.py
```
3. Follow the on-screen instructions:
- Enter the desired password length
- Choose whether to include numbers and symbols
- The password will be generated and displayed instantly

## ✅ Requirements

- Python 3.x
- No external libraries required (uses Python standard library only)

## 📁 Project Structure

```bash
Password_Generator/
│
├── Password_Generator.py    # Main Python script
├── README.md                # Project documentation
├── .gitignore               # Git ignore rules
└── passwords.txt            # Auto-created (ignored by GitHub)
```

## 🔒 Data & Security Notes

- Generated passwords are stored locally in passwords.txt
- The file is ignored using .gitignore to prevent sensitive data from being uploaded
- No passwords are transmitted or shared online

## 🚀 Future Improvements

- Option to copy password to clipboard
- Stronger password strength evaluation
- Option to exclude similar characters (e.g. l, I, 1, O, 0)
- Password history viewer inside the CLI
- Export passwords to encrypted storage

## 👤 Author

Khaled Fahad Al-Hamad

## 📝 Notes

- This project is intended for educational and personal use
- Designed to practice Python fundamentals such as user input validation, randomness, and file handling

