import bisect

class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        max_dist = self.seats[0]
        seat_to_take = 0
        for i in range(len(self.seats) - 1):
            dist = (self.seats[i + 1] - self.seats[i]) // 2
            if dist > max_dist:
                max_dist = dist
                seat_to_take = self.seats[i] + dist
        if self.N - 1 - self.seats[-1] > max_dist:
            seat_to_take = self.N - 1
        bisect.insort(self.seats, seat_to_take)
        return seat_to_take

    def leave(self, p: int) -> None:
        self.seats.remove(p)
