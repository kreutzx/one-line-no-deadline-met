import os

# One-line excuse for a missed deadline: the self-reference loop, performed
# in the first person — move the deadline, log it, cite the log as proof.
ENTRY = "I moved the deadline to Friday, logged the move, then cited my own log as proof the deadline had moved — so technically, I met it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
