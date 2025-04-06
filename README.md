# ⏱️ Clock Generator (Date + Time)

This project simulates a digital clock that continuously generates complete date and time sequences using Python generators.
By leveraging generators, the system produces one value at a time in a memory-efficient way, without storing large lists in memory.
This approach is ideal for handling long-running or infinite time streams, and demonstrates how clean, modular design combined with generator-based logic can lead to efficient and elegant code.

## 📂 Project Structure
```
clock_project/
│
├── clock_generator/
│   ├── time_gen.py
│   ├── date_gen.py
│   └── utils.py
│
├── main.py
└── README.md
```

## 🚀 How to Run

```bash
python main.py
```

The screen will update every 1,000,000 iterations (can be changed in the 'main.py' module) with the current generated timestamp starts at 2019 year my default, this parameter can be edited in the 'date_gen.py' module >>'gen_year()' generator function.

## 🧠 Highlights

- Efficient use of Python generators
- Clean modular structure
- Leap year detection
- Formatted output (e.g., `2024/02/29 13:45:07`)
- Console-clearing for a clean, real-time-like display

## 📜 License

MIT License — free to use, modify, and distribute.
