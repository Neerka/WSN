import numpy as np

# Parametry algorytmu
c = 0.5  # Współczynnik uczenia
epsilon = 1e-4  # Kryterium stopu
beta = 1.0  # Parametr funkcji sigmoidalnej
N = 3.0  # Zakres losowania wag

# Funkcja aktywacji sigmoid z parametrem beta
def sigmoid(x):
    return 1 / (1 + np.exp(-beta * x))

def sigmoid_derivative(x):
    return beta * x * (1 - x)

# Dane treningowe
inputs = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]])
targets = np.array([[0], [1], [1], [0]])

# Inicjalizacja wag
np.random.seed(2137)
w_old = np.random.uniform(-N, N, (2, 3))  # Wagi wejście -> warstwa ukryta
s_old = np.random.uniform(-N, N, (3, 1))  # Wagi warstwa ukryta -> wyjście
print(f'Początkowe w: {w_old}')
print(f'Początkowe s: {s_old}')

# Algorytm gradientowy
t1 = 0
while True:
    t1 += 1
    
    # Forward pass
    hidden_input = np.dot(inputs, w_old.T)
    hidden_output = sigmoid(hidden_input)  # Warstwa ukryta
    hidden_output = np.hstack([hidden_output, np.ones((hidden_output.shape[0], 1))])  # Bias w warstwie ukrytej
    final_input = np.dot(hidden_output, s_old)
    final_output = sigmoid(final_input)  # Warstwa wyjściowa
    
    # Obliczanie gradientów
    error = final_output - targets
    DE_s = np.dot(hidden_output.T, error * sigmoid_derivative(final_output))
    hidden_error = np.dot(error * sigmoid_derivative(final_output), s_old.T) * sigmoid_derivative(hidden_output)
    DE_w = np.dot(hidden_error[:, :-1].T, inputs)
    
    # Aktualizacja wag
    s_new = s_old - c * DE_s
    w_new = w_old - c * DE_w
    
    # Kryterium stopu
    if np.max(np.abs(s_new - s_old)) < epsilon or np.max(np.abs(w_new - w_old)) < epsilon:
        break
    
    s_old = s_new
    w_old = w_new

# Wyniki
print(f"Liczba iteracji: {t1}")
print(f'Końcowe w: {w_old}')
print(f'Końcowe s: {s_old}')
print("Testowanie bramki XOR:")
for i in range(4):
    hidden_output = sigmoid(np.dot(inputs[i], w_old.T))
    hidden_output = np.append(hidden_output, 1)  # Bias w warstwie ukrytej
    final_output = sigmoid(np.dot(hidden_output, s_old))
    print(f"Wejście: {inputs[i][:2]}, Przewidywane wyjście: {final_output[0]:.4f}, Oczekiwane: {targets[i][0]}")