def verifier_integrite(T):
    for i in range(len(T)-1):
        if T[i] != T[i+1]:
            return False
    print("La chaîne est intègre.")
    return True  