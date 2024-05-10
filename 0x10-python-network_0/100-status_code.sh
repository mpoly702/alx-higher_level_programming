#!/bin/bash
# Sends request to URL as an arg and displays only the status code of the response
curl -s -w "%{response_code}" -o /dev/null "$1"
