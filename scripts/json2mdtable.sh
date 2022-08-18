#!/bin/bash
# Output a (markdown) table from a set of .json host definitions passed via stdin
if which jq > /dev/null; then
	readonly columns=".name, .vm, .vmhost, .serial"
	echo ${columns} | tr -d "." | sed 's/^/| /g;s/,/ | /g;s/$/ |/g'
	jq --slurp 'reduce .[] as $item ({}; . * $item)' | jq -r ".[] | [${columns}] | @tsv" | sed 's/^/| /g;s/\t/ | /g;s/$/ |/g'
else
	echo "Install jq"
	exit 2
fi
