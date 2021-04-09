# Event-stack thing
This code can be used to create a minimal Python API server which will transform certain querystring information to a json message.
Currently this code can be used to turn http calls into messages to be sent to an upstream system (for instance SQS).
The messages should be defined as class and be JSON serionizable somehow. For AWS calls to work you should have AWS cli working and configured credentials.

## Files
* Message class - message.py
* Upstream contstruct - upstream.py
* Basic http interface - server.py

## Usage
- set the correct SQS url in upstream.py.
- make sure the server listens on the right ip and port in server.py

```
python3 server.py
```

## Dependencies
See requirements.txt, currently very much depending on Boto3 and JSON.