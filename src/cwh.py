import fire

from api.leetcode.leetcode_cli import LeetcodeCLI

class CLI:
    def __init__(self):
        self.leetcode = LeetcodeCLI()

def main():
    fire.core.Display = lambda lines, out: print(*lines, file = out)
    fire.Fire(CLI())
    
if __name__ == "__main__":
    main()
