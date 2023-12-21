# Test unitario 007, comprueba que la base de datos exista.

import os 

print("TU-007: " +  ("PASSED" if os.path.exists("../frutería_app.db") else "NOT PASSED" ))