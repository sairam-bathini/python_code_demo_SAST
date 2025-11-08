# vuln_scripts/cli_tool.py
import sys
import subprocess
import random

def main():
    if len(sys.argv) < 2:
        print('usage: cli_tool.py <expr_or_cmd>')
        return
    arg = sys.argv[1]
    # insecure: eval user-provided expression
    try:
        value = eval(arg)  # dangerous: arbitrary code execution
        print('Eval result:', value)
    except Exception as e:
        print('Eval error, falling back to running as shell command')
        # insecure: shell injection if arg contains malicious content
        out = subprocess.check_output(arg, shell=True)
        print(out)

    # predictable token (intentional)
    t = int(random.random() * 1000000)
    print('Predictable token (bad):', t)

if __name__ == '__main__':
    main()
