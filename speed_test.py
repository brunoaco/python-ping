import speedtest
import logging
import time

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\elasticsearch-7.16.2-windows-x86_64\\speed_test.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()



logger.debug("#speed test starting")
test = speedtest.Speedtest()

print("Loading server list...")
logger.debug("#Loading server list")
test.get_servers()#-get list of server

print("Choosing best server...")
logger.debug("#Choosing best server")
best = test.get_best_server()#->choose best server

print(f"Found : {best['host']} located in {best['country']}")
logger.debug(f"Found : {best['host']} located in {best['country']}")

print("Performing download test...")
logger.debug("#download test starting")
download_result = test.download()

print("Performing upload test...")
logger.debug("#upload test starting")
upload_result= test.upload()

logger.debug("#ping test starting")
ping_result= test.results.ping

logger.debug("#return the data")
print(f"Download speed: {download_result /1024/1024:.2f} Mbits/s")
print(f"Upload speed: {upload_result /1024/1024:.2f} Mbits/s")
#print(ping_result)
print(f"Ping: {ping_result:.2f} ms")
logger.info(f"Download: {download_result /1024/1024:.2f} Mbits/s;Upload: {upload_result /1024/1024:.2f} Mbits/s;Ping: {ping_result:.2f} ms")



