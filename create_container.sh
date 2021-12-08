#!/bin/bash

sudo docker build . -t postgres_to_csv_image
sudo docker run --name postgres_to_csv -d postgres_to_csv_image

