#!/bin/bash
# Sends JSON POST request to URL as the first arg and displays the body
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
