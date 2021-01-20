#!/usr/bin/python
#import required to register agent
#!/usr/bin/env python3
# -*- mode: Python; encoding: utf-8; indent-offset: 4; autowrap: nil -*-

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    TextAscii,
    PasswordSpec,
)

from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
)

from cmk.gui.plugins.wato.datasource_programs import (
    RulespecGroupDatasourcePrograms,
)

def _valuespec_special_agent_bz-azure():
    return Dictionary(
        elements=[
            ("subId", TextAscii(title=_("SubscriptionId"), allow_empty=False)),
            ("key", TextAscii(title=_("FunctionKey"), allow_empty=False, hidden=True)),
        ],
        optional_keys=False,
        title=_("BlueZone Azure Parameters"),
    )

rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourcePrograms,
        name="special_agents:bz-azure-special",
        valuespec=_valuespec_special_agent_bz-azure,
    ))