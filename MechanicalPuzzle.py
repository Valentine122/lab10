class MechanicalPuzzle:
    mechanicalPuzzle_amount = 0
    
    def __init__(self, elements_count=None, garanty="N/A", material="N/A", puzzle_type="N/A",
                production_year=2020, producer_country="Ukraine", price_in_UAH=None):
        self._elements_count = elements_count
        self._garanty = garanty
        self._material = material
        self._puzzle_type = puzzle_type
        self._production_year = production_year 
        self._producer_country = producer_country
        self._price_in_UAH = price_in_UAH
        MechanicalPuzzle.mechanicalPuzzle_amount +=1
        
    def __del__(self):
        print("Mechanical Puzzle deleted.")

    def __str__(self):
        return str(self._elements_count) + ', ' + self._garanty + \
        ', ' + self._material + ', ' + self._puzzle_type + \
        ', ' + str(self._production_year) + ', ' + self._producer_country + \
        ', ' + str(self._price_in_UAH)

    @staticmethod
    def get_mechanicalPuzzle_amount():
        return  MechanicalPuzzle.mechanicalPuzzle_amount


if __name__ == "__main__":
    first_mechanicalPuzzle = MechanicalPuzzle(2000, '1 year', 'wood', 'A3',  2015,'USA', 1500)
    second_mechanicalPuzzle = MechanicalPuzzle(4000, '2 year')
    third_mechanicalPuzzle = MechanicalPuzzle()

    print('First Mechanical Puzzle:', first_mechanicalPuzzle)
    print('Second Mechanical Puzzle:', second_mechanicalPuzzle)
    print('Third Mechanical Puzzle:', third_mechanicalPuzzle)
    print('\nAmount of Mechanical Puzzle:', MechanicalPuzzle.get_mechanicalPuzzle_amount())
