from datetime import datetime
import os
from zipfile import ZipFile
import maa_win

#yymmdd
def today6(): return datetime.now().strftime('%y%m%d')


def pack(name, out, files):
    """ packs @files(.fst) to zip with name @files(.snd)
            -- expects files to be a list of tuples
        with filename derived from @name, version (of first file), date
        and outputs that to @out folder
    """
    f0, _ = files[0]
    nm = '{}_{}_{}'.format(
        name,
        today6(),
        maa_win.file_version_str(f0, '-'))
    nmo = os.path.join(out, nm + '.zip')

    with ZipFile(nmo, 'w') as zf:
        for f in files:
            zf.write(*f)
