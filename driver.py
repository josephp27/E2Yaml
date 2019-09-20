import eyconverter as ey

yml = ey.load_file('test_input.env', log=True)

yml.ignore_lines_containing('JAVA_OPTS', 'CONVEYOR')

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
                   'replicaSet')

yml.convert_to_dictionary().write_file('output.yml')
