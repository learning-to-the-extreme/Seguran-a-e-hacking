//Recommended way to install:
$ python3 -m pip install --upgrade git+https://github.com/fportantier/habu.git


//Now we have a command to upgrade directly from the Git repo and clean any old
//command that not longer exists or that has been renamed.
$ habu.upgrade


//habu.arp.ping
Usage: habu.arp.ping [OPTIONS] IP

  Send ARP packets to check if a host it's alive in the local network.

  Example:

  # habu.arp.ping 192.168.0.1
  Ether / ARP is at a4:08:f5:19:17:a4 says 192.168.0.1 / Padding

Options:
  -i TEXT  Interface to use
  -v       Verbose output
  --help   Show this message and exit.


//habu.arp.poison
Usage: habu.arp.poison [OPTIONS] VICTIM1 VICTIM2

  Send ARP 'is-at' packets to each victim, poisoning their ARP tables for
  send the traffic to your system.

  Note: If you want a full working Man In The Middle attack, you need to
  enable the packet forwarding on your operating system to act like a
  router. You can do that using:

  # echo 1 > /proc/sys/net/ipv4/ip_forward

  Example:

  # habu.arpoison 192.168.0.1 192.168.0.77
  Ether / ARP is at f4:96:34:e5:ae:1b says 192.168.0.77
  Ether / ARP is at f4:96:34:e5:ae:1b says 192.168.0.70
  Ether / ARP is at f4:96:34:e5:ae:1b says 192.168.0.77
  ...

Options:
  -i TEXT  Interface to use
  -v       Verbose
  --help   Show this message and exit.


//habu.arp.sniff
Usage: habu.arp.sniff [OPTIONS]

  Listen for ARP packets and show information for each device.

  Columns: Seconds from last packet | IP | MAC | Vendor

  Example:

  1   192.168.0.1     a4:08:f5:19:17:a4   Sagemcom Broadband SAS
  7   192.168.0.2     64:bc:0c:33:e5:57   LG Electronics (Mobile Communications)
  2   192.168.0.5     00:c2:c6:30:2c:58   Intel Corporate
  6   192.168.0.7     54:f2:01:db:35:58   Samsung Electronics Co.,Ltd

Options:
  -i TEXT  Interface to use
  --help   Show this message and exit.


//habu.asydns
Usage: habu.asydns [OPTIONS]

  Requests a DNS domain name based on public and private RSA keys using the
  AsyDNS protocol https://github.com/portantier/asydns

  Example:

  $ habu.asydns -v
  Generating RSA key ...
  Loading RSA key ...
  {
      "ip": "181.31.41.231",
      "name": "07286e90fd6e7e6be61d6a7919967c7cf3bbfb23a36edbc72b6d7c53.a.asydns.org"
  }

  $ dig +short 07286e90fd6e7e6be61d6a7919967c7cf3bbfb23a36edbc72b6d7c53.a.asydns.org
  181.31.41.231

Options:
  -u TEXT  API URL
  -g       Force the generation of a new key pair
  -r       Revoke the public key
  -v       Verbose output
  --help   Show this message and exit.


//habu.b64
Usage: habu.b64 [OPTIONS] [F]

  Encodes or decode data in base64, just like the command base64.

  $ echo awesome | habu.b64
  YXdlc29tZQo=

  $ echo YXdlc29tZQo= | habu.b64 -d
  awesome

Options:
  -d      decode instead of encode
  --help  Show this message and exit.


//habu.cert.clone
Usage: habu.cert.clone [OPTIONS] HOSTNAME PORT KEYFILE CERTFILE

  Connect to an SSL/TLS server, get the certificate and generate a
  certificate with the same options and field values.

  Note: The generated certificate is invalid, but can be used for social
  engineering attacks

  Example:

  $ habu.certclone www.google.com 443 /tmp/key.pem /tmp/cert.pem

Options:
  --copy-extensions  Copy certificate extensions (default: False)
  --expired          Generate an expired certificate (default: False)
  -v                 Verbose
  --help             Show this message and exit.


//habu.cert.crtsh
Usage: habu.cert.crtsh [OPTIONS] DOMAIN

  Downloads the certificate transparency logs for a domain and check with
  DNS queries if each subdomain exists.

  Uses multithreading to improve the performance of the DNS queries.

  Example:

  $ habu.crtsh securetia.com
  alt.securetia.com
  other.securetia.com
  www.securetia.com

