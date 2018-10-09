from TSP import *
from libs.GeneticAlgorithm import GeneticAlgorithm


def main():
    poland = Country()
    poland.add([
        City('Gorlice', (49.655299, 21.159769)),
        City('Sosnowiec', (50.286263, 19.104078)),
        City('Łódź', (51.760229, 19.457209)),
        City('Wrocław', (51.108314, 17.037802)),
        City('Poznań', (52.406376, 16.925167)),
        City('Toruń', (53.013790, 18.598444)),
        City('Zielona Góra', (51.935619, 15.506186)),
        City('Szczecin', (53.428543, 14.552812)),
        City('Rzeszów', (50.041187, 21.999121)),
        City('Kraków', (50.049683, 19.944544)),
        City('Olsztyn', (53.770226, 20.490189)),
        City('Lublin', (51.245376, 22.568278))
    ])
    print('Cities:', end=' ')
    print(*(city for city in poland.cities), sep=', ')
    ga = GeneticAlgorithm(100, mutation_rate=0.5, ptype=Route, args=(poland.cities,))
    ga.run(seconds=2)
    fittest = ga.best()
    best_fitness = fittest.fitness
    print('Best route:', fittest)
    print('Best fitness:', best_fitness)


if __name__ == '__main__':
    main()
