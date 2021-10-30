#!/bin/sh
curl $1 -s | grep http | cut -f2 -d \"
