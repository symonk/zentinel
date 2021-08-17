========
Zentinel
========

.. image:: https://img.shields.io/pypi/v/zentinel.svg
        :target: https://pypi.python.org/pypi/zentinel

.. image:: https://github.com/symonk/zentinel/actions/workflows/python-package.yml/badge.svg
        :target: https://github.com/symonk/zentinel/actions

.. image:: https://readthedocs.org/projects/zentinel/badge/?version=latest
        :target: https://zentinel.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://codecov.io/gh/symonk/zentinel/branch/master/graph/badge.svg?token=E7SVA868NR
    :target: https://codecov.io/gh/symonk/zentinel

Zentinel
=========

Zentinel is a fully async TCP port scanner written on top of asyncio.  It's sole purpose is for administrators
to test services that are exposed on their infrastructure with a simple python library.  Zentinel is powerful
and highly configurable, by default it will complete full TCP connect scans on each of the ports, however to
perform a SYN -> ACK -> RST --half-open can be specified which will prevent a full 3 way handshake and connection.
Zentinel is lightning fast, compared to other multi threaded models.

----

Legal Disclaimer
-----------------

The use of code contained in this repository, either in part or in its totality, for engaging targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws.

Developers assume no liability and are not responsible for misuses or damages caused by any code contained in this repository in any event that, accidentally or otherwise, it comes to be utilized by a threat agent or unauthorized entity as a means to compromise the security, privacy, confidentiality, integrity, and/or availability of systems and their associated resources by leveraging the exploitation of known or unknown vulnerabilities present in said systems, including, but not limited to, the implementation of security controls, human- or electronically-enabled.

The use of this code is only endorsed by the developers in those circumstances directly related to educational environments or authorized penetration testing engagements whose declared purpose is that of finding and mitigating vulnerabilities in systems, limiting their exposure to compromises and exploits employed by malicious agents as defined in their respective threat models.
