import requests
import os

rows = ""

with open("urls.txt", "r") as f:
    rows = f.readlines()

total = 0
for url in rows:
	try:
		# try to download the image
		r = requests.get(url.strip(), timeout=7)
		# save the image to disk
		p = os.path.sep.join(["C:\\PythonPrograms\\DeerDetect\\imgs", "{}.jpg".format(str(total).zfill(8))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()
		# update the counter
		print("[INFO] downloaded: {}".format(p))
		total += 1
	# handle if any exceptions are thrown during the download process
	except:
		print("[INFO] error downloading {}...skipping".format(p))