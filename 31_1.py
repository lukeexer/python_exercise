def get_user_input():
    resting_pulse = input('Resting Pulse: ') or '65'
    age = input('Age: ') or '22'
    return validate_input(resting_pulse, age)

def validate_input(resting_pulse, age):
    resting_pulse = str.strip(resting_pulse)
    age = str.strip(age)

    try:
        resting_pulse = int(age)
        age = int(age)
    except:
        print('Please input a numeric value!')
        exit()

    return (resting_pulse, age)

def calculate_rate(resting_pulse, age, intensity):
    rate = (((220 - age) - resting_pulse) * intensity) + resting_pulse
    return rate

def display_output(resting_pulse, age):
    print('Intensity\t| Rate')
    print('----------------|-------')
    for intensity in range(55, 100, 5):
        print(f'{intensity}%      \t| {calculate_rate(resting_pulse, age, intensity)} bpm')


(resting_pulse, age) = get_user_input()
display_output(resting_pulse, age)