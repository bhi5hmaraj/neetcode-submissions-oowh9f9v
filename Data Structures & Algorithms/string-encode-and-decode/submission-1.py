class Solution:

    # we will map the characters to int so str -> List[int]
    # enc(List[str]) = enc'(s1) + enc'(s2) .... enc'(sn)
    EMPTY_ENC = 'EMPTY'
    def _enc(self, word) -> str:
        if not word:
            return ""
        return '-'.join(map(str, map(ord, word)))
  
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return self.EMPTY_ENC
        return '/'.join(map(self._enc, strs))

    def _dec(self, word) -> str:
        if not word:
            return ""
        return ''.join(map(chr, map(int, word.split('-'))))

    def decode(self, s: str) -> List[str]:
        if s == self.EMPTY_ENC:
            return []

        return list(map(self._dec, s.split( '/')))
