import json, sys, os, requests
from datetime import datetime

if not os.environ.get("MEDIA_API"):
	sys.exit("\033[91mMEDIA_API not set\033[0m")
apiurl = os.environ.get("MEDIA_API")
if (apiurl.endswith("/")):
	sys.exit("\033[91mDon't include a trailing slash in the API url\033[0m")

class getAllTracks:
	"""Returns an iterator covering all tracks in the media API

	Gets tracks one page at a time and returns them track-by-track
	When out of tracks, fetches the next page and returns those track-by-track
	Finishes when out of pages
	"""
	def __init__(self):
		self.page = 0
		self.tracks = []

	def __iter__(self):
		return self

	def __next__(self):

		# While there's still tracks left in the page of tracks, use the next of those
		if len(self.tracks) > 0:
			return self.tracks.pop(0)

		# If there's none left, fetch the next page
		self.page += 1
		self.tracks = requests.get(apiurl+"/tracks/?page="+str(self.page)).json()

		if len(self.tracks) > 0:
			return self.tracks.pop(0)

		# If there's no tracks in the next page, then all tracks have been returned
		else:
			raise StopIteration

def updateTrack(trackid, data):
	trackresult = requests.patch(apiurl+"/tracks/"+str(trackid), data=json.dumps(data), allow_redirects=False)
	if trackresult.ok:
		print(str(trackid) + " => "+trackresult.headers.get("Track-Action"))
	else:
		log("HTTP Status code "+str(trackresult.status_code)+" returned by API: " +  trackresult.text.rstrip() + " <" + str(trackid) + ">", error=True)