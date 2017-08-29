#!/bin/bash

ffmpeg -i $1 -acodec pcm_u8 -ar 22050 $2
