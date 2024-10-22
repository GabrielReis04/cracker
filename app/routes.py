from flask import Blueprint, jsonify
from .utils import scan_networks, capture_handshake, reaver_attack, pixie_attack

main = Blueprint('main', __name__)

@main.route('/scan', methods=['GET'])
def scan():
    """Escaneia redes Wi-Fi usando airodump-ng."""
    networks = scan_networks()
    return jsonify(networks)

@main.route('/capture-handshake/<bssid>', methods=['POST'])
def capture(bssid):
    """Captura o handshake de uma rede específica."""
    success = capture_handshake(bssid)
    return jsonify({"status": "success" if success else "failure"})

@main.route('/reaver-attack/<bssid>', methods=['POST'])
def reaver(bssid):
    """Executa o ataque WPS usando Reaver."""
    success = reaver_attack(bssid)
    return jsonify({"status": "success" if success else "failure"})

@main.route('/pixie-attack/<bssid>', methods=['POST'])
def pixie(bssid):
    """Executa o ataque Pixie Dust."""
    success = pixie_attack(bssid)
    return jsonify({"status": "success" if success else "failure"})
