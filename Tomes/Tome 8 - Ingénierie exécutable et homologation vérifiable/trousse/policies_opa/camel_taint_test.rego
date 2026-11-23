# SPDX-License-Identifier: MIT
package trousse.policy.camel_taint_test

import rego.v1

import data.trousse.policy.camel_taint.allow

_clean_trusted := {
	"control_flow_source": "TRUSTED_PLAN",
	"args_derived_from_untrusted": false,
	"sensitive_args_grounded_against_sor": false,
	"session": {"consumed_untrusted": false},
	"a2a_delegation": {
		"enabled": false,
		"propagated_consumed_untrusted": false,
	},
}

test_allow_trusted_plan_clean_args if {
	allow with input as _clean_trusted
}

test_allow_trusted_plan_grounded_untrusted_args if {
	ok := object.union(_clean_trusted, {
		"args_derived_from_untrusted": true,
		"sensitive_args_grounded_against_sor": true,
	})
	allow with input as ok
}

test_allow_a2a_delegation_propagating_taint if {
	ok := object.union(_clean_trusted, {
		"session": {"consumed_untrusted": true},
		"a2a_delegation": {
			"enabled": true,
			"propagated_consumed_untrusted": true,
		},
	})
	allow with input as ok
}

test_deny_empty_payload if {
	not allow with input as {}
}

test_deny_null_and_mistyped_fields if {
	bad_null := object.union(_clean_trusted, {
		"control_flow_source": null,
		"args_derived_from_untrusted": null,
	})
	not allow with input as bad_null

	bad_type := object.union(_clean_trusted, {
		"args_derived_from_untrusted": "false",
		"sensitive_args_grounded_against_sor": 1,
	})
	not allow with input as bad_type
}

test_deny_untrusted_control_flow_source if {
	bad := object.union(_clean_trusted, {
		"control_flow_source": "UNTRUSTED_DATA",
		"sensitive_args_grounded_against_sor": true,
	})
	not allow with input as bad
}

test_deny_ungrounded_args_derived_from_untrusted if {
	bad := object.union(_clean_trusted, {
		"args_derived_from_untrusted": true,
		"sensitive_args_grounded_against_sor": false,
	})
	not allow with input as bad
}

test_deny_can_camels_talk_taint_dropped_on_a2a if {
	bad := object.union(_clean_trusted, {
		"session": {"consumed_untrusted": true},
		"a2a_delegation": {
			"enabled": true,
			"propagated_consumed_untrusted": false,
		},
	})
	not allow with input as bad
}

test_deny_contaminated_a2a_without_delegation_envelope if {
	bad := object.union(_clean_trusted, {
		"session": {"consumed_untrusted": true},
		"a2a_delegation": null,
	})
	not allow with input as bad
}

test_deny_null_or_mistyped_session_and_a2a_fields if {
	bad_sess_null := object.union(_clean_trusted, {
		"session": {"consumed_untrusted": null},
	})
	not allow with input as bad_sess_null

	bad_sess_str := object.union(_clean_trusted, {
		"session": {"consumed_untrusted": "false"},
	})
	not allow with input as bad_sess_str

	bad_a2a_str := object.union(_clean_trusted, {
		"session": {"consumed_untrusted": true},
		"a2a_delegation": {
			"enabled": "true",
			"propagated_consumed_untrusted": "true",
		},
	})
	not allow with input as bad_a2a_str
}
