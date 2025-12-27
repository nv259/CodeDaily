class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        room_time = [[0, room_idx] for room_idx in range(n)]

        room_usage_counter = [0] * n

        for start, end in meetings:
            available_rooms = []
            available_time = -1
            while len(room_time):
                available_time, room_idx = heapq.heappop(room_time)

                if available_time <= start:
                    available_rooms.append(room_idx)
                else:
                    heapq.heappush(room_time, [available_time, room_idx])
                    break 
            
            if len(available_rooms):
                lowest_room_idx = min(available_rooms)
                available_time = start
            else:
                available_time, room_idx = heapq.heappop(room_time)
                lowest_room_idx = room_idx

            for room_idx in available_rooms:
                if lowest_room_idx != room_idx:
                    heapq.heappush(room_time, [0, room_idx])

            room_usage_counter[lowest_room_idx] += 1
            duration = end - start
            heapq.heappush(room_time, [max(available_time, start) + duration, lowest_room_idx])

        max_usage = 0
        ans = 0
        for room_idx in range(n):
            if max_usage < room_usage_counter[room_idx]:
                ans = room_idx
                max_usage = room_usage_counter[room_idx]
            
        return ans