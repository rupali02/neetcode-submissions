class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for w in words for c in w}
        degree = {c: 0 for c in adj}

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for i in range(min_len):
                if w1[i] != w2[i]:
                    adj[w1[i]].append(w2[i])
                    degree[w2[i]] += 1
                    break

        print(adj)

        q = [ c for c in degree if degree[c] == 0]
        res = []

        while q:
            x = q.pop()
            res.append(x)

            for neigh in adj[x]:
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    q.append(neigh)

        return "".join(res) if len(res) == len(adj) else ""

        

        