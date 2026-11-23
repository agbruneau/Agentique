# SPDX-License-Identifier: MIT
package trousse.policy.sandbox_test

import rego.v1

import data.trousse.policy.sandbox.allow

_valid_none := {
	"sandbox_id": "sbx-01",
	"network": {
		"mode": "none",
		"allowlist": [],
		"imds_blocked": true,
		"special_iana_blocked": true,
	},
	"env_secrets": [],
	"read_only_root": true,
	"allow_shell": false,
	"timeouts": {"tool_s": 30, "loop_s": 1200, "lifetime_s": 3600},
}

test_allow_isolated_none_network_at_exact_bounds if {
	allow with input as _valid_none
}

test_allow_explicit_allowlist_without_wildcard if {
	ok := object.union(_valid_none, {
		"network": {
			"mode": "allowlist",
			"allowlist": ["erp.ent.ca", "catalogue.ent.ca"],
			"imds_blocked": true,
			"special_iana_blocked": true,
		},
		"timeouts": {"tool_s": 15, "loop_s": 600, "lifetime_s": 1800},
	})
	allow with input as ok
}

test_deny_empty_payload if {
	not allow with input as {}
}

test_deny_null_and_mistyped_fields if {
	bad_null := object.union(_valid_none, {
		"env_secrets": null,
		"read_only_root": null,
	})
	not allow with input as bad_null

	bad_type := object.union(_valid_none, {
		"read_only_root": "true",
		"timeouts": {"tool_s": "30", "loop_s": 1200, "lifetime_s": 3600},
	})
	not allow with input as bad_type
}

test_deny_imds_not_blocked if {
	bad := object.union(_valid_none, {"network": {
		"mode": "none",
		"allowlist": [],
		"imds_blocked": false,
		"special_iana_blocked": true,
	}})
	not allow with input as bad
}

test_deny_special_iana_not_blocked if {
	bad := object.union(_valid_none, {"network": {
		"mode": "none",
		"allowlist": [],
		"imds_blocked": true,
		"special_iana_blocked": false,
	}})
	not allow with input as bad
}

test_deny_env_secrets_non_empty if {
	bad := object.union(_valid_none, {"env_secrets": ["API_KEY"]})
	not allow with input as bad
}

test_deny_writable_root_or_shell_enabled if {
	bad_root := object.union(_valid_none, {"read_only_root": false})
	not allow with input as bad_root

	bad_shell := object.union(_valid_none, {"allow_shell": true})
	not allow with input as bad_shell
}

test_deny_wildcard_in_allowlist if {
	bad_star := object.union(_valid_none, {"network": {
		"mode": "allowlist",
		"allowlist": ["*"],
		"imds_blocked": true,
		"special_iana_blocked": true,
	}})
	not allow with input as bad_star

	bad_glob := object.union(_valid_none, {"network": {
		"mode": "allowlist",
		"allowlist": ["*.ent.ca"],
		"imds_blocked": true,
		"special_iana_blocked": true,
	}})
	not allow with input as bad_glob
}

test_deny_timeouts_out_of_bounds if {
	bad_tool := object.union(_valid_none, {
		"timeouts": {"tool_s": 31, "loop_s": 1200, "lifetime_s": 3600},
	})
	not allow with input as bad_tool

	bad_loop := object.union(_valid_none, {
		"timeouts": {"tool_s": 30, "loop_s": 1201, "lifetime_s": 3600},
	})
	not allow with input as bad_loop

	bad_life := object.union(_valid_none, {
		"timeouts": {"tool_s": 30, "loop_s": 1200, "lifetime_s": 3601},
	})
	not allow with input as bad_life

	bad_zero := object.union(_valid_none, {
		"timeouts": {"tool_s": 0, "loop_s": 1200, "lifetime_s": 3600},
	})
	not allow with input as bad_zero
}

test_deny_invalid_network_mode if {
	bad := object.union(_valid_none, {"network": {
		"mode": "open",
		"allowlist": [],
		"imds_blocked": true,
		"special_iana_blocked": true,
	}})
	not allow with input as bad
}

test_deny_none_mode_with_non_empty_allowlist if {
	bad := object.union(_valid_none, {"network": {
		"mode": "none",
		"allowlist": ["erp.ent.ca"],
		"imds_blocked": true,
		"special_iana_blocked": true,
	}})
	not allow with input as bad
}

test_deny_imds_ip_in_allowlist if {
	bad := object.union(_valid_none, {"network": {
		"mode": "allowlist",
		"allowlist": ["169.254.169.254"],
		"imds_blocked": true,
		"special_iana_blocked": true,
	}})
	not allow with input as bad
}

test_deny_mistyped_shell_env_and_negative_timeouts if {
	bad_shell := object.union(_valid_none, {"allow_shell": "false"})
	not allow with input as bad_shell

	bad_env := object.union(_valid_none, {"env_secrets": "none"})
	not allow with input as bad_env

	bad_neg := object.union(_valid_none, {
		"timeouts": {"tool_s": 30, "loop_s": 0, "lifetime_s": -1},
	})
	not allow with input as bad_neg

	bad_null := object.union(_valid_none, {
		"timeouts": {"tool_s": null, "loop_s": 1200, "lifetime_s": 3600},
	})
	not allow with input as bad_null
}
