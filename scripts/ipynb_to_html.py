import glob
import os

'''
convert ./*.ipynb to html, need jupyter
'''

fps = glob.glob('*.ipynb')

if not fps:
    print('current folder has no notebook(s).')
else:
    fps.sort()
    for fp in fps:
        cmd = 'jupyter nbconvert --to html "%s"' % fp
        os.system(cmd)
        print('## %s ## convert success!' % fp)
