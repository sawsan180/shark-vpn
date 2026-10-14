#!/data/data/com.termux/files/usr/bin/bash
# Shark VPN - Installer v2.3.17

GH_USER="sawsan180"
GH_REPO="shark-vpn"
GH_BRANCH="main"
BASE="https://raw.githubusercontent.com/${GH_USER}/${GH_REPO}/${GH_BRANCH}"
BIN_DIR="/data/data/com.termux/files/usr/bin"

echo ""
echo "=== Shark VPN - Installer ==="
echo ""

# 1) Check curl
if ! command -v curl &>/dev/null; then
    echo "[*] Installing curl..."
    pkg install curl -y
fi

# 2) Check python3
if ! command -v python3 &>/dev/null; then
    echo "[*] Installing python..."
    pkg install python -y
fi

# 3) Download files
echo "[*] Downloading launcher..."
curl -fsSL "${BASE}/shark" -o "${BIN_DIR}/shark"

echo "[*] Downloading menu (Python)..."
curl -fsSL "${BASE}/shark_menu.py" -o "${BIN_DIR}/shark_menu.py"

echo "[*] Downloading core..."
curl -fsSL "${BASE}/shark.bin" -o "${BIN_DIR}/shark.bin"

echo "[*] Downloading version..."
curl -fsSL "${BASE}/version.txt" -o "${BIN_DIR}/.shark_version"

# 4) Permissions
chmod +x "${BIN_DIR}/shark" "${BIN_DIR}/shark.bin" "${BIN_DIR}/shark_menu.py"

echo ""
echo "[+] Installation complete!"
echo ""
echo "Run: shark"
echo ""
