#! /usr/local/bin/python3
import urllib.parse, taglib
from media_api import getAllTracks


print ("\033[0mChecking media library for tracks whose title matches the filename...")

# Iterate through every track in the media API and try updating its weighting
for track in getAllTracks():
	trackpath = "/medlib/"+urllib.parse.unquote(track['url']).partition('/medlib/')[2]
	filename = trackpath.rpartition('/')[2]
	filetitle = filename.rpartition('.')[0]
	if ('title' not in track['tags']):
		track['tags']['title'] = None
	apititle = track['tags']['title']

	## Ignore any titles which have already been updated to not match the file name
	if (apititle != filetitle):
		continue

	try:
		filemetadata = taglib.File(trackpath)
	except OSError:
		print("Can't find file "+ trackpath +" - Skipping")
		continue

	# Ignore any tracks which don't have a TITLE tag
	if (('TITLE' not in filemetadata.tags) or (len(filemetadata.tags['TITLE']) == 0)):
		continue

	id3title = " & ".join(filemetadata.tags['TITLE'])

	## If the id3 title is empty or the same as the api title, then no need to do an update
	if (id3title == apititle):
		continue

	trackdata = {
		"tags": {
			"title": id3title,
		},
	}
	print("Track ID:"+str(track['trackid'])+" -> "+str(trackdata))