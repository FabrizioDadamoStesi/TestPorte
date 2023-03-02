import tkinter as tk
import socket

def port_scan(ip_address, port):
    """
    Questa funzione esegue la scansione di una porta su un determinato indirizzo IP
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            return True
        else:
            return False
    except:
        return False

def network_scan(ip_address):
    """
    Questa funzione esegue la scansione di tutte le porte aperte su un determinato indirizzo IP
    """
    open_ports = []
    for port in range(1, 10000):
        if port_scan(ip_address, port):
            open_ports.append(port)
    return open_ports

def run_scan():
    """
    Questa funzione esegue la scansione della rete aziendale e aggiorna l'interfaccia grafica con i risultati
    """
    selected_ips = ip_entry.get().split(',')  # ottieni l'elenco degli indirizzi IP selezionati dall'interfaccia grafica
    results_text.delete(1.0, tk.END)  # cancella il testo precedente
    for ip_address in selected_ips:
        open_ports = network_scan(ip_address.strip())
        if len(open_ports) > 0:
            results_text.insert(tk.END, f"Porte aperte su {ip_address}: {open_ports}\n")
        else:
            results_text.insert(tk.END, f"Nessuna porta aperta su {ip_address}\n")

# creazione della finestra principale dell'interfaccia grafica
window = tk.Tk()
window.title("Programma di test della sicurezza della rete aziendale")

# creazione dei widget per la finestra
ip_label = tk.Label(window, text="Indirizzi IP da esaminare (separati da virgola):")
ip_label.pack()

ip_entry = tk.Entry(window)
ip_entry.pack()

scan_button = tk.Button(window, text="Esegui la scansione", command=run_scan)
scan_button.pack()

results_text = tk.Text(window)
results_text.pack()

# avvio dell'interfaccia grafica
window.mainloop()
