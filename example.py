# Import the config module.
import config

# Call the parse_config method from the config module
# with the filepath as the parameter.
# The parse_config method returns a Config object which
# is stored in the 'test' variable.
test = config.parse_config('test.conf')

# Print the config filename to standard out to
# demonstrate that the config filename is stored in
# the Config object.
print(test.name)

print()

# Print the config parameters to standard out to
# demonstrate how the Config object's get method
# is used to retrieve values by the config parameter
# name.
print(test.get('host'))
print(test.get('server_id'))
print(test.get('server_load_alarm'))
print(test.get('user'))
print(test.get('verbose'))
print(test.get('test_mode'))
print(test.get('debug_mode'))
print(test.get('log_file_path'))
print(test.get('send_notifications'))

print()

# Print config name-value pairs to standard out to
# demonstrate how the Config object's 'parameters'
# variable can be used to iterate over the config
# parameters' names and/or values.
for name, value in test.parameters.items():
    print('<%s: %s>'%(name, value))

print()

# Print output of exists method to standard out to
# demonstrate how the Config object's exists method
# can be used to check if a given parameter is
# associated with this Config object.
print(test.exists('user_id'))
print(test.exists('user'))
