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
	apititle = track['tags']['title']

	## Ignore any titles which have already been updated to not match the file name
	if (apititle != filetitle):
		continue

	path = "/medlib/"+track['url'].partition('/medlib/')[2]
	filemetadata = taglib.File(path)
	id3title = " & ".join(filemetadata.tags['TITLE'])

	## If the id3 title is empty or the same as the api title, then no need to do an update
	if ((not id3title) or (id3title == apititle)):
		continue

	print(path + "=>" + apititle +  "~~~~~" + id3title)