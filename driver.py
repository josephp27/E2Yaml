from eyconverter import EyConverter

ey = EyConverter().load_file('test.env')

ey.ignore_lines_containing('JAVA_OPTS', 'CONVEYOR')

ey.preserve_words('auditLog',
                  'queue_connection_factory',
                  'inbound_queue',
                  'outbound_queue',
                  'retry_queue',
                  'pkt_dead_letter_queue',
                  'idle_concurrent',
                  'max_concurrent')

ey.convert_to_dictionary().write_file('outty.yml')
