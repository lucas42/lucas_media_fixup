# lucas_media_fixup
One-off script for fixing up some media metadata.  Finds tracks which haven't correctly imported their name from the ID3 file and defaulted to the filename

## Dependencies

* docker
* docker-compose

## Remote Dependencies

* [lucos_media_metadata_api](https://github.com/lucas42/lucos_media_metadata_api)

## Build-time Dependencies (Installed by Dockerfile)

* [python 3](https://www.python.org/download/releases/3.0/)
* [pipenv](https://github.com/pypa/pipenv)

## Running
`docker-compose up -d --no-build`

## Running locally

Run `pipenv install` to setup

`pipenv run python all-tracks.py`


## Environment Variables
For local development, these should be stored in a .env file

* _**MEDIA_DIRECTORY**_ The directory in which to look for audio files to import
* _**MEDIA_PREFIX**_ Added to the start of each track's local path to form the url for that track
* _**MEDIA_API**_ URL of an instance of [lucos_media_metadata_api](https://github.com/lucas42/lucos_media_metadata_api)