Options:
  -c      Disable cache
  -n      Disable DNS subdomain validation
  -v      Verbose output
  --json  Print the output in JSON format
  --help  Show this message and exit.


//habu.cert.names
Usage: habu.cert.names [OPTIONS] [NETWORK]

  Connects to each host/port and shows a summary of the certificate names.

  The hosts to connect to are taken from two possible options:

  1. -i option (default: stdin). A file where each line is a host or network

  2. An argument that can be a host or network

  If you use both methods, the hosts and networks are merged into one list.

  Example:

  $ habu.cert.names 2.18.60.240/29
  2.18.60.241         443 i.s-microsoft.com microsoft.com privacy.microsoft.com
  2.18.60.242         443 aod-ssl.itunes.apple.com aod.itunes.apple.com aodp-ssl.itunes.apple.com
  2.18.60.243         443 *.mlb.com mlb.com
  2.18.60.244         443 [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1056)
  2.18.60.245         443 cert2-cn-public-ubiservices.ubi.com cert2-cn-public-ws-ubiservices.ubi.com
  2.18.60.246         443 *.blog.sina.com.cn *.dmp.sina.cn

  aod.itunes.apple.com
  aodp-ssl.itunes.apple.com
  aod-ssl.itunes.apple.com
  *.blog.sina.com.cn
  cert2-cn-public-ubiservices.ubi.com
  cert2-cn-public-ws-ubiservices.ubi.com
  *.dmp.sina.cn
  i.s-microsoft.com microsoft.com
  *.mlb.com mlb.com
  privacy.microsoft.com

Options:
  -p TEXT      Ports to connect to (comma separated list)
  -i FILENAME  Input file (Default: stdin)
  -t FLOAT     Time to wait for each connection
  -v           Verbose output
  --json       Print the output in JSON format
  --help       Show this message and exit.


//habu.config.del
Usage: habu.config.del [OPTIONS] KEY

  Delete a KEY from the configuration.

  Note: By default, KEY is converted to uppercase.

  Example:

  $ habu.config.del DNS_SERVER

Options:
  --help  Show this message and exit.


//habu.config.set
Usage: habu.config.set [OPTIONS] KEY VALUE

  Set VALUE to the config KEY.

  Note: By default, KEY is converted to uppercase.

  Example:

  $ habu.config.set DNS_SERVER 8.8.8.8

Options:
  --help  Show this message and exit.


//habu.config.show
Usage: habu.config.show [OPTIONS]

  Show the current config.

  Note: By default, the options with 'KEY' in their name are shadowed.

  Example:

  $ habu.config.show
  {
      "DNS_SERVER": "8.8.8.8",
      "FERNET_KEY": "*************"
  }

Options:
  -k, --show-keys   Show also the key values
  --option TEXT...  Write to the config(KEY VALUE)
  --help            Show this message and exit.


//habu.crack.luhn
Usage: habu.crack.luhn [OPTIONS] NUMBER

  Having known values for a Luhn validated number, obtain the possible
  unknown numbers.

  Numbers that use the Luhn algorithm for validation are Credit Cards, IMEI,
  National Provider Identifier in the United States, Canadian Social
  Insurance Numbers, Israel ID Numbers and Greek Social Security Numbers
  (ΑΜΚΑ).

  The '-' characters are ignored.

  Define the missing numbers with the 'x' character.

  Reference: https://en.wikipedia.org/wiki/Luhn_algorithm

  Example:

  $ habu.crack.luhn 4509-xx08-3160-6445
  4509000831606445
  4509180831606445
  4509260831606445
  4509340831606445
  4509420831606445
  4509590831606445
  4509670831606445
  4509750831606445
  4509830831606445
  4509910831606445

Options:
  --help  Show this message and exit.


//habu.crack.snmp
Usage: habu.crack.snmp [OPTIONS] IP

  Launches snmp-get queries against an IP, and tells you when finds a valid
  community string (is a simple SNMP cracker).

  The dictionary used is the distributed with the onesixtyone tool
  https://github.com/trailofbits/onesixtyone

  Example:

  # habu.crack.snmp 179.125.234.210
  Community found: private
  Community found: public

  Note: You can also receive messages like \<UNIVERSAL\> \<class
  'scapy.asn1.asn1.ASN1\_Class\_metaclass'\>, I don't know how to supress
  them for now.

