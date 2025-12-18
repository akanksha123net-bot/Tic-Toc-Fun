import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮")

st.title("🎮 Tic Tac Toe")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.player = "X"

def check_winner():
    b = st.session_state.board
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for i,j,k in wins:
        if b[i] and b[i] == b[j] == b[k]:
            return b[i]
    if "" not in b:
        return "Draw"
    return None

winner = check_winner()

cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i):
            if not st.session_state.board[i] and not winner:
                st.session_state.board[i] = st.session_state.player
                st.session_state.player = "O" if st.session_state.player == "X" else "X"

if winner:
    if winner == "Draw":
        st.success("It's a Draw!")
    else:
        st.success(f"🎉 Player {winner} wins!")

if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.player = "X"

