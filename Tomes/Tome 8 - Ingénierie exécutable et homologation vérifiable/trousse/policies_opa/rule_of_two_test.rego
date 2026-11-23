# SPDX-License-Identifier: MIT
package trousse.policy.rule_of_two_test

import rego.v1

import data.trousse.policy.rule_of_two.allow

_valid_sha := concat("", [
	"92be40835a73023d117ebb4965da82df",
	"a05e2e6d647d0919d53461289bbc6e81",
])

_other_sha := concat("", [
	"00000000000000000000000000000000",
	"00000000000000000000000000000000",
])

_base_p0 := {
	"tool": {
		"name": "lire_catalogue",
		"tier": "P0",
		"exfiltration_capable": false,
		"egress_destination": "internal-catalog.ent.ca",
	},
	"session": {"consumed_untrusted": false},
	"human_approval": {
		"verified": false,
		"action_sha256": null,
		"approver_sub": null,
	},
	"computed_action_sha256": _valid_sha,
	"principal_sub": "alice",
	"egress_allowlist": ["internal-catalog.ent.ca", "erp.ent.ca"],
}

test_allow_p0_trusted_no_exfil if {
	allow with input as _base_p0
}

test_allow_p1_trusted_no_egress_destination if {
	p1 := object.union(_base_p0, {"tool": {
		"name": "lire_solde",
		"tier": "P1",
		"exfiltration_capable": false,
		"egress_destination": null,
	}})
	allow with input as p1
}

test_allow_p2_uncontaminated_no_exfil if {
	p2 := object.union(_base_p0, {"tool": {
		"name": "creer_brouillon_bc",
		"tier": "P2",
		"exfiltration_capable": false,
		"egress_destination": "erp.ent.ca",
	}})
	allow with input as p2
}

