  state = [0]*k
        ans = sum(cookies)
        
        def search(state, idx):
            nonlocal ans
            if idx == k:
                if sum(cookies) == 0:
                    ans = min(ans, max(state))
                return
            
            for i in range(len(cookies)):
                if cookies[i] == 0:
                    continue
                state[idx] += cookies[i]
                temp = cookies[i]
                cookies[i] = 0

                if state[idx] < ans:
                    search(state, idx)
                    search(state, idx+1)

                state[idx] -= temp
                cookies[i] = temp

        search(state, 0)
        return ans
