from stockfish import Stockfish
from gradio_client import Client
from stockfish import Stockfish
from chess_engine import stockfish

# Initialize Stockfish
stockfish = Stockfish(path=r"D:\C-Drive\Programs\stockfish\stockfish-windows-x86-64.exe", parameters={"Skill Level": 10})

def get_ai_move(fen):
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()


def Mistral_LLM(prompt):
    client = Client("hysts/mistral-7b")
    result = client.predict(
        message=[{"role": "user", "content": prompt}],
        param_2=1024,
        param_3=0.6,
        param_4=0.9,
        param_5=50,
        param_6=1.2,
        api_name="/chat"
    )
    return result



def get_move_suggestions(fen):
    stockfish.set_fen_position(fen)
    top_moves = stockfish.get_top_moves(3)
    suggestions = []
    for move in top_moves:
        suggestions.append({
            "move": move["Move"],
            "score": move["Centipawn"] / 100  # Convert centipawns to pawns
        })
    return suggestions


def get_strategy_insights(fen):
    stockfish.set_fen_position(fen)
    evaluation = stockfish.get_evaluation()
    if evaluation["type"] == "mate":
        return f"Mate in {evaluation['value']} moves."
    elif evaluation["type"] == "cp":
        score = evaluation["value"] / 100
        if score > 1:
            return "You have a strong positional advantage."
        elif score < -1:
            return "You are in a difficult position."
        else:
            return "The position is balanced."



def explain_move(move, fen):
    """
    Explain a chess move using both Stockfish evaluation and LLM explanation
    """
    # Get Stockfish evaluation
    stockfish.set_fen_position(fen)
    initial_eval = stockfish.get_evaluation()
    
    stockfish.make_moves_from_current_position([move])
    new_eval = stockfish.get_evaluation()
    
    # Calculate evaluation difference
    eval_diff = (new_eval.get('value', 0) - initial_eval.get('value', 0)) / 100
    stockfish.set_fen_position(fen)
    stockfish.make_moves_from_current_position([move])
    evaluation = stockfish.get_evaluation()
    stockfish.set_fen_position(fen)  # Reset to original position
    return f"The move {move} leads to an evaluation of {evaluation['value']/100} pawns."