test_allow_p3_with_valid_distinct_human_approval if {
	p3 := object.union(_base_p0, {
		"tool": {
			"name": "virer_fonds",
			"tier": "P3",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"human_approval": {
			"verified": true,
			"action_sha256": _valid_sha,
			"approver_sub": "apb-5e19c2",
		},
	})
	allow with input as p3
}

test_allow_untrusted_and_exfil_with_valid_approval if {
	req := object.union(_base_p0, {
		"tool": {
			"name": "envoyer_rapport",
			"tier": "P2",
			"exfiltration_capable": true,
			"egress_destination": "erp.ent.ca",
		},
		"session": {"consumed_untrusted": true},
		"human_approval": {
			"verified": true,
			"action_sha256": _valid_sha,
			"approver_sub": "apb-91d4e8",
		},
	})
	allow with input as req
}

test_deny_empty_payload if {
	not allow with input as {}
}

test_deny_null_fields if {
	bad := object.union(_base_p0, {
		"session": {"consumed_untrusted": null},
		"tool": null,
	})
	not allow with input as bad
}

test_deny_mistyped_boolean_as_string if {
	bad := object.union(_base_p0, {
		"session": {"consumed_untrusted": "false"},
		"tool": {
			"name": "lire_catalogue",
			"tier": "P0",
			"exfiltration_capable": "false",
			"egress_destination": "internal-catalog.ent.ca",
		},
	})
	not allow with input as bad
}

test_deny_mistyped_tier_int if {
	bad := object.union(_base_p0, {"tool": {
		"name": "lire_catalogue",
		"tier": 0,
		"exfiltration_capable": false,
		"egress_destination": "internal-catalog.ent.ca",
	}})
	not allow with input as bad
}

test_deny_untrusted_plus_exfiltration_without_approval if {
	bad := object.union(_base_p0, {
		"tool": {
			"name": "webhook_externe",
			"tier": "P1",
			"exfiltration_capable": true,
			"egress_destination": "erp.ent.ca",
		},
		"session": {"consumed_untrusted": true},
	})
	not allow with input as bad
}

test_deny_untrusted_p2_without_approval if {
	bad := object.union(_base_p0, {
		"tool": {
			"name": "creer_bc",
			"tier": "P2",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"session": {"consumed_untrusted": true},
	})
	not allow with input as bad
}

test_deny_p3_without_approval if {
	bad := object.union(_base_p0, {"tool": {
		"name": "virer_fonds",
		"tier": "P3",
		"exfiltration_capable": false,
		"egress_destination": "erp.ent.ca",
	}})
	not allow with input as bad
}

test_deny_action_sha256_mismatch if {
	bad := object.union(_base_p0, {
		"tool": {
			"name": "virer_fonds",
			"tier": "P3",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"human_approval": {
			"verified": true,
			"action_sha256": _other_sha,
			"approver_sub": "apb-5e19c2",
		},
	})
	not allow with input as bad
}

test_deny_self_approval_approver_equals_principal if {
	bad := object.union(_base_p0, {
		"tool": {
			"name": "virer_fonds",
			"tier": "P3",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"human_approval": {
			"verified": true,
			"action_sha256": _valid_sha,
			"approver_sub": "alice",
		},
	})
	not allow with input as bad
}

test_deny_egress_destination_not_in_allowlist if {
	bad := object.union(_base_p0, {"tool": {
		"name": "lire_catalogue",
		"tier": "P0",
		"exfiltration_capable": false,
		"egress_destination": "attacker.example.net",
	}})
	not allow with input as bad
}

test_deny_unknown_tier if {
	bad := object.union(_base_p0, {"tool": {
		"name": "x",
		"tier": "P9",
		"exfiltration_capable": false,
		"egress_destination": "erp.ent.ca",
	}})
	not allow with input as bad
}

test_deny_empty_action_sha256_even_if_equal if {
	bad := object.union(_base_p0, {
		"tool": {
			"name": "virer_fonds",
			"tier": "P3",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"computed_action_sha256": "",
		"human_approval": {
			"verified": true,
			"action_sha256": "",
			"approver_sub": "apb-5e19c2",
		},
	})
	not allow with input as bad
}

test_deny_null_approver_sub_or_unverified_flag if {
	bad_null := object.union(_base_p0, {
		"tool": {
			"name": "virer_fonds",
			"tier": "P3",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"human_approval": {
			"verified": true,
			"action_sha256": _valid_sha,
			"approver_sub": null,
		},
	})
	not allow with input as bad_null

	bad_unver := object.union(_base_p0, {
		"tool": {
			"name": "virer_fonds",
			"tier": "P3",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"human_approval": {
			"verified": false,
			"action_sha256": _valid_sha,
			"approver_sub": "apb-5e19c2",
		},
	})
	not allow with input as bad_unver
}

test_deny_egress_allowlist_null_or_wildcard if {
	bad_null := object.union(_base_p0, {"egress_allowlist": null})
	not allow with input as bad_null

	bad_wild_only := object.union(_base_p0, {
		"egress_allowlist": ["*"],
		"tool": {
			"name": "lire_catalogue",
			"tier": "P0",
			"exfiltration_capable": false,
			"egress_destination": "*",
		},
	})
	not allow with input as bad_wild_only

	bad_wild_mixed := object.union(_base_p0, {
		"egress_allowlist": ["*", "internal-catalog.ent.ca"],
	})
	not allow with input as bad_wild_mixed
}

test_deny_exfil_or_untrusted_low_tier_without_approval if {
	bad_exfil := object.union(_base_p0, {"tool": {
		"name": "webhook_exfil",
		"tier": "P1",
		"exfiltration_capable": true,
		"egress_destination": "erp.ent.ca",
	}})
	not allow with input as bad_exfil

	bad_untrusted_p1 := object.union(_base_p0, {
		"tool": {
			"name": "lire_solde",
			"tier": "P1",
			"exfiltration_capable": false,
			"egress_destination": "erp.ent.ca",
		},
		"session": {"consumed_untrusted": true},
	})
	not allow with input as bad_untrusted_p1
}

test_deny_empty_or_mistyped_principal_and_egress if {
	bad_princ := object.union(_base_p0, {"principal_sub": ""})
	not allow with input as bad_princ

	bad_egress_type := object.union(_base_p0, {"tool": {
		"name": "lire_catalogue",
		"tier": "P0",
		"exfiltration_capable": false,
		"egress_destination": 123,
	}})
	not allow with input as bad_egress_type

	bad_egress_empty := object.union(_base_p0, {"tool": {
		"name": "lire_catalogue",
		"tier": "P0",
		"exfiltration_capable": false,
		"egress_destination": "",
	}})
	not allow with input as bad_egress_empty
}
