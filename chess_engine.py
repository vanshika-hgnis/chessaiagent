from stockfish import Stockfish

# Use raw string (r prefix) or forward slashes for the path
stockfish = Stockfish(path=r"D:\C-Drive\Programs\stockfish\stockfish-windows-x86-64.exe")
# OR
# stockfish = Stockfish(path="D:/C-Drive/Programs/stockfish_14_win_x64_avx2/stockfish_14_x64_avx2.exe")

# Rest of your code remains the same
stockfish.set_position([])
best_move = stockfish.get_best_move()
print(f"Best move: {best_move}")

stockfish.set_position(["e2e4", "e7e5"])
print(f"Next best move: {stockfish.get_best_move()}")

evaluation = stockfish.get_evaluation()
print(f"Evaluation: {evaluation}")