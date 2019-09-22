import dns.query
import dns.zone
import argparse as ap

def transferZone(dnsServer, domain):
    try:
        return dns.zone.from_xfr(dns.query.xfr(dnsServer, domain))
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':

    parser = ap.ArgumentParser()
    parser.add_argument('--server', help='The DNS server to consult.', required=True)
    parser.add_argument('--domain', help='The domain to be consulted.', required=True)
    parsed = parser.parse_args()

    results = transferZone(parsed.server, parsed.domain)

    if not results:
        print('Could not transfer zones.')
    else:
        for name in results.nodes.keys():
            print(results[name].to_text(name))