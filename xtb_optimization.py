from rdkit import Chem
import os
import shutil
import subprocess

def xtb_optimization(sdf, xtb_path, logger):
    basename = os.path.basename(sdf)
    dirname = os.path.dirname(sdf)

    pwd = os.getcwd()
    os.chdir(dirname)

    file_name = os.path.splitext(basename)[0]

    xtb_command = os.path.join(xtb_path, 'xtb')
    try:
        with open(f'{file_name}_xtb_opt.log', 'w') as out:
            print(xtb_command, '{}.sdf'.format(file_name))
            subprocess.call([xtb_command, '{}.sdf'.format(file_name), '-opt'],
                            stdout=out, stderr=out)
            shutil.move('xtbopt.sdf', '{}_opt.sdf'.format(file_name))
            os.remove('{}.sdf'.format(file_name))
            logger.info(f'XTB optimization for {os.path.splitext(basename)[0]} completed. '
                        f'Structure saved in {os.path.join(dirname, file_name)}_opt.sdf')
    except Exception as e:
        logger.error(f'XTB optimization for {os.path.splitext(basename)[0]} failed: {e}')

    os.chdir(pwd)
