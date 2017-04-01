    # import the python subprocess module
import subprocess
def run_cmd(args_list):
	print('Running system command: {0}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return =  proc.returncode
        return s_return, s_output, s_err 

if __name__ == '__main__':
    (ret, out, err)= run_cmd(['hdfs', 'dfs', '-put', '/home/mmcoe/Desktop/sample.csv', 'hdfs://localhost:9000/temp'])
    
