#!/usr/bin/env python3
"""
Entry point for CyberShield AI deployment
This file imports the main application for deployment platforms
"""

from malware_detection_fyp.cyber_deploy import app

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)