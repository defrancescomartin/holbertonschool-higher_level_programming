#!/bin/bash
# This script is used to calculate the body size of a HTTP request.
curl -s "$1" | wc -c