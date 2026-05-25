import requests
import json
import time

# Flask server ka URL jahan model request accept kar raha hai
API_URL = "http://127.0.0.1:5000/predict"

def send_realtime_log(scenario, metrics):
    print(f"\n[*] Sending Stream: [{scenario}] -> Metrics: {json.dumps(metrics)}")
    try:
        # Flask API par POST request bhej rahe hain
        response = requests.post(API_URL, json=metrics)
        if response.status_code == 200:
            result = response.json()
            print(f"    [Detection System Response]: {result['Risk_Mitigation_Action']}")
        else:
            print(f"    [-] Processing Fault: {response.text}")
    except requests.exceptions.ConnectionError:
        print("    [-] Critical Error: Flask server endpoint is offline! Pehle app.py run karein.")

if __name__ == "__main__":
    print("=== INITIALIZING CYBER THREAT REAL-TIME MONITORING ===")
    
    # 1. Normal User Traffic Simulation
    send_realtime_log("Normal User Browsing", {"packet_size": 320, "failed_logins": 0, "request_frequency": 12})
    time.sleep(2) # 2 second ka gap
    
    # 2. Brute-Force Attack Simulation (High failed logins)
    send_realtime_log("Brute-Force Anomaly", {"packet_size": 64, "failed_logins": 12, "request_frequency": 180})
    time.sleep(2)
    
    # 3. DoS Attack Simulation (High packet size and request frequency)
    send_realtime_log("Volumetric DoS Hit", {"packet_size": 1500, "failed_logins": 0, "request_frequency": 600})