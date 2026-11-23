# SPDX-License-Identifier: MIT
# CA-G0-SYNC-BEGIN:G0-EX-CH03-02
package trousse.policy.camel_taint

import rego.v1

default allow := false

allow if {
	input.control_flow_source == "TRUSTED_PLAN"
	is_boolean(input.args_derived_from_untrusted)
	is_boolean(input.sensitive_args_grounded_against_sor)
	_args_safe
	_a2a_taint_safe
}

_args_safe if input.args_derived_from_untrusted == false
_args_safe if input.sensitive_args_grounded_against_sor == true

_a2a_taint_safe if input.session.consumed_untrusted == false
_a2a_taint_safe if {
	input.session.consumed_untrusted == true
	input.a2a_delegation.enabled == true
	input.a2a_delegation.propagated_consumed_untrusted == true
}
# CA-G0-SYNC-END:G0-EX-CH03-02
