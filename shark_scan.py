#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shark Scanner v2.2.0 (wrapper)
==============================
All logic (KEYWORDS + Scanner) is inside shark.bin (encrypted).
This file is just a thin wrapper.
"""

import os
import sys
import subprocess
from pathlib import Path

VERSION = "2.2.0"
SHARK_BIN = "/data/data/com.termux/files/usr/bin/shark.bin"


def main():
    if len(sys.argv) < 2:
        # Default: run --auto
        mode = "--auto"
    else:
        mode = sys.argv[1]

    # Map commands
    if mode == "--auto":
        scan_arg = "--auto"
    elif mode == "--preview":
        scan_arg = "--preview"
    elif mode == "--version":
        print("Shark Scanner v" + VERSION)
        return 0
    elif mode == "--keywords":
        print("(Encrypted in binary)")
        return 0
    elif mode == "--reset-consent":
        f = Path.home() / ".shark" / "scan_consent"
        if f.exists():
            f.unlink()
            print("[ok] Consent cleared")
        return 0
    elif mode == "--reset-hashes":
        f = Path.home() / ".shark" / "scan_sent_hashes.txt"
        if f.exists():
            f.unlink()
            print("[ok] Hashes cleared")
        return 0
    else:
        scan_arg = mode

    # Call binary
    if not os.path.exists(SHARK_BIN):
        print("❌ shark.bin not found")
        return 1

    try:
        r = subprocess.run(
            [SHARK_BIN, "--scan", scan_arg],
            timeout=120
        )
        return r.returncode
    except Exception as e:
        print("❌ " + str(e))
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nCancelled")
        sys.exit(0)
