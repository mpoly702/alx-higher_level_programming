#!/bin/bash
# Sends DELETE request to URL as the first arg and displays the body of the response
curl -s "$1" -X DELETE
