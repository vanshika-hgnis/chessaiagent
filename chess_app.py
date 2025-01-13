import streamlit as st
import streamlit.components.v1 as components
import chess
import chess.svg
from stockfish import Stockfish
import pandas as pd

def get_board_html():
    return """
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>
    </head>
    <body>
        <div id="board" style="width: 500px"></div>
        <script>
            var board = null;
            var game = new Chess();
            
            function onDragStart(source, piece, position, orientation) {
                if (game.game_over()) return false;
                if (piece.search(/^b/) !== -1) return false;
            }
            
            function onDrop(source, target) {
                var move = game.move({
                    from: source,
                    to: target,
                    promotion: 'q'
                });
                
                if (move === null) return 'snapback';
                
                window.parent.document.dispatchEvent(new CustomEvent('chess_move', {
                    detail: { move: move }
                }));
            }
            
            function onSnapEnd() {
                board.position(game.fen());
            }
            
            var config = {
                draggable: true,
                position: 'start',
                onDragStart: onDragStart,
                onDrop: onDrop,
                onSnapEnd: onSnapEnd
            };
            
            board = Chessboard('board', config);
        </script>
    </body>
    """

def main():
    st.set_page_config(layout="wide")
    st.title("Interactive Chess Training Platform")

    # Initialize session state
    if 'board' not in st.session_state:
        st.session_state.board = chess.Board()
    if 'assistant' not in st.session_state:
        st.session_state.assistant = ChessTeachingAssistant(
            r"path/to/your/stockfish.exe"  # Update this path
        )

    # Layout
    col1, col2 = st.columns([2, 1])

    with col1:
        # Embed the chessboard
        components.html(get_board_html(), height=600)

    with col2:
        st.subheader("Game Controls")
        if st.button("New Game"):
            st.session_state.board = chess.Board()
            st.experimental_rerun()

        st.subheader("Analysis")
        if st.button("Analyze Position"):
            analysis = st.session_state.assistant.analyze_position()
            st.write("Evaluation:", analysis['evaluation'])
            st.write("Best Moves:", analysis['best_moves'])

        # Interactive learning mode
        st.subheader("Learning Mode")
        if st.checkbox("Enable Interactive Learning"):
            st.write("Make a move to see suggestions")

if __name__ == "__main__":
    main()