Options:
  -p INTEGER  Port to use
  -c TEXT     Community (default: list of most used)
  -s          Stop after first match
  -v          Verbose
  --help      Show this message and exit.


//habu.crypto.fernet
Usage: habu.crypto.fernet [OPTIONS]

  Fernet cipher.

  Uses AES-128-CBC with HMAC

  Note: You must use a key to cipher with Fernet.

  Use the -k paramenter or set the FERNET_KEY configuration value.

  The keys can be generated with the command habu.crypto.fernet.genkey

  Reference: https://github.com/fernet/spec/blob/master/Spec.md

  Example:

  $ "I want to protect this string" | habu.crypto.fernet
  gAAAAABbXnCGoCULLuVNRElYTbEcwnek9iq5jBKq9JAN3wiiBUzPqpUgV5oWvnC6xfIA...

  $ echo gAAAAABbXnCGoCULLuVNRElYTbEcwnek9iq5jBKq9JAN3wiiBUzPqpUgV5oWvnC6xfIA... | habu.crypto.fernet -d
  I want to protect this string

Options:
  -k TEXT        Key
  -d             Decrypt instead of encrypt
  --ttl INTEGER  Time To Live for timestamp verification
  -i FILENAME    Input file (default: stdin)
  -o FILENAME    Output file (default: stdout)
  --help         Show this message and exit.


//habu.crypto.fernet.genkey
Usage: habu.crypto.fernet.genkey [OPTIONS]

  Generate a new Fernet Key, optionally write it to ~/.habu.json

  Example:

  $ habu.crypto.fernet.genkey
  xgvWCIvjwe9Uq7NBvwO796iI4dsGD623QOT9GWqnuhg=

Options:
  -w      Write this key to ~/.habu.json
  --help  Show this message and exit.


//habu.crypto.gppref
Usage: habu.crypto.gppref [OPTIONS] PASSWORD

  Decrypt the password of local users added via Windows 2008 Group Policy
  Preferences.

  This value is the 'cpassword' attribute embedded in the Groups.xml file,
  stored in the domain controller's Sysvol share.

  Example:

  # habu.crypto.gppref AzVJmXh/J9KrU5n0czX1uBPLSUjzFE8j7dOltPD8tLk
  testpassword

Options:
  --help  Show this message and exit.


//habu.crypto.hasher
Usage: habu.crypto.hasher [OPTIONS] [F]

  Compute various hashes for the input data, that can be a file or a stream.

  Example:

  $ habu.crypto.hasher README.rst
  md5          992a833cd162047daaa6a236b8ac15ae README.rst
  ripemd160    0566f9141e65e57cae93e0e3b70d1d8c2ccb0623 README.rst
  sha1         d7dbfd2c5e2828eb22f776550c826e4166526253 README.rst
  sha256       6bb22d927e1b6307ced616821a1877b6cc35e... README.rst
  sha512       8743f3eb12a11cf3edcc16e400fb14d599b4a... README.rst
  whirlpool    96bcc083242e796992c0f3462f330811f9e8c... README.rst

  You can also specify which algorithm to use. In such case, the output is
  only the value of the calculated hash:

  $ habu.hasher -a md5 README.rst
  992a833cd162047daaa6a236b8ac15ae README.rst

Options:
  -a [md5|sha1|sha256|sha512|ripemd160|whirlpool]
                                  Only this algorithm (Default: all)
  --help                          Show this message and exit.


//habu.crypto.xor
Usage: habu.crypto.xor [OPTIONS]

  XOR cipher.

  Note: XOR is not a 'secure cipher'. If you need strong crypto you must use
  algorithms like AES. You can use habu.fernet for that.

  Example:

  $ habu.xor -k mysecretkey -i /bin/ls > xored
  $ habu.xor -k mysecretkey -i xored > uxored
  $ sha1sum /bin/ls uxored
  $ 6fcf930fcee1395a1c95f87dd38413e02deff4bb  /bin/ls
  $ 6fcf930fcee1395a1c95f87dd38413e02deff4bb  uxored

