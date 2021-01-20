#!/usr/bin/env python3

def agent_myspecal_arguments(params):
    args = []

    args += ["-k", params['key']]
    args += ["-s", params['subId']]

    return args




special_agent_info['myspecial'] = agent_myspecial_arguments