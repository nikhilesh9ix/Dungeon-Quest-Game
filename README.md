# ⚔️ Dungeon Quest

An interactive text-based dungeon adventure game built with Streamlit, featuring a dark fantasy theme, puzzles, and treasure hunting!

🎮 **[Play the Game](https://dungeon-quest-game.streamlit.app/)** 🎮

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎮 Game Overview

**Dungeon Quest** is an immersive, browser-based dungeon crawler where you navigate through mysterious chambers, collect items, solve puzzles, and ultimately discover legendary treasure. The game features:

- 🌑 **4 Unique Rooms** with atmospheric descriptions
- 🎒 **Inventory System** to manage collected items
- 🧩 **Puzzle-Solving Mechanics** that require specific items
- 💎 **Victory Condition** - Find the treasure chamber!
- 🎨 **Beautiful Dark Fantasy UI** with custom CSS styling and animations

## ✨ Features

- **Interactive Gameplay**: Navigate using simple button controls
- **Visual Progress Tracking**: Track your journey through the dungeon
- **Dynamic Inventory Management**: Collect and use items to progress
- **Puzzle System**: Solve challenges using items you've collected
- **Atmospheric Design**: Custom fonts, animations, and a medieval theme
- **Responsive UI**: Clean layout with sidebar inventory display
- **Reset Functionality**: Replay the adventure anytime

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/nikhilesh9ix/Dungeon-Quest-Game.git
cd Dungeon-Quest-Game
```

2. **Install required dependencies**
```bash
pip install streamlit
```

### Running the Game

Launch the game with:
```bash
streamlit run DQ2.py
```

The game will automatically open in your default web browser at `http://localhost:8501`

## 🎯 How to Play

### Controls
- **⬅️ GO BACK**: Return to the previous room
- **🚶 GO FORWARD**: Move to the next room (if unlocked)
- **✋ PICK UP**: Collect items in the current room
- **🧩 SOLVE**: Use items from your inventory to solve puzzles
- **🎒 INVENTORY**: View all collected items
- **🔄 RESET GAME**: Start a new adventure

### Gameplay Tips
1. Explore each room thoroughly to find items
2. Collect items before moving forward - you might need them!
3. Some rooms are locked by puzzles that require specific items
4. Check your inventory (sidebar) to see what you've collected
5. Read room descriptions carefully for hints

### Winning the Game
Navigate through all 4 rooms, solve the puzzles, and reach the treasure chamber to win!

## 🏗️ Project Structure

```
Dungeon-Quest-Game/
│
├── DQ2.py              # Main game file with Streamlit app
├── streamlit_app.py    # Alternative entry point
└── README.md           # Project documentation
```

## 🛠️ Technical Details

### Built With
- **[Streamlit](https://streamlit.io/)** - Web application framework
- **Python** - Core programming language

### Key Components

#### Room Class
Manages individual room properties including:
- Description text
- Items available
- Puzzles and solutions
- Navigation links
- Visual emojis

#### Player Class
Handles player inventory and item management:
- Pick up items
- Check inventory
- Item validation

#### Game Logic
- Room navigation system
- Puzzle-solving mechanics
- Win condition checking
- Game state management with `st.session_state`

### Custom Styling
- Medieval-themed fonts (Cinzel, MedievalSharp)
- Gradient backgrounds and glowing effects
- Smooth animations (fade-in, pulse, glow)
- Responsive button designs
- Custom color scheme with gold and orange accents

## 🎨 UI Features

- **Animated Title**: Glowing text effect with gold accents
- **Room Boxes**: Styled containers with border animations
- **Progress Bar**: Visual indicator of game progression
- **Item/Puzzle Indicators**: Color-coded boxes for game elements
- **Sidebar Inventory**: Real-time inventory display
- **Victory Screen**: Celebratory animations and balloons

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Add more rooms and puzzles
- Implement a combat system
- Add sound effects and music
- Create multiple difficulty levels
- Add character customization
- Implement save/load functionality

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Nikhilesh**
- GitHub: [@nikhilesh9ix](https://github.com/nikhilesh9ix)

## 🙏 Acknowledgments

- Streamlit community for the amazing framework
- Google Fonts for medieval-themed typography
- Inspiration from classic text-based adventure games

## 📸 Screenshots

### Game Interface
The main game screen features a dark fantasy theme with atmospheric room descriptions and interactive controls.

### Victory Screen
Upon finding the treasure, players are greeted with a celebration screen complete with animations!

---

**Enjoy your adventure in the Dungeon Quest! ⚔️💎**