import json
import logging
import argparse
from SWProxy import SWPlugin

logging.basicConfig()

class PluginTester:
    @staticmethod
    def getPluginNames():
        lines = []
        for plugin in SWPlugin.plugins:
            lines.append("\t\t{}".format(plugin.name))
        return "\n".join(lines)

    @staticmethod
    def execute_calls(filename):
        with open(filename) as f:
            calls = json.load(f)
            i = 1
            for call in calls:
                print 'processing call #%s\n' % i
                SWPlugin.call_plugins('process_request', (call['request'], call['response']))
                i += 1

if __name__ == "__main__":
    tester = PluginTester()
    print tester.getPluginNames()

    parser = argparse.ArgumentParser(description='SW Proxy - Plugin Tester')
    parser.add_argument('-f', '--file', type=str)
    options = parser.parse_args()

    if options.file is not None:
        tester.execute_calls(options.file)
