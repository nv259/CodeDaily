class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)
        M = len(strs[0])
        satisfied = [False] * N

        """
        strs[0][0] strs[0][1] ... strs[0][M - 1]
        strs[1][0] strs[1][1] ... strs[1][M - 1]
        strs[2][0] strs[2][1] ... strs[2][M - 1]
        ...
        strs[N - 1][0] strs[N - 1][1] ... strs[N - 1][M - 1]
        """

        ans = 0
        for j in range(M):
            is_lxc_order = True
            for i in range(1, N):
                if not satisfied[i - 1] and strs[i - 1][j] > strs[i][j]:
                    is_lxc_order = False
                    ans += 1
                    break
            
            if is_lxc_order:
                for i in range(1, N):
                    if not satisfied[i - 1] and strs[i - 1][j] < strs[i][j]:
                        satisfied[i - 1] = True
        
        return ans

# Solution().minDeletionSize(["vqyoysnpxbjiitandmvugsqpfmggkv","uzdfeclxepjzfecmsxrqqkcomtrnvm","yvhwrsapfffwehdmvqwxstgeexfeua","awjymwysjpazpgdeqtvdiebfwuapin","odhihlbvsnximvdwqntdeqptigiyik","qtrfpwiilxskcieilfvarqbnpdxham","whvrqkdwuzbcaagsmlfvfbeataygud","kncwqrmejjmhtfhppsrdmzqperwlww","hgphuwaumjjibzhvvejpniopjxizie","bxvccswqevnudqicgrvjecfqpeppob","nnmvncnpbksdjyjjelsjizliicxpgz","oifmofrkbgpxlhkcbibwaoiygmqqio","ekdfyvsumngcfjlydgpmhgjjyfovfi","fyqryrpkvauhkylmfzhuasjxpqrohx","rdvjglvpavzdmtobnpjfwdwivhrpsj","zahrkuiejecndfprwysunznialtfok","jlrgpfdptlolmlqoophhciiqjnxdkh","bhbsdukebqvvemrcunboipprcbrfcl","kreyeyvsmufolvsrzdyeqpuqlieeij","vgosaxsfnbsndstjohgyknyionhoga","igmnlibpadandgtugbgxpxwlqbknmv","mjdbxxprxbjegvtthlrenhfpdlamww","qfssehellhvqyntozbrizixptppfpr","utghfndlcturahtcvmqrjyxqfhrsxt","xvminqhybbiadetniqfwubqxmjokjv","udfckncwvhcrmxtbkqbqqptymlqnss","gwwcmterazvyakuvwtyhthfiohlywq","mpieryurvarojfvhfbbcwepdeoedri","lpaonsugmlzuweyvrrlgwwdjsgwmoh","kexyawgkinwvjvzwvofqlthmhaicgs"])
 