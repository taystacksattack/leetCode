class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_int = {
                'start': intervals[i][0],
                'end': intervals[i][1]
            }

            last_int_indx = len(stack)-1
            last_int = {
                'start': stack[last_int_indx][0],
                'end': stack[last_int_indx][1]                
            }

            if curr_int['start'] <= last_int['end'] and curr_int['end'] >last_int['end']:
                stack[last_int_indx][1] = curr_int['end']
            elif curr_int['start'] > last_int['end']:
                stack.append(intervals[i])

        return stack