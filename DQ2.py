import streamlit as st

class Room:
    def __init__(self, description, item=None, puzzle=None, solution=None):
        self.description = description
        self.item = item
        self.puzzle = puzzle
        self.solution = solution
        self.next_room = None
        self.previous_room = None

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

# Set up rooms
room1 = Room("You are at the entrance of a dark cave.", item="torch")
room2 = Room("You enter a narrow hallway with strange markings.")
room3 = Room("A locked door blocks your path.", puzzle="door lock", solution="key")
room4 = Room("A treasure room filled with gold and jewels!", item="treasure")

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

# Game functions
def go_forward():
    if st.session_state.current_room.next_room:
        # Check if puzzle is solved
        if st.session_state.current_room.puzzle and st.session_state.current_room.solution not in st.session_state.inventory:
            st.session_state.message = "You need something to solve the puzzle here before moving forward."
        else:
            st.session_state.current_room = st.session_state.current_room.next_room
            st.session_state.message = ""
    else:
        st.session_state.message = "You can't go forward."

def go_back():
    if st.session_state.current_room.previous_room:
        st.session_state.current_room = st.session_state.current_room.previous_room
        st.session_state.message = ""
    else:
        st.session_state.message = "You can't go back."

def pick_up_item():
    if st.session_state.current_room.item and st.session_state.current_room.item not in st.session_state.inventory:
        st.session_state.inventory.append(st.session_state.current_room.item)
        st.session_state.message = f"You picked up: {st.session_state.current_room.item}"
    else:
        st.session_state.message = "There is nothing to pick up here."

def solve_puzzle():
    if st.session_state.current_room.puzzle:
        if st.session_state.current_room.solution in st.session_state.inventory:
            st.session_state.message = f"You use the {st.session_state.current_room.solution} to solve the puzzle!"
            st.session_state.current_room.puzzle = None  # Puzzle solved
        else:
            st.session_state.message = "You don't have the item needed to solve this puzzle."
    else:
        st.session_state.message = "There is no puzzle to solve here."

def show_inventory():
    st.session_state.message = "Inventory: " + ", ".join(st.session_state.inventory) if st.session_state.inventory else "Your inventory is empty."

# Game interface
st.title("Linked List Adventure Game")
st.write(st.session_state.current_room.description)

# Show available item if any
if st.session_state.current_room.item and st.session_state.current_room.item not in st.session_state.inventory:
    st.write(f"You see an item here: {st.session_state.current_room.item}")

# Show puzzle if any
if st.session_state.current_room.puzzle and st.session_state.current_room.solution not in st.session_state.inventory:
    st.write(f"There is a puzzle here: {st.session_state.current_room.puzzle}")

# Action buttons
if st.button("Go Forward"):
    go_forward()

if st.button("Go Back"):
    go_back()

if st.button("Pick Up Item"):
    pick_up_item()

if st.button("Solve Puzzle"):
    solve_puzzle()

if st.button("Inventory"):
    show_inventory()

# Display messages
if "message" in st.session_state and st.session_state.message:
    st.write(st.session_state.message)

# Check for win condition
if st.session_state.current_room == room4:
    st.success("Congratulations! You've found the treasure and won the game!")
    st.write("Thank you for playing Linked List Adventure!")
    st.stop()  # Stops further execution when the game is won
