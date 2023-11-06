class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            if len(state) == len(nums):
                return True
            return False
        def get_candidates(state):
            return [candidates for candidates in nums if candidates not in state]
        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()
        solutions = []
        state = []
        search(state, solutions)
        print(state)
        return solutions