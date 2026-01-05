import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="🏰 Dungeon Quest",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark dungeon theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=MedievalSharp&family=Cinzel:wght@400;700&display=swap');
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #e8e8e8;
    }
    
    /* Title styling */
    h1 {
        font-family: 'Cinzel', serif;
        color: #ffd700 !important;
        text-align: center;
        text-shadow: 0 0 20px #ff6b35, 0 0 30px #ff6b35;
        font-size: 3.5em !important;
        margin-bottom: 20px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #ff6b35, 0 0 20px #ff6b35, 0 0 30px #ff6b35; }
        to { text-shadow: 0 0 20px #ff6b35, 0 0 30px #ff6b35, 0 0 40px #ff6b35, 0 0 50px #ff6b35; }
    }
    
    /* Room description box */
    .room-box {
        background: linear-gradient(145deg, #2c2c3e 0%, #1a1a2e 100%);
        border: 3px solid #ffd700;
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.3), inset 0 0 20px rgba(0, 0, 0, 0.5);
        font-family: 'MedievalSharp', cursive;
        font-size: 1.3em;
        color: #e8e8e8;
        text-align: center;
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Item and puzzle boxes */
    .item-box, .puzzle-box {
        background: linear-gradient(145deg, #ff6b35 0%, #ff8c42 100%);
        border: 2px solid #ffd700;
        border-radius: 10px;
        padding: 15px;
        margin: 15px 0;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(255, 107, 53, 0.4);
        animation: pulse 2s infinite;
    }
    
    .puzzle-box {
        background: linear-gradient(145deg, #b721ff 0%, #8b00ff 100%);
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.03); }
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(145deg, #ff6b35 0%, #f7931e 100%);
        color: white;
        border: 2px solid #ffd700;
        border-radius: 10px;
        padding: 15px 30px;
        font-size: 1.2em;
        font-family: 'Cinzel', serif;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 107, 53, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(145deg, #f7931e 0%, #ff6b35 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.6);
    }
    
    /* Inventory sidebar */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #0f3460 100%);
        border-right: 3px solid #ffd700;
    }
    
    /* Success message */
    .success-box {
        background: linear-gradient(145deg, #28a745 0%, #20c997 100%);
        border: 3px solid #ffd700;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        font-size: 1.5em;
        animation: celebrate 1s ease-in-out;
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.8);
    }
    
    @keyframes celebrate {
        0%, 100% { transform: scale(1) rotate(0deg); }
        25% { transform: scale(1.1) rotate(-5deg); }
        75% { transform: scale(1.1) rotate(5deg); }
    }
    
    /* Message box */
    .message-box {
        background: rgba(255, 107, 53, 0.2);
        border-left: 5px solid #ff6b35;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
        font-size: 1.1em;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* Inventory items */
    .inventory-item {
        background: linear-gradient(145deg, #ffd700 0%, #ffed4e 100%);
        color: #1a1a2e;
        border-radius: 8px;
        padding: 10px;
        margin: 5px 0;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 3px 10px rgba(255, 215, 0, 0.5);
    }
    
    /* Progress indicator */
    .progress-bar {
        background: linear-gradient(90deg, #ff6b35 0%, #ffd700 100%);
        height: 8px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

class Room:
    def __init__(self, description, item=None, puzzle=None, solution=None, emoji="🏰"):
        self.description = description
        self.item = item
        self.puzzle = puzzle
        self.solution = solution
        self.next_room = None
        self.previous_room = None
        self.emoji = emoji

class Player:
    def __init__(self):
        self.inventory = []
    
    def pick_up_item(self, item):
        if item:
            self.inventory.append(item)
            return f"You picked up: {item}"
        return "There's nothing to pick up here."
    
    def has_item(self, item):
        return item in self.inventory
    
    def show_inventory(self):
        return "Your inventory: " + ", ".join(self.inventory) if self.inventory else "Your inventory is empty."

# Set up rooms with emojis
room1 = Room("You stand at the entrance of a dark, ominous cave. Ancient runes glow faintly on the stone walls, and a cold wind whispers through the darkness...", item="torch", emoji="🌑")
room2 = Room("You enter a narrow hallway covered with strange mystical markings. The air is thick with mystery, and shadows dance on the walls.", item="key", emoji="🔮")
room3 = Room("A massive iron door blocks your path. Its lock gleams in the torchlight, waiting for the right key...", puzzle="ancient door lock", solution="key", emoji="🚪")
room4 = Room("✨ You've discovered the legendary treasure chamber! Gold coins, precious gems, and ancient artifacts fill the room. You are victorious! ✨", item="treasure", emoji="💎")

# Link rooms
room1.next_room = room2
room2.previous_room = room1
room2.next_room = room3
room3.previous_room = room2
room3.next_room = room4
room4.previous_room = room3

# Initialize Streamlit session state
if "current_room" not in st.session_state:
    st.session_state.current_room = room1
if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "message" not in st.session_state:
    st.session_state.message = ""
if "room_number" not in st.session_state:
    st.session_state.room_number = 1

# Game functions
def go_forward():
    if st.session_state.current_room.next_room:
        # Check if puzzle is solved
        if st.session_state.current_room.puzzle and st.session_state.current_room.solution not in st.session_state.inventory:
            st.session_state.message = "⚠️ The path is blocked! You need something to solve the puzzle here before moving forward."
        else:
            st.session_state.current_room = st.session_state.current_room.next_room
            st.session_state.room_number += 1
            st.session_state.message = "🚶 You venture deeper into the dungeon..."
    else:
        st.session_state.message = "🚫 There's no path forward from here."

def go_back():
    if st.session_state.current_room.previous_room:
        st.session_state.current_room = st.session_state.current_room.previous_room
        st.session_state.room_number -= 1
        st.session_state.message = "↩️ You backtrack carefully..."
    else:
        st.session_state.message = "🚫 You can't go back from the entrance."

def pick_up_item():
    if st.session_state.current_room.item and st.session_state.current_room.item not in st.session_state.inventory:
        st.session_state.inventory.append(st.session_state.current_room.item)
        st.session_state.message = f"✅ You picked up: {st.session_state.current_room.item.upper()}!"
    else:
        st.session_state.message = "❌ There is nothing to pick up here."

def solve_puzzle():
    if st.session_state.current_room.puzzle:
        if st.session_state.current_room.solution in st.session_state.inventory:
            st.session_state.message = f"🎉 You use the {st.session_state.current_room.solution.upper()} to solve the puzzle! The way is now clear!"
            st.session_state.current_room.puzzle = None  # Puzzle solved
        else:
            st.session_state.message = "🔒 You don't have the item needed to solve this puzzle."
    else:
        st.session_state.message = "ℹ️ There is no puzzle to solve here."

def show_inventory():
    if st.session_state.inventory:
        st.session_state.message = "🎒 Your inventory: " + ", ".join([item.upper() for item in st.session_state.inventory])
    else:
        st.session_state.message = "🎒 Your inventory is empty."

def reset_game():
    st.session_state.current_room = room1
    st.session_state.inventory = []
    st.session_state.message = "🔄 Game reset! Your adventure begins anew..."
    st.session_state.room_number = 1
    # Reset room3 puzzle
    room3.puzzle = "ancient door lock"

# Game interface
st.markdown("<h1>⚔️ DUNGEON QUEST ⚔️</h1>", unsafe_allow_html=True)

# Progress bar
progress = st.session_state.room_number / 4
st.markdown(f'<div class="progress-bar" style="width: {progress * 100}%"></div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #ffd700; font-size: 1.2em;'>🗺️ Room {st.session_state.room_number} of 4</p>", unsafe_allow_html=True)

# Main game area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Room description with emoji
    st.markdown(f"""
        <div class="room-box">
            <div style="font-size: 3em; margin-bottom: 15px;">{st.session_state.current_room.emoji}</div>
            <div>{st.session_state.current_room.description}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Show available item if any
    if st.session_state.current_room.item and st.session_state.current_room.item not in st.session_state.inventory:
        item_emoji = {"torch": "🔦", "key": "🗝️", "treasure": "💰"}.get(st.session_state.current_room.item, "📦")
        st.markdown(f"""
            <div class="item-box">
                {item_emoji} You spot an item here: <strong>{st.session_state.current_room.item.upper()}</strong> {item_emoji}
            </div>
        """, unsafe_allow_html=True)
    
    # Show puzzle if any
    if st.session_state.current_room.puzzle and st.session_state.current_room.solution not in st.session_state.inventory:
        st.markdown(f"""
            <div class="puzzle-box">
                🧩 Puzzle detected: <strong>{st.session_state.current_room.puzzle.upper()}</strong> 🧩
            </div>
        """, unsafe_allow_html=True)

# Sidebar for inventory and controls
with st.sidebar:
    st.markdown("<h2 style='color: #ffd700; text-align: center; font-family: Cinzel;'>🎒 INVENTORY</h2>", unsafe_allow_html=True)
    
    if st.session_state.inventory:
        for item in st.session_state.inventory:
            item_emoji = {"torch": "🔦", "key": "🗝️", "treasure": "💰"}.get(item, "📦")
            st.markdown(f"""
                <div class="inventory-item">
                    {item_emoji} {item.upper()}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<p style='text-align: center; color: #888;'>Empty</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h3 style='color: #ffd700; text-align: center; font-family: Cinzel;'>📜 GAME INFO</h3>", unsafe_allow_html=True)
    st.info("🎮 Navigate through the dungeon\n\n🔍 Collect items\n\n🧩 Solve puzzles\n\n💎 Find the treasure!")
    
    st.markdown("---")
    if st.button("🔄 RESET GAME", key="reset"):
        reset_game()
        st.rerun()

# Action buttons in centered layout
st.markdown("<br>", unsafe_allow_html=True)
button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)

with button_col1:
    if st.button("⬅️ GO BACK", key="back"):
        go_back()
        st.rerun()

with button_col2:
    if st.button("🚶 GO FORWARD", key="forward"):
        go_forward()
        st.rerun()

with button_col3:
    if st.button("✋ PICK UP", key="pickup"):
        pick_up_item()
        st.rerun()

with button_col4:
    if st.button("🧩 SOLVE", key="solve"):
        solve_puzzle()
        st.rerun()

with button_col5:
    if st.button("🎒 INVENTORY", key="inv"):
        show_inventory()
        st.rerun()

# Display messages
if st.session_state.message:
    st.markdown(f"""
        <div class="message-box">
            {st.session_state.message}
        </div>
    """, unsafe_allow_html=True)

# Check for win condition
if st.session_state.current_room == room4:
    st.markdown("""
        <div class="success-box">
            <div style="font-size: 3em;">🏆</div>
            <div style="font-size: 2em; margin: 15px 0;">CONGRATULATIONS!</div>
            <div>You've found the legendary treasure and conquered the dungeon!</div>
            <div style="font-size: 3em; margin-top: 15px;">💎✨🎉</div>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
    st.markdown("<p style='text-align: center; margin-top: 20px;'>Click RESET GAME to play again!</p>", unsafe_allow_html=True)
