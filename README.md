# 📝 Python Todo App — Web, CLI, and GUI

A versatile **Todo Application** built with Python, offering **three different interfaces**:
- **Web App** for online access
- **CLI (Command Line Interface)** for terminal lovers
- **GUI (Graphical User Interface)** for desktop users

Manage your tasks your way — all powered by the same backend logic.

---

## 🚀 Features
- Add, view, edit, and delete todos
- Persistent storage (local file or database)
- Same backend logic shared across all interfaces
- Lightweight and beginner-friendly
- Cross-platform support

---

## 📦 Installation
Make sure you have **Python 3.8+** installed.

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/python-todo-app.git
cd python-todo-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🖥 Usage

### 1️⃣ CLI Mode
```bash
python todo_cli.py
```
- Use simple commands to add, list, mark, or delete todos.

---

### 2️⃣ GUI Mode
```bash
python todo_gui.py
```
- Opens a desktop window to manage tasks with buttons and forms.

---

### 3️⃣ Web Mode
```bash
python todo_web.py
```
- Starts a local server (default: `http://127.0.0.1:5000`)
- Access your todos in a browser.

---

## 📂 File Structure
```
📁 python-todo-app
 ├── todo_cli.py       # CLI interface
 ├── todo_gui.py       # GUI interface
 ├── todo_web.py       # Web interface
 ├── todo_core.py      # Shared backend logic
 ├── requirements.txt  # Dependencies
 ├── README.md         # Documentation
 └── data.json         # Todo storage file
```

---

## 🧰 Dependencies
- **Flask** — For the web app
- **tkinter** — For the GUI
- **colorama** — For CLI text formatting
- **json** (built-in) — For data storage

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 💡 How It Works
All three interfaces use the same backend (`todo_core.py`) for managing tasks.  
This ensures consistent behavior regardless of the interface you choose.

---

## 📜 License
This project is licensed under the MIT License — free to use and modify.

---

## 🤝 Contributing
Pull requests are welcome!  
For major changes, open an issue to discuss your ideas.

---

## ⭐ Show Your Support
If you like this project, give it a ⭐ on GitHub to help it grow!
