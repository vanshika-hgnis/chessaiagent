from gradio_client import Client
from stockfish import Stockfish
from chess_engine import stockfish
client = Client("hysts/mistral-7b")





def explain_move(move,position_fen):
    prompt = f"""
    Explain why the move {move} is a strong move in this chess position: {position_fen}.
    Provide an explanation in simple terms suitable for a beginner.
    """
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

fen_position = stockfish.get_fen_position()
best_move = stockfish.get_best_move()
explanation = explain_move(best_move, fen_position)
print(f"Move Explanation: {explanation}")