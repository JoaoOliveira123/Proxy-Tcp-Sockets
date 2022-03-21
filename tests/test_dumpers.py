from proxy.utils import BytesToHexOrganizedDumper

def test(src, length):
    dumper = BytesToHexOrganizedDumper()
    dumper.dump(src, length)
    dumper.print_dumped_value()

def main():
    test(b'Hello World, i can not wait for enter into this world', 16)