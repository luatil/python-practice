class Img:

    def __init__(self, data : [[float]]) -> None:
        self.img = data

    def get_val(self, pos : (int, int) ) -> float:
        return self.img[pos[0]][pos[1]]

    def is_pos_valid(self, pos : (int, int)) -> bool:
        return 0 <= pos[0] < len(self.img) and 0 <= pos[1] < len(self.img[0])

    def get_neighboors(self, pos : (int, int)) -> [(int, int)]:
        traversal_pattern = ((0, -1), (-1, 0), (0, 1), (1, 0))
        row, column = pos
        return [(row + x, column + y) for x, y in traversal_pattern if self.is_pos_valid((row + x, column + y))]

    def inplace_rec_fill(self, visited : [(int, int)], pos : (int, int), new_pos_value : float) -> None:
        visited.append(pos)
        val = self.get_val(pos)
        self.img[pos[0]][pos[1]] = new_pos_value # Side Effect
        neighboors = self.get_neighboors(pos)
        for el in neighboors:
            if el not in visited and self.get_val(el) == val:
                self.inplace_rec_fill(visited, el, new_pos_value)

    def inplace_flood_fill(self, pos : (int, int), new_pos_value : float) -> None:
        self.inplace_rec_fill([], pos, new_pos_value)
