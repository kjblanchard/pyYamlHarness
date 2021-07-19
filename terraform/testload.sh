#!/bin/bash
for i in {0..10000..1}
do
   curl -s kubernetes.supergoon.com:1337 > /dev/null
done
