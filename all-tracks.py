#! /usr/local/bin/python3
import urllib.parse, taglib
from media_api import getAllTracks


print ("\033[0mChecking media library for tracks whose title matches the filename...")

# Iterate through every track in the media API and try updating its weighting
for track in getAllTracks():
	filename = track['url'].rpartition('/')[2]
	filetitle = urllib.parse.unquote(filename).rpartition('.')[0]
	if ('title' not in track['tags']):
		track['tags']['title'] = None

	## Ignore any titles which have already been updated to not match the file name
	if (track['tags']['title'] != filetitle):
		continue

	path = "/medlib/"+track['url'].partition('/medlib/')[2]
	print(path + "=>" + track['tags']['title'] +  "~~~~~" + filetitle)
	filemetadata = taglib.File(path)
	print(filetitle + "====" + filemetadata.tags['TITLE'])