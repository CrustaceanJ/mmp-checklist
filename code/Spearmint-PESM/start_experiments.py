import argparse
import os
import sys
import subprocess


def main(input_dir, main_path):
    exp_dir = [name for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name))]
    for cur_dir in exp_dir:
        print 'EXP_NAME: %s' % cur_dir
        exp_name = os.path.join(input_dir, cur_dir)
        command = ['./start_experiment.sh', '--script', main_path, '--input', exp_name]
        p = subprocess.Popen(command, stdout=sys.stdout)
        result, _ = p.communicate()
        print result
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Experiments dir', \
                        default=None, type=str)
    parser.add_argument('--script', help='main.py script path', \
                        default=None, type=str)

    args = parser.parse_args()
    
    input_dir = args.input
    main_path = args.script
    
    main(input_dir, main_path)