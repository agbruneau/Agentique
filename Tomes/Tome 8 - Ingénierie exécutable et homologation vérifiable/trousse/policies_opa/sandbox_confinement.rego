# SPDX-License-Identifier: MIT
package trousse.policy.sandbox

import rego.v1

default allow := false

allow if {
	is_string(input.sandbox_id)
	count(input.sandbox_id) > 0
	input.network.imds_blocked == true
	input.network.special_iana_blocked == true
	is_array(input.env_secrets)
	count(input.env_secrets) == 0
	input.read_only_root == true
	input.allow_shell == false
	_timeouts_ok
	_network_ok
}

_timeouts_ok if {
	is_number(input.timeouts.tool_s)
	is_number(input.timeouts.loop_s)
	is_number(input.timeouts.lifetime_s)
	round(input.timeouts.tool_s) == input.timeouts.tool_s
	round(input.timeouts.loop_s) == input.timeouts.loop_s
	round(input.timeouts.lifetime_s) == input.timeouts.lifetime_s
	input.timeouts.tool_s >= 1
	input.timeouts.tool_s <= 30
	input.timeouts.loop_s >= 1
	input.timeouts.loop_s <= 1200
	input.timeouts.lifetime_s >= 1
	input.timeouts.lifetime_s <= 3600
}

_network_ok if {
	input.network.mode == "none"
	is_array(input.network.allowlist)
	count(input.network.allowlist) == 0
}

_network_ok if {
	input.network.mode == "allowlist"
	is_array(input.network.allowlist)
	every host in input.network.allowlist {
		is_string(host)
		count(host) > 0
		not contains(host, "*")
		host != "169.254.169.254"
		not startswith(host, "127.")
		not startswith(host, "10.")
		not startswith(host, "169.254.")
		not startswith(host, "192.168.")
		lower(host) != "localhost"
		host != "::1"
	}
}
