# E2Yaml [![Downloads](https://pepy.tech/badge/e2yaml)](https://pepy.tech/project/e2yaml) [![Downloads](https://pepy.tech/badge/e2yaml/month)](https://pepy.tech/project/e2yaml/month) [![Downloads](https://pepy.tech/badge/e2yaml/week)](https://pepy.tech/project/e2yaml/week)
An environment variable to yaml converter. 

## Purpose
Due to security reasons at my job, we cannot upload contents of Yaml files that have sensitive data. Variables are injected into a virtual environment as environment variables via a Jenkins job. However, when testing locally, sometimes we need those variables. E2Yaml addresses that problem.

```
SPRING_DATA_MONGODB_DATABASE: TESTDB
SPRING_DATA_MONGODB_ENCRYPTION: disabled
SPRING_DATA_MONGODB_ENCRYPTION-KEY: FakePassWord!
SPRING_DATA_MONGODB_PASSWORD: !54353Ffesf34
SPRING_DATA_MONGODB_REPLICASET: FAKE-DB-531
```
Converts to:
```yml
spring:
  data:
    mongodb:
      database: TESTDB
      encryption: disabled
      encryption-key: "FakePassWord!"
      password: "!54353Ffesf34"
      replicaSet: FAKE-DB-531
```
 And we can see this from the command line by runnning driver.py:
 
 ```
 ╰─$ python3 driver.py
PARSING: 	SPRING_DATA_MONGODB_DATABASE: TESTDB	OK
PARSING: 	SPRING_DATA_MONGODB_ENCRYPTION: disabled	OK
PARSING: 	SPRING_DATA_MONGODB_ENCRYPTION-KEY: FakePassWord!	OK
PARSING: 	SPRING_DATA_MONGODB_PASSWORD: !54353Ffesf34	OK
PARSING: 	SPRING_DATA_MONGODB_REPLICASET: FAKE-DB-531	OK
 ```
## Installing
From bash run the line below
```bash
pip install E2Yaml
```
This project is published on pip at: https://pypi.org/project/E2Yaml/
## Importing
```bash
import E2Yaml as ey
```

## Loading
```python
# example program loading from clipboard and outputting to clipboard
yml = ey.from_clipboard(log=True, separate=True)

# converting a file
yml = ey.load_file('test_input.env', log=True)

# adding one line at a time
yml = EyConverter().add_line("SOME_TEXT=true")
```
Note: you can disable logging by not including the second parameter *log=True* and provide better output spacing with *separate=True*

## Preserving Words
Environment variables are delimited by '_' to indicate nesting in YAML and sometimes these characters are also used to define a variable. You can choose to preserve the letters by calling this function
```python
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
```
Note: environment variables are usually upper case and camel case is lost in translation. To preserve this, you can add the variable above as well.

## Ignoring Lines
If you're loading in from a file or from your clipboard, you can ignore specific lines containing an attribute.
```python
yml.ignore_lines_containing('JAVA_OPTS', 'CONVEYOR')
```

## Converting
First, you need to call the function *convert_to_dictionary()*, which returns itself, allowing chaining. Then, setting the proper output to clipboard, stdout, or a file.
```python
# in this case we are writing to the clipboard.
yml.convert_to_dictionary().to_clipboard()

# print to stdout
yml.convert_to_dictionary().show()

# print to file
yml.convert_to_dictionary().write_file('filename.yml'))
```

## Examples
driver.py is an example program to write to read from the clipboard and writes back for easy copying and pasting
