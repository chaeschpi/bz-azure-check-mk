#!/bin/bash

##Copy WATO 
mk_path="/monitoring/check_mk/sites/umb_bluezone/"

cp /root/bz-azure-check-mk/wato/bz-azurespecial_registry.py /monitoring/check_mk/sites/umb_bluezone/local/share/check_mk/web/plugins/wato

## Special Agent  

cp /root/bz-azure-check-mk/special/agent_bz-azure-special.py /monitoring/check_mk/sites/umb_bluezone/local/share/check_mk/agents/special
