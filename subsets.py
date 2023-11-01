class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def is_valid_state(state):
            if len(state)<= len(nums):
                return True
            return False 
        def get_candidates(state):
            
            return set([i for i in nums if len(state) == 0 or i > max(state)])

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        solutions = []
        state = set()
        search(state, solutions)
        return solutions