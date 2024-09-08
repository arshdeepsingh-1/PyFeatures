import speedtest #pip install speedtest-cli

def test_internet_speed():
    # Create an instance of Speedtest
    st = speedtest.Speedtest()

    # Get the best server based on ping
    st.get_best_server()
    
    # Measure download speed (in bits per second)
    download_speed = st.download()
    
    # Measure upload speed (in bits per second)
    upload_speed = st.upload()
    
    # Measure ping (latency in milliseconds)
    ping = st.results.ping
    
    # Convert speeds from bits per second to Mbps for easier readability
    download_speed_mbps = download_speed / (1024 * 1024)
    upload_speed_mbps = upload_speed / (1024 * 1024)
    
    # Print the results
    print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")
    print(f"Ping: {ping} ms")

# Run the speed test
test_internet_speed()
