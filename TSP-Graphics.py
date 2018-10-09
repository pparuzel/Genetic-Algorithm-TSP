import pygame
from TSP import *
from libs.GeneticAlgorithm import GeneticAlgorithm


def map_cities_onto_screen(cities):
    for city in cities:
        y = -int(150 * (city.x - 54))
        x = int(50 * (city.y - 13.5))
        yield (x, y)


def text_labels(cities, population_size, mutation_rate):
    global arial_norm, arial_small
    arial_norm = pygame.font.SysFont('arial', 25)
    arial_small = pygame.font.SysFont('arial', 16)
    labels = []
    for city, (posx, posy) in zip(cities, map_cities_onto_screen(cities)):
        labels.append((arial_norm.render(city.name, 1, (255, 255, 255)), (posx - 45, posy - 15)))
    labels.append((arial_small.render('Population size: {}'.format(population_size), 1, (255, 255, 255)), (450, 10)))
    labels.append((arial_small.render('City count: {}'.format(len(cities)), 1, (255, 255, 255)), (450, 25)))
    labels.append((arial_small.render('Mutation rate: {}'.format(mutation_rate), 1, (255, 255, 255)), (450, 40)))
    return labels


def main():
    """ Main program """

    ''' Adjustable Parameters '''
    population_size = 20
    mutation_rate = 0.01
    skipped_frames = 108  # recommended: values between 100 and 1000

    ''' Cities '''
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

    ''' Initialization '''
    pygame.init()
    pygame.display.set_caption('Travelling Salesman Problem')
    screen = pygame.display.set_mode((600, 700))
    stat_labels = text_labels(poland.cities, population_size, mutation_rate)
    ga = GeneticAlgorithm(population_size, mutation_rate, ptype=Route, args=(poland.cities,))
    alltime_fittest = ga.alltime_best
    alltime_fitness = 0
    refresh = True

    ''' Main loop '''
    while refresh:
        ''' Event handling '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                refresh = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        event2 = pygame.event.wait()
                        if event2.type == pygame.KEYDOWN and event2.key == pygame.K_SPACE:
                            pause = False
                        elif event2.type == pygame.QUIT:
                            pause = False
                            refresh = False

        ''' Genetic Algorithm process + statistics '''
        ga.run(reps=skipped_frames)
        current_best = ga.best()
        alltime_fittest = ga.alltime_best
        alltime_fitness = alltime_fittest.raw_fitness

        ''' Drawing part '''
        screen.fill((0, 0, 0))
        for point in map_cities_onto_screen(poland.cities):
            pygame.draw.circle(screen, (255, 255, 255), point, 3)
        pygame.draw.aalines(screen, (100, 100, 25), True, list(map_cities_onto_screen(current_best.genes)))
        pygame.draw.aalines(screen, (255, 255, 255), True, list(map_cities_onto_screen(alltime_fittest.genes)))
        screen.blit(arial_small.render('Generation: {}'.format(ga.generation), 1, (255, 255, 255)), (450, 55))
        screen.blit(arial_small.render('Fitness: {:.4f}'.format(alltime_fitness), 1, (255, 255, 255)), (450, 70))
        screen.blit(arial_small.render('Current Fitness: {:.4f}'.format(current_best.raw_fitness), 1, (255, 255, 0)), (450, 85))
        for label in stat_labels:
            screen.blit(label[0], label[1])
        pygame.display.flip()

    print('Best route:', alltime_fittest)
    print('Best fitness:', alltime_fitness)


if __name__ == '__main__':
    main()
