# TI-DSS-Python
Wrapper that enables interaction with Texas Instruments Debug Server Scripting through Python
## Introduction
DSS is a great tool for programming and running tests on Texas Instruments embedded computing products, but it really only supports scripting in Java-esque lanuages.

TI has examples for how to leverage Jython to script the debug server, but Jython only supports python up to 2.7 and doesn't support any python libraries that make use of C.  This IMO is pretty limiting.

TI-DSS-Python intends to provide a pathway to control the debug server from normal python.  FWIW this is intended to be more of an example than a full featured implementation.  It does what I need it to do.

## How it works
TI-DSS-Python uses Pyro4 implement an RPC interface to DSS.  The server runs in Jython so it can easily access all the DSS objects.  Clients can connect from whatever languages Pyro supports (i.e. real python) and make calls to DSS.

## Disclaimer
I don't work for TI (although I did at one point).  This repo isn't associated with TI in any way.  I'm a hardware/embedded software engineer.  My python isn't the best.  Deal with it or make a PR. Please don't sue me.

## Contributing
I dunno.  Make a PR and I'll look at it.

## License
Read the license file, do whatever you want.
