import numpy as np
import matplotlib.pyplot as plt


class CityGrid:
    def __init__(self, n, m, obstruction_threshold=0.3):
        self.grid = np.zeros((n, m))
        self.obstructed_blocks = np.random.choice([0, 1], size=(n, m),
                                                  p=[1 - obstruction_threshold, obstruction_threshold])
        self.grid[self.obstructed_blocks == 1] = -1

    def place_tower(self, x, y, r):
        coverage = np.zeros_like(self.grid)
        for i in range(max(0, x - r), min(self.grid.shape[0], x + r + 1)):
            for j in range(max(0, y - r), min(self.grid.shape[1], y + r + 1)):
                if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                    coverage[i, j] = 1
        return coverage

    def display_tower_coverage(self, tower_coverage):
        plt.imshow(self.grid, cmap='Greys', alpha=0.5)
        plt.imshow(tower_coverage, cmap='Blues', alpha=0.5)
        plt.show()

    def place_towers_optimally(self, r):
        towers = []
        covered = np.zeros_like(self.grid)
        while np.min(covered) == 0:
            best_tower = None
            best_tower_coverage = None
            best_tower_covered = None
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i, j] != -1 and covered[i, j] == 0:
                        tower_coverage = self.place_tower(i, j, r)
                        newly_covered = np.logical_and(tower_coverage, self.grid != -1)
                        if np.sum(newly_covered) > np.sum(best_tower_covered):
                            best_tower = (i, j)
                            best_tower_coverage = tower_coverage
                            best_tower_covered = newly_covered
            towers.append(best_tower)
            covered = np.logical_or(covered, best_tower_coverage)
        return towers

    def find_most_reliable_path(self, start_tower, end_tower):
        # implement algorithm to find most reliable path between two towers
        pass

    def visualize_city(self):
        # implement visualization of the city grid including obstructed blocks, towers, coverage areas, and data paths
        pass
