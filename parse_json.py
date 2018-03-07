#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
import sys,json
config_files="/home/htsat/TSestuary/caliper/config/cases_config.json"

load_f = open(config_files, 'r')
case_list = json.load(load_f)
for dimension in case_list:
  for i in range(len(case_list[dimension])):
    for tool in case_list[dimension][i]:
      print(tool)
