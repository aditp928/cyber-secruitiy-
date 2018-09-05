# Generate a hex dump of `secret_message`, but exclude ASCII table and line numbers
xxd -p secret_message

# Save hex dump to `secret_message.dump`
xxd -p secret_message | tee secret_message.dump

# Show hexdump
cat secret_message.dump

# Decode hexdump back into readable text. Both flags are necessary.
xxd -r -p secret_message.dump
