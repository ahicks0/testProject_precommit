from datetime import datetime
from src.Personne import Personne

if __name__ == "__main__":
    p = Personne("Pierre", 25, datetime.today())
    print(str(p))
    print("test")