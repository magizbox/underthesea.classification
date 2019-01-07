#!/usr/bin/env bash

curl -L -o models/default_model.zip "https://www.dropbox.com/s/gztv0dpn3lzan51/models.zip?dl=0"

unzip models/default_model.zip -d models

rm -rf models/default_model.zip