import fire

from .api.leetcode.leetcode_cli import LeetcodeCLI
from .api.lintcode.lintcode_cli import LintcodeCLI
from .api.geeksforgeeks.gfg_cli import GFGCLI

class CLI:
    def __init__(self):
        self.leetcode = LeetcodeCLI()
        self.lintcode = LintcodeCLI()
        self.gfg = GFGCLI()

def main():
    fire.core.Display = lambda lines, out: print(*lines, file = out)
    fire.Fire(CLI())
    
if __name__ == "__main__":
    main()
