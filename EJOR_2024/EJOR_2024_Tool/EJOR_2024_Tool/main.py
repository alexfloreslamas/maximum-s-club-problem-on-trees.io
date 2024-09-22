import yaml
import sys

import Tests.Testing.run_Schafers_and_Max_DsT as m2

# An example of how to run this code:
#   1.- Open a command-line interpreter and navigate to the 'EJOR_2024_Tool' folder
#   2.- Type the following command: python main.py Settings/EJOR_2024_small_example.yaml
#   3.- If the above command does not work, try: python3.10 main.py Settings/EJOR_2024_small_example.yaml


def _execute_script(script_configurations: dict):
    if script == 'run_2':
        m2.execute(script_configurations)
    else:
        print(f"Script >>> {script} <<< not configured yet\n")


if __name__ == "__main__":
    print(f"\nRunning {__file__}\n")

    with open(sys.argv[1]) as f:  # Loads the config file
        config = yaml.load(f, Loader=yaml.FullLoader)

    script_list = config['scripts']

    for script in script_list:  # Loops through the scripts list and executes the script
        script_config = config[script]
        _execute_script(script_config)

    print("\n")
