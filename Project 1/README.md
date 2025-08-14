# 🐍💧🔫 Snake, Water, Gun Game (Python)

A simple Python game where you play **Snake, Water, Gun** against the computer.

---

## 📜 Rules
- **Snake (s)** drinks **Water (w)** → Snake wins 🐍🏆
- **Water (w)** douses **Gun (g)** → Water wins 💧🏆
- **Gun (g)** kills **Snake (s)** → Gun wins 🔫🏆
- If both choose the same → Draw ⚖️

---

## 🛠 Code Explanation
1. **Random computer choice**  
   ```python
   computer = random.choice([-1, 0, 1])


1 = Snake 🐍

-1 = Water 💧

0 = Gun 🔫


2. User input → Converted into numeric form for easy comparison


    youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}



3. Compare choices → Decide winner based on game rules.

4. Output choices & result → Printed using f-strings.






🔄 Dry Run

Example Input:

Enter your choice: s


Step-by-step:

Suppose computer chooses -1 (Water)

You choose "s" → converted to 1 (Snake)

if computer == you: → False

if computer == -1 and you == 1: → True → "You win!"

Output:

You chose Snake
Computer chose Water
You win!

▶️ How to Run
python main.py


Enter:

s → Snake 🐍

w → Water 💧

g → Gun 🔫

📌 Sample Outputs
You chose Snake
Computer chose Water
You win!

You chose Gun
Computer chose Snake
You win!

You chose Water
Computer chose Gun
You win!

📂 Project Structure
📦 SnakeWaterGun
 ┣ 📜 main.py      # Game code
 ┗ 📜 README.md    # Documentation


💡 Perfect mini-project for Python beginners to practice conditionals and random module usage.


---

If you want, I can also **add ASCII art for Snake, Water, and Gun** in the README to
