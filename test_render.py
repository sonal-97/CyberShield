#!/usr/bin/env python3
"""
Test script to diagnose Render deployment issues
"""
import requests
import json

# Replace with your actual Render URL
RENDER_URL = "https://cybershield-rck1.onrender.com"

def test_endpoint(endpoint, method="GET", files=None):
    """Test a specific endpoint"""
    url = f"{RENDER_URL}{endpoint}"
    print(f"\n🔍 Testing {method} {url}")
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=30)
        elif method == "POST":
            response = requests.post(url, files=files, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Length: {len(response.text)} chars")
        
        # Try to parse as JSON
        try:
            json_data = response.json()
            print(f"JSON Response: {json.dumps(json_data, indent=2)}")
        except:
            print(f"Raw Response: {response.text[:500]}...")
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("🚀 Testing CyberShield AI on Render")
    print("=" * 50)
    
    # Test basic endpoints
    test_endpoint("/")
    test_endpoint("/health")
    test_endpoint("/api/test")
    test_endpoint("/api/model-status")
    
    # Test upload with a small dummy file
    print("\n📤 Testing file upload...")
    dummy_file = {'file': ('test.png', b'fake_image_data', 'image/png')}
    test_endpoint("/upload", method="POST", files=dummy_file)
    test_endpoint("/api/test-upload", method="POST", files=dummy_file)

if __name__ == "__main__":
    main()