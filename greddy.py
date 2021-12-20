def get_states_needed():
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

    return states_needed

def get_stations():
    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfive'] = set(['ca', 'az'])

    return stations

def get_optimal_stations(states_needed, stations):
    optimal_stations = []

    while states_needed:
        covered_states = set()
        best_station = None

        for station, states in stations.items():
            covered = states_needed & states

            if len(covered) > len(covered_states):
                best_station = station
                covered_states = covered

        states_needed -= covered_states
        optimal_stations.append(best_station)

    return optimal_stations

def display_output(optimal_stations):
    print(f'The optimal stations are: {optimal_stations}.')

def main():
    states_needed = get_states_needed()
    stations = get_stations()
    optimal_stations = get_optimal_stations(states_needed, stations)
    display_output(optimal_stations)

main()
