import threading

# Função que será executada por cada thread
def imprimir_numeros():
    for i in range(1, 6):
        print(f"Thread {threading.current_thread().name}: {i}")

# Criando duas threads
thread1 = threading.Thread(target=imprimir_numeros, name="Thread 1")
thread2 = threading.Thread(target=imprimir_numeros, name="Thread 2")

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando que ambas as threads terminem
thread1.join()
thread2.join()

print("Concluido")