Options:
  -k TEXT      Encryption key
  -i FILENAME  Input file (default: stdin)
  -o FILENAME  Output file (default: stdout)
  --help       Show this message and exit.


//habu.data.enrich
Usage: habu.data.enrich [OPTIONS]

  Enrich data adding interesting information.

  Example:

  $ cat /var/log/auth.log | habu.data.extract.ipv4 | habu.data.enrich
  [
      {
          "asset": "8.8.8.8",
          "family": "IPAddress",
          "asn": "15169",
          "net": "8.8.8.0/24",
          "cc": "US",
          "rir": "ARIN",
          "asname": "GOOGLE - Google LLC, US"
      },
      {
          "asset": "8.8.4.4",
          "family": "IPAddress",
          "asn": "15169",
          "net": "8.8.4.0/24",
          "cc": "US",
          "rir": "ARIN",
          "asname": "GOOGLE - Google LLC, US"
      }
  ]

Options:
  -i FILENAME  Input file (Default: stdin)
  -v           Verbose output
  --help       Show this message and exit.


//habu.data.extract.domain
Usage: habu.data.extract.domain [OPTIONS] [INFILE]

  Extract valid domains from a file or stdin.

  Optionally, check each domain for the presence of NS registers.

  Example:

  $ cat /var/log/some.log | habu.data.extract.domain -c
  google.com
  ibm.com
  redhat.com

Options:
  -c      Check if domain has NS servers defined
  -v      Verbose output
  -j      JSON output
  --help  Show this message and exit.


//habu.data.extract.email
Usage: habu.data.extract.email [OPTIONS] [INFILE]

  Extract email addresses from a file or stdin.

  Example:

  $ cat /var/log/auth.log | habu.data.extract.email
  john@securetia.com
  raven@acmecorp.net
  nmarks@fimax.com

Options:
  -v      Verbose output
  -j      JSON output
  --help  Show this message and exit.


//habu.data.extract.fqdn
Usage: habu.data.extract.fqdn [OPTIONS] [INFILE]

  Extract FQDNs (Fully Qualified Domain Names) from a file or stdin.

  Example:

  $ cat /var/log/some.log | habu.data.extract.fqdn
  www.google.com
  ibm.com
  fileserver.redhat.com

Options:
  -c      Check if hostname resolves
  -v      Verbose output
  -j      JSON output
  --help  Show this message and exit.


//habu.data.extract.ipv4
Usage: habu.data.extract.ipv4 [OPTIONS] [INFILE]

  Extract IPv4 addresses from a file or stdin.

  Example:

  $ cat /var/log/auth.log | habu.data.extract.ipv4
  172.217.162.4
  23.52.213.96
  190.210.43.70

Options:
  -j, --json    JSON output
  -u, --unique  Remove duplicates
  -v            Verbose output
  --help        Show this message and exit.


//habu.data.filter
Usage: habu.data.filter [OPTIONS] FIELD [gt|lt|eq|ne|ge|le|in|contains|defin
                          ed|undefined|true|false] [VALUE]

  Filter data based on operators.

  Operator Reference:

  gt:         Greater than
  lt:         Lesser than
  eq:         Equal to
  ne:         Not equal to
  ge:         Greather or equal than
  le:         Lesser or equal than
  in:         Inside the list of values (or inside the network)
  contains:   Contains the value (or the network address)
  defined:    The value is defined
  undefined:  The value is not defined
  true:       The value is True
  false:      The value is False

  Example:

  $ cat /var/log/auth.log | habu.data.extract.ipv4 | habu.data.enrich | habu.data.filter cc eq US
  [
      {
          "item": "8.8.8.8",
          "family": "ipv4_address",
          "asn": "15169",
          "net": "8.8.8.0/24",
          "cc": "US",
          "rir": "ARIN",
          "asname":  "GOOGLE - Google LLC, US"
      }
  ]

  Docs: https://fportantier.github.io/hacking-with-habu/user/data-manipulation.html#data-enrichment

Options:
  -i FILENAME  Input file (Default: stdin)
  -v           Verbose output
  --not        Negate the comparison
  --help       Show this message and exit.
