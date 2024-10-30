import speedtest

print("")
print("Wait a while we are calculating !")

test = speedtest.Speedtest()
download_speed = test.download()
upload_speed = test.upload()

print(f"Download speed : {download_speed / 1000000} MBps")
print(f"Upload speed : {upload_speed / 1000000} MBps")
