import subprocess
import numpy as np

# '01_Regular', , '03_Forward', '04_Running'
datasets = ['02_Rotation']

#double quality_level;
#double min_distance;
#double max_diff_distance;

dof = { "quality_level" : (0.06, 0.1, 0.01),
        "min_distance" : (1, 5, 1),
        "max_diff_distance" : (0.5, 2.0, 0.5)
        }

current_dof = "quality_level"

for data in datasets:
    start_argu = dof[current_dof][0]
    end_argu = dof[current_dof][1]
    interval_argu = dof[current_dof][2]

    argu_lists = np.arange(start_argu, start_argu+end_argu, interval_argu)
    print('Running ' + data + ', current degree of freedom is ' + current_dof)
    for argu in argu_lists:
        subprocess.check_call(['./build/SubspaceStab', '../videos/{}.mp4'.format(data), '--output=build/result_{}'.format(data), '--resize=false', '--crop=false', '--{}={}'.format(current_dof, argu)])
        subprocess.check_call(['mkdir', '-p', '{}'.format(current_dof)])
        subprocess.check_call(['ffmpeg', '-i', 'build/result_{}%05d.jpg'.format(data), '-vcodec', 'h264', '-qp', '0', '{}/result_{}_{:3.2f}.mp4'.format(current_dof, data, argu)])
        subprocess.call('rm build/*.jpg', shell=True)
#        subprocess.check_call(['mkdir', '-p', 'out'])
#        subprocess.check_call(['ffmpeg', '-y', '-i', '{}/result_{}_{:3.2f}.mp4'.format(current_dof, data, argu), '-filter:v', 'crop=540:300:50:30', '-c:a', 'copy', 'out/{}/result_{}_{:3.2f}.mp4'.format(current_dof, data, argu)])

