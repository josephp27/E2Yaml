#!/usr/bin/env python3

# first import the tool

# example program loading from clipboard and outputting to clipboard
import E2Yaml

yml = E2Yaml.from_clipboard(log=True)

# uncomment this if you would like to convert a file
# yml = ey.load_file('test_input.env', log=True)

# optional argument to ignore lines that contain a value. Accepts unlimited parameters
yml.ignore_lines_containing('JAVA_OPTS', 'CONVEYOR', 'JBP')

# optional argument to maintain a word. If your config uses camel case or under scores
# this is a setting you want. Note: only preserves the specified word, NOT the line.
# use ignore_lines_containing above if that is your use case
yml.preserve_words('auditLog',
                   'logInsertsEnabled',
                   'kafkaEnabled',
                   'tibcoPublishes',
                   'tibcoSubscriptions',
                   'queue_connection_factory',
                   'inbound_queue',
                   'outbound_queue',
                   'retry_queue',
                   'pkt_dead_letter_queue',
                   'idle_concurrent',
                   'max_concurrent',
                   'connection_timeout',
                   'connection_attempts',
                   'reconnection_timeout',
                   'reconnection_attempts',
                   'replicaSet',
                   'receive_timeout',
                   'client_key')

# first you need to convert the input to a dictionary, then set the output destination.
# in this case we are writing to the clipboard. Other options include a file or stdout
yml.convert_to_dictionary().to_clipboard()
