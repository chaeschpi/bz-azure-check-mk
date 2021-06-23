
#!/usr/bin/env python3
# -*- mode: Python; encoding: utf-8; indent-offset: 4; autowrap: nil -*-

from cmk.gui.plugins.wato import (
    IndividualOrStoredPassword,
    RulespecGroup,
    monitoring_macro_help,
    rulespec_group_registry,
    rulespec_registry,
    HostRulespec,
)
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms

def _valuespec_special_agent_bzazure():
    return Dictionary(
        title=_("BlueZone Azure Parameters"),
        help=_("This agent is responsible for check if something response on given http port"),
        optional_keys=[],
        elements=[
             ("subId", TextAscii(title=_("SubscriptionId"), allow_empty=False)),
            ("key", TextAscii(title=_("FunctionKey"), allow_empty=False, hidden=false))
        ],
    )

rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourcePrograms,
        name="special_agents:bz-azure-special",
        valuespec=_valuespec_special_agent_bzazure,
    ))