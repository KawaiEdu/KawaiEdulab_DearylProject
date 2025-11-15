# utils.py
def to_int(s):
    try: return int(s)
    except : return None

def menu():
    print("\\n[1]faktorial [2]fib [3]pangkat [0]keluar")