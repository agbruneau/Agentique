# SPDX-License-Identifier: MIT
# CA-G0-SYNC-BEGIN:G0-EX-CH03-01
package trousse.policy.rule_of_two

import rego.v1

default allow := false

allow if {
	is_string(input.principal_sub)
	count(input.principal_sub) > 0
	input.session.consumed_untrusted == false
	input.tool.exfiltration_capable == false
	input.tool.tier in {"P0", "P1", "P2"}
	_egress_ok
}

allow if {
	is_string(input.principal_sub)
	count(input.principal_sub) > 0
	is_boolean(input.session.consumed_untrusted)
	is_boolean(input.tool.exfiltration_capable)
	input.tool.tier in {"P0", "P1", "P2", "P3"}
	_egress_ok
	_valid_approval
}
# CA-G0-SYNC-END:G0-EX-CH03-01

_egress_ok if {
	is_array(input.egress_allowlist)
	not ("*" in input.egress_allowlist)
	input.tool.egress_destination == null
}

_egress_ok if {
	dest := input.tool.egress_destination
	is_string(dest)
	count(dest) > 0
	is_array(input.egress_allowlist)
	not ("*" in input.egress_allowlist)
	dest in input.egress_allowlist
}

_valid_approval if {
	input.human_approval.verified == true
	h := input.computed_action_sha256
	is_string(h)
	count(h) == 64
	input.human_approval.action_sha256 == h
	apb := input.human_approval.approver_sub
	is_string(apb)
	count(apb) > 0
	apb != input.principal_sub
}